import numpy as np  # подключение числ.вычислений
import numba


@numba.njit
def gamma(t, time):
    return 1 - np.exp(-2 * t / time)


@numba.njit(cache=True, parallel=True)
def implicit_solve(x, t, alpha, c, d, number):
    i = len(x) - 1
    k = len(t) - 1
    time = t[k]
    hx = x[1] - x[0]
    ht = t[1] - t[0]
    zeta = (alpha * ht) / (c * hx ** 2)
    eta = d * ht / c
    nu_1 = 1 + 2 * zeta + eta
    nu_2 = -zeta
    mu = np.zeros(k)
    a = np.zeros(i)
    b = np.zeros(i)
    u = np.zeros((i + 1, k + 1))  # 1 Шаг — заполняем массив решений нулями, в т.ч. слой k = 0
    for m in range(k):
        if m == 0:
            u[0] = np.array([gamma(t[j], time) for j in range(k + 1)])  # 2 Шаг
            mu = np.array([zeta * gamma(t[j + 1], time) for j in range(k)])
        a[0] = -nu_2 / nu_1  # a1
        b[0] = (u[1][m] + mu[m]) / nu_1  # b1
        j = 2
        while j < i:
            a[j - 1] = -nu_2 / (nu_1 + nu_2 * a[j - 2])  # a_i
            b[j - 1] = (u[j][m] - nu_2 * b[j - 2]) / (nu_1 + nu_2 * a[j - 2])  # b_i
            j += 1
        a[j - 1] = 0  # a_I
        b[j - 1] = (u[j][m] - 2 * nu_2 * b[j - 2]) / (nu_1 + 2 * nu_2 * a[j - 2])  # b_I
        u[j][m + 1] = b[j - 1]
        j -= 1
        while j > 0:  # здесь и далее обратный ход прогонки
            u[j][m + 1] = a[j - 1] * u[j + 1][m + 1] + b[j - 1]
            j -= 1
    return u
