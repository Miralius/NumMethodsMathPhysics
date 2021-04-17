import numpy as np  # подключение числ.вычислений
import numba


@numba.njit
def gamma(t, time):
    return 1 - np.exp(-2 * t / time)


@numba.njit(cache=True, parallel=True)
def implicit_solve(x, t, alpha, c, d):
    i = len(x) - 1  # Инициализация всех констант и массивов
    k = len(t) - 1
    u = np.zeros((i + 1, k + 1))  # 1 Шаг — заполняем массив решений нулями, в т.ч. слой k = 0
    print("Лиза, где алгоритм?")
    return u
