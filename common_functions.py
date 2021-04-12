import os
import matplotlib.pyplot as plt  # отрисовка графиков
from concurrent import futures
from crank_nicholson_scheme import *


# noinspection SpellCheckingInspection
def linspace(a, b, n):
    h = (b - a) / n
    return np.array([i * h for i in range(n + 1)])


def get_analytical_solutions_row(x, t, alpha, c, d, time, length, number):
    u = np.zeros(len(t))
    for k in range(len(t)):
        summa = 0
        n = 1
        while n <= number:
            lambda_n = np.pi * (2 * n - 1) / (2 * length)
            mu_n = (1 / c) * (alpha * lambda_n ** 2 + d)
            summa += (2 * np.sin(lambda_n * x) * (2 * (d - c * mu_n) * np.exp(-mu_n * t[k]) + mu_n * (2 * c - d *
                                                                                                         time) *
                                                     np.exp(-2 * t[k] / time) + d * (mu_n * time - 2))) / (
                             length * lambda_n * mu_n * c * (mu_n * time - 2))
            n += 1
        u[k] = -summa + 1 - np.exp(-2 * t[k] / time)
    return u


# Аналитическое решение
def analytical_solution(x, t, alpha, c, d, time, length, number):
    path = 'analytical_solutions/I=' + str(len(x) - 1) + ' K=' + str(len(t) - 1) + ' alpha=' + str(alpha) + ' c=' + str(
        c) + ' D=' + str(d) + ' T=' + str(time) + ' l=' + str(length) + ' N=' + str(number)
    if not os.path.isdir('analytical_solutions'):
        os.mkdir('analytical_solutions')
    if os.path.exists(path + '.npz'):
        return np.load(path + '.npz')['arr_0']
    solution = np.array([])

    if __name__ == 'common_functions':
        with futures.ProcessPoolExecutor() as executor:
            todo = []
            for m in range(len(x)):
                future = executor.submit(get_analytical_solutions_row, x[m], t, alpha, c, d, time, length, number)
                todo.append(future)
            for future in futures.as_completed(todo):
                if len(solution) == 0:
                    solution = future.result()
                else:
                    solution = np.vstack((solution, future.result()))

    np.savez_compressed(path, solution)
    return solution


def mean_norm_error(field1, field2):
    return np.mean(abs(field1 - field2))


def uniform_norm_error(field1, field2):
    eps = 0
    for j in range(len(field1)):
        if max(abs(field1[j] - field2[j])) > eps:
            eps = max(abs(field1[j] - field2[j]))
    return eps


def root_mean_square_norm_error(field1, field2):
    eps = 0
    for i in range(len(field1)):
        for j in range(len(field1[0])):
            eps += (field1[i][j] - field2[i][j]) ** 2
    return np.sqrt(eps / (len(field1) * len(field1[0])))


def find_number(alpha, c, d, time, length):
    size = 100
    x = linspace(0, length, size)  # разбиение интервала длины
    t = linspace(0, time, size)  # разбиение интервала времени
    number = 1
    while True:
        field = analytical_solution(x, t, alpha, c, d, time, length, number)
        field2 = analytical_solution(x, t, alpha, c, d, time, length, number + 1)
        maximum = uniform_norm_error(field, field2)
        print(str(maximum))
        print("n = " + str(number))
        if maximum < 10 ** (-9):
            break
        number += 1
    return number


def get_numerical_experiments(i, k, alpha, c, d, time, length, number, hx_rate, ht_rate, method, norm_error):
    results = np.zeros((len(i), 5), dtype=float)
    for j in range(len(i)):
        results[j][0] = i[j]
        results[j][1] = k[j]
        x = linspace(0, length, i[j])
        t = linspace(0, time, k[j])
        field1 = analytical_solution(x, t, alpha, c, d, time, length, number)
        field2 = method(x, t, alpha, c, d)
        eps = norm_error(field1, field2)
        results[j][2] = eps
        x = linspace(0, length, hx_rate * i[j])
        t = linspace(0, time, ht_rate * k[j])
        field1 = analytical_solution(x, t, alpha, c, d, time, length, number)
        field2 = method(x, t, alpha, c, d)
        eps2 = norm_error(field1, field2)
        results[j][3] = eps2
        results[j][4] = eps / eps2
    return results


# Отрисовка одномерных графиков
def plot(x, functions, names, label, name, axis_values=None):
    xy = plt.subplot()
    xy.grid(which='major', color='k')
    xy.minorticks_on()
    xy.grid(which="minor", color='gray', linestyle=':')
    i = 0
    while i < len(functions):
        xy.plot(x, functions[i], label=names[i])
        i += 1
    xy.set_xlabel(label)
    xy.set_ylabel("u(x,t), г/см³")
    if axis_values is not None:
        plt.axis(axis_values)
    xy.legend()
    xy.set_title(name, fontsize=9)
    plt.show()


# Отрисовка одномерных графиков
def plot_test(x, functions, names, label, name, axis_values=None):
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


# Отрисовка двумерных графиков
def plot_2d(field, label):  # field -результат , Label - надпись
    my_map = plt.get_cmap("plasma")  # цветовая схема
    plt.set_cmap(my_map)  # применение схемы к фигуре графика
    plt.figure(figsize=(10, 10))  # создание фигуры с размером 1000*1000 пикселей

    plt.imshow(field)  # наложение на график изобр. ампл. поля
    plt.title(label, fontsize=9)  # заголовок
    plt.colorbar()
    plt.show()
