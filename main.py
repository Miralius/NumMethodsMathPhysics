from common_functions import *

if __name__ == '__main__':

    length = 10  # см — длина трубки
    I_ = 100 # кол-во интервалов разбиения по длине
    time = 150  # с — время наблюдения
    K = 100  # кол-во интервалов разбиения по времени
    alpha = 0.24  # см²/с — коэффициент диффузии
    c = 0.8  # коэффициент пористости
    d = 0.002  # 1/с — коэффициент пропорциональности концентрации растворенного вещества
    x = linspace(0, length, I_)  # разбиение интервала длины
    t = linspace(0, time, K)  # разбиение интервала времени
    #  number = find_number(alpha, c, d, time, length)
    number = 1000
    field = analytical_solution(x, t, alpha, c, d, time, length, number)

    x_0, = np.where(x >= 0)
    x_1, = np.where(x >= 3)
    x_2, = np.where(x >= 6)
    x_3, = np.where(x >= 9)
    t_0, = np.where(t >= 0)
    t_1, = np.where(t >= 30)
    t_2, = np.where(t >= 75)
    t_3, = np.where(t >= 140)
    plot_2d(field, "Аналитическое решение u(x,t)")
    plot(t, np.array([field[x_0[0]], field[x_1[0]], field[x_2[0]], field[x_3[0]]]),
         np.array(["x = " + str(x[x_0[0]]), "x = " + str(x[x_1[0]]), "x = " + str(x[x_2[0]]), "x = " + str(x[x_3[0]])]),
         "t, с", "Изменение аналитического решения u(x,t) по времени")
    plot(x, np.array([field.T[t_0[0]], field.T[t_1[0]], field.T[t_2[0]], field.T[t_3[0]]]),
         np.array(["t = " + str(t[t_0[0]]), "t = " + str(t[t_1[0]]), "t = " + str(t[t_2[0]]), "t = " + str(t[t_3[0]])]),
         "x, см", "Изменение аналитического решения u(x,t) по координате")

    field_C_N = crank_nicholson_solve(x, t, alpha, c, d)
    plot_2d(field_C_N, "Решения для схемы Кранка-Николсона u(x,t)")
    plot(t, np.array([field_C_N[x_0[0]], field_C_N[x_1[0]], field_C_N[x_2[0]], field_C_N[x_3[0]]]),
         np.array(["x = " + str(x[x_0[0]]), "x = " + str(x[x_1[0]]), "x = " + str(x[x_2[0]]), "x = " + str(x[x_3[0]])]),
         "t, с", "Изменение концентрации вещества u(x,t) по времени")
    plot(x, np.array([field_C_N.T[t_0[0]], field_C_N.T[t_1[0]], field_C_N.T[t_2[0]], field_C_N.T[t_3[0]]]),
         np.array(["t = " + str(t[t_0[0]]), "t = " + str(t[t_1[0]]), "t = " + str(t[t_2[0]]), "t = " + str(t[t_3[0]])]),
         "x, см", "Изменение концентрации вещества u(x,t) по координате")

    plot(t, np.array([field[x_0[0]], field[x_1[0]], field[x_2[0]], field[x_3[0]],
                      field_C_N[x_0[0]], field_C_N[x_1[0]], field_C_N[x_2[0]], field_C_N[x_3[0]]]),
         np.array(["x_a = " + str(x[x_0[0]]), "x_a = " + str(x[x_1[0]]), "x_a = " + str(x[x_2[0]]),
                   "x_a = " + str(x[x_3[0]]), "x = " + str(x[x_0[0]]), "x = " + str(x[x_1[0]]), "x = " + str(x[x_2[0]]),
                   "x = " + str(x[x_3[0]])]), "t, с", "Изменение аналитического и численного решений u(x,t) по времени")
    plot(x, np.array([field.T[t_0[0]], field.T[t_1[0]], field.T[t_2[0]], field.T[t_3[0]], field_C_N.T[t_0[0]],
                      field_C_N.T[t_1[0]], field_C_N.T[t_2[0]], field_C_N.T[t_3[0]]]), np.array(
        ["t_a = " + str(t[t_0[0]]), "t_a = " + str(t[t_1[0]]), "t_a = " + str(t[t_2[0]]), "t_a = " + str(t[t_3[0]]),
         "t = " + str(t[t_0[0]]), "t = " + str(t[t_1[0]]), "t = " + str(t[t_2[0]]), "t = " + str(t[t_3[0]])]), "x, см",
         "Изменение аналитического и численного решений u(x,t) по координате")

    x_1, = np.where(x >= 5)
    t_1, = np.where(t >= 75)
    I_, K = 100, 5
    x1 = linspace(0, length, I_)  # разбиение интервала длины
    t1 = linspace(0, time, K)  # разбиение интервала времени
    field_C_N_1 = crank_nicholson_solve(x1, t1, alpha, c, d)
    t__1, = np.where(t1 >= 75)
    x__1, = np.where(x1 >= 5)

    I_, K = 100, 10
    x2 = linspace(0, length, I_)  # разбиение интервала длины
    t2 = linspace(0, time, K)  # разбиение интервала времени
    field_C_N_2 = crank_nicholson_solve(x2, t2, alpha, c, d)
    t__2, = np.where(t2 >= 75)
    x__2, = np.where(x2 >= 5)

    I_, K = 100, 50
    x3 = linspace(0, length, I_)  # разбиение интервала длины
    t3 = linspace(0, time, K)  # разбиение интервала времени
    field_C_N_3 = crank_nicholson_solve(x3, t3, alpha, c, d)
    t__3, = np.where(t3 >= 75)
    x__3, = np.where(x3 >= 5)

    plot_test(np.array([x, x1, x2, x3], dtype=object), np.array([field_C_N.T[t_1[0]], field_C_N_1.T[t__1[0]],
                                                                 field_C_N_2.T[t__2[0]], field_C_N_3.T[t__3[0]]],
                                                                dtype=object),
              np.array(["t_a", "t_" + str(len(t1) - 1), "t_" + str(len(t2) - 1), "t_" + str(len(t3) - 1)]), "x, см",
              "Тест сходимости разностного решения к точному, t = " + str(t[t_1[0]]) + " с", np.array([9.9, 10, 0.065, 0.102]))
    plot_test(np.array([t, t1, t2, t3], dtype=object), np.array([field_C_N[x_1[0]], field_C_N_1[x__1[0]],
                                                                 field_C_N_2[x__2[0]], field_C_N_3[x__3[0]]],
                                                                dtype=object),
              np.array(["x_a", "x_" + str(len(t1) - 1), "x_" + str(len(t2) - 1), "x_" + str(len(t3) - 1)]), "t, с",
              "Тест сходимости разностного решения к точному, x = " + str(x[x_1[0]]) + " см", np.array([29.75, 30.25, 0.0275, 0.0375]))

    grid_x = np.array([2, 4, 8, 16, 32, 64])
    grid_t = np.array([128, 256, 512, 1024, 2048, 4096])
    print(get_numerical_experiments(
        grid_x, grid_t, alpha, c, d, time, length, number, 2, 2, crank_nicholson_solve, root_mean_square_norm_error))
