import os

import matplotlib.pyplot as plt  # отрисовка графиков
from numba import prange

from crank_nicholson_scheme import *


# noinspection SpellCheckingInspection
@numba.njit
def linspace(a, b, n):
    h = (b - a) / n
    return np.array([i * h for i in range(n + 1)])


@numba.njit(cache=True, parallel=True)
def get_analytical_solutions(x, t, alpha, c, d, time, length, number):
    solution = np.zeros((len(x), len(t)))
    for k in prange(len(t)):
        for i in range(len(x)):
            summa = 0
            n = 1
            while n <= number:
                lambda_n = np.pi * (2 * n - 1) / (2 * length)
                mu_n = (1 / c) * (alpha * lambda_n ** 2 + d)
                summa += (2 * np.sin(lambda_n * x[i]) * (2 * (d - c * mu_n) * np.exp(-mu_n * t[k]) + mu_n * (2 * c - d *
                                                                                                             time) *
                                                         np.exp(-2 * t[k] / time) + d * (mu_n * time - 2))) / (
                                 length * lambda_n * mu_n * c * (mu_n * time - 2))
                n += 1
            solution[i][k] = -summa + 1 - np.exp(-2 * t[k] / time)
    return solution


# Аналитическое решение
def analytical_solution(x, t, alpha, c, d, number):
    i = len(x) - 1
    k = len(t) - 1
    time = t[k]
    length = x[i]
    path = 'analytical_solutions/I=' + str(i) + ' K=' + str(k) + ' alpha=' + str(alpha) + ' c=' + str(
        c) + ' D=' + str(d) + ' T=' + str(time) + ' l=' + str(length) + ' N=' + str(number)
    if not os.path.isdir('analytical_solutions'):
        os.mkdir('analytical_solutions')
    if os.path.exists(path + '.npz'):
        return np.load(path + '.npz')['arr_0']
    solution = get_analytical_solutions(x, t, alpha, c, d, time, length, number)
    np.savez_compressed(path, solution)
    return solution


@numba.njit
def mean_norm_error(field1, field2):
    return np.mean(abs(field1 - field2))


@numba.njit
def uniform_norm_error(field1, field2):
    eps = 0
    for i in range(len(field1)):
        for j in range(len(field1[0])):
            if max(abs(field1[i][j] - field2[i][j]), eps) > eps:
                eps = abs(field1[i][j] - field2[i][j])
    return eps


@numba.njit
def root_mean_square_norm_error(field1, field2):
    eps = 0
    for i in range(len(field1)):
        for j in range(len(field1[0])):
            eps += (field1[i][j] - field2[i][j]) ** 2
    return np.sqrt(eps / (len(field1) * len(field1[0])))


@numba.njit
def find_number(alpha, c, d, time, length):
    size = 100
    x = linspace(0, length, size)  # разбиение интервала длины
    t = linspace(0, time, size)  # разбиение интервала времени
    number = 1
    while True:
        field = analytical_solution(x, t, alpha, c, d, number)
        field2 = analytical_solution(x, t, alpha, c, d, number + 1)
        maximum = uniform_norm_error(field, field2)
        print(str(maximum))
        print("n = " + str(number))
        if maximum < 10 ** (-9):
            break
        number += 1
    return number


def get_numerical_experiments(i, k, alpha, c, d, time, length, number, hx_rate, ht_rate, method, norm_error):
    results = np.zeros(5, dtype=float)
    results[0] = i
    results[1] = k
    x = linspace(0, length, i)
    t = linspace(0, time, k)
    field1 = analytical_solution(x, t, alpha, c, d, number)
    field2 = method(x, t, alpha, c, d, number)
    eps = norm_error(field1, field2)
    results[2] = eps
    x = linspace(0, length, hx_rate * i)
    t = linspace(0, time, ht_rate * k)
    field1 = analytical_solution(x, t, alpha, c, d, number)
    field2 = method(x, t, alpha, c, d, number)
    eps2 = norm_error(field1, field2)
    results[3] = eps2
    results[4] = eps / eps2
    return results


# Отрисовка одномерных графиков
def plot(x, functions, names, label, name, axis_values=None):
    xy = plt.subplot()
    xy.grid(which='major', color='k')
    xy.minorticks_on()
    xy.grid(which="minor", color='gray', linestyle=':')
    i = 0
    while i < len(functions):
        xy.plot(x[i], functions[i], label=names[i])
        i += 1
    xy.set_xlabel(label)
    xy.set_ylabel("u(x,t), г/см³")
    if axis_values is not None:
        plt.axis(axis_values)
    xy.legend()
    xy.set_title(name, fontsize=9)
    plt.show()
