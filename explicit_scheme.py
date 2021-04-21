import numpy as np  # подключение числ.вычислений
import numba


@numba.njit
def gamma(t, time):
    return 1 - np.exp(-2 * t / time)


@numba.njit(cache=True, parallel=True)
def explicit_solve(x, t, alpha, c, d, number):
    i = len(x) - 1
    k = len(t) - 1
    time = t[k]
    hx = x[1] - x[0]
    ht = t[1] - t[0]
    ksi = (alpha * ht) / (c * hx ** 2)
    eta = d * ht / c
    u = np.zeros((i + 1, k + 1))  # 1 Шаг — заполняем массив решений нулями, в т.ч. слой k = 0
    for m in range(k):
        if m == 0:
            u[0] = np.array([gamma(t[j], time) for j in range(k + 1)])  # 2 Шаг
        j = 1  # 3 Шаг и далее
        while j < i:
            u[j][m + 1] = (1 - 2 * ksi - eta) * u[j][m] + ksi * (u[j + 1][m] + u[j - 1][m])
            j += 1
        u[j][m + 1] = (1 - 2 * ksi - eta) * u[j][m] + 2 * ksi * u[j - 1][m]
    return u
