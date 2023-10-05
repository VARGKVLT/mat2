import numpy as np
from matplotlib import pyplot as plt

def system1():
    # Показываем функцию с которой работаем
    print("x*x + y*y = 4")
    print("y = 3*x*x")
    itercount = 0
    # Узнаем приближение
    eps = float(input("Enter epsilon!\n").replace(",", "."))

    # Построение графика
    a = np.arange(-2, 2, 0.01)
    t = np.arange(0, 2 * np.pi, 0.01)
    r = 4
    plt.plot(a, 3 * a * a, r * np.sin(t), r * np.cos(t), lw=3)
    plt.axis('equal')
    plt.show()

    # Вводим начальные значения для x и y
    xp = float(input("Enter X0!\n").replace(",", "."))
    yp = float(input("Enter Y0!\n").replace(",", "."))

    if xp == 0:
        xp = 0.01
    if yp == 0:
        yp = 0.01

    # Запускаем процесс итерации
    iteration_sys1(xp, yp, eps, itercount)

# Генерируем матрицу Якоби для данной системы в точке x и y
# Матрица Якоби - это матрица первых производных функций системы уравнений
# по каждой из переменных
def get_matrix1(x, y):
    return [[2 * x, 2 * y, 4 - x * x - y * y], [-6 * x, 1, 3 * x * x - y]]

# Итерационный процесс метода Ньютона
# Основной идеей являеться использование формулы Ньютона Xn+1 = Xn - J(Xn)^-1 * F(Xn)
# Xn - текущие приближение Xn+1 - следующие приближение J(Xn) - матрица Якоби для данного Xn
# F(Xn) - вектор значений функций для данного Xn который мы находим используя Гаусса
def iteration_sys1(x, y, eps, itercount):
    f1 = (x * x + y * y - 4)
    f2 = (y - 3 * x * x)

    dx, dy = gauss(get_matrix1(x, y))

    # Полученные системы уравнения необходимые для получения нового приближения
    xi = x + dx
    yi = y + dy

    itercount += 1
    # Условием сходимости явлеться достижением заданной точности
    # то есть достижение разница между текущим и предыдущим значением приближения должно быть меньше заданной точности
    while abs(x - xi) > eps or abs(y -yi) > eps:
        iteration_sys1(xi, yi, eps, itercount)
        return

    print("|x-xi|: " + str(abs(x-xi)) + " |y-yi|: " + str(abs(y - yi)))
    x = xi
    y = yi
    print("x: " + str(x) + " y: " + str(y))
    print("Check: x_i, y_i -> equations")
    print("x^2 + y^2 - 4 = " + str(f1))
    print("y - 3x^2 = " + str(f2))
    print("Number of iterations " + str(itercount))
    return
def system2():
    # Показываем функцию с которой работаем
    print("2x = y/(1 + y*y)")
    print("2y = x/(1+x*x)")
    itercount = 0

    # Узнаем приближение
    eps = float(input("Enter epsilon!\n").replace(",", "."))

    # Построение графика
    x = np.linspace(-np.pi, np.pi, 100)
    t = np.linspace(-np.pi / 1000, np.pi / 1000, 100)
    y = 2 * x + 2 * x * t * t - t
    z = 2 * x + 2 * x * y * y - y
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.plot(y)
    plt.plot(z)
    plt.show()

    # Вводим начальные значения для x и y
    xp = float(input("Enter X0!\n").replace(",", "."))
    yp = float(input("Enter Y0!\n").replace(",", "."))

    if xp == 0:
        xp = 0.01
    if yp == 0:
        yp = 0.01

    # Запускаем процесс итерации
    iteration_sys2(xp, yp, eps, itercount)

def get_matrix2(x, y):
    return [[2 + 2 * y * y, 4 * x * y - 1, -2 * x - 2 * x * y * y + y],
            [4 * x * y - 1, 2 + 2 * x * x, -2 * y - 2 * y * x * x + x]]

# Итерационный процесс метода Ньютона
# Основной идеей являеться использование формулы Ньютона Xn+1 = Xn - J(Xn)^-1 * F(Xn)
# Xn - текущие приближение Xn+1 - следующие приближение J(Xn) - матрица Якоби для данного Xn
# F(Xn) - вектор значений функций для данного Xn который мы находим используя Гаусса
def iteration_sys2(x, y, eps, itercount):
    f1 = (-2 * x + y / (1 + y * y))
    f2 = (-2 * y + x / (1 + x * x))

    dx, dy = gauss(get_matrix2(x, y))

    # Полученные системы уравнения необходимые для получения нового приближения
    xi = x + dx
    yi = y + dy

    itercount += 1
    # Условием сходимости явлеться достижением заданной точности
    # то есть достижение разница между текущим и предыдущим значением приближения должно быть меньше заданной точности
    while abs(x - xi) > eps or abs(y - yi) > eps:

        iteration_sys2(xi, yi, eps, itercount)
        return

    print("|x-xi|: " + str(abs(x - xi)) + " |y-yi|: " + str(abs(y - yi)))
    x = xi
    y = yi
    print("x: " + str(x) + " y: " + str(y))
    print("Check: x_i, y_i -> equations")
    print("-2xy/y^2 = " + str(f1))
    print("-2xy/x^2 = " + str(f2))
    print("Number of iterations " + str(itercount))
    return

# Метод гаусса принимающий на вход матрицу
def gauss(matrix):
    # Цикл проверки матрицы на наличие нулевых элементов на главной диагонали
    # Если был найден нулевой элемент то осущевстляеться перестановка
    # для того чтобы на диагонали были ненулевые элементы
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            for j in range(len(matrix)):
                if matrix[j][i] != 0:
                    for k in range(len(matrix) + 1):
                        matrix[i][k] += matrix[j][k]
                    break

    if matrix[len(matrix) - 1][len(matrix) - 1] == 0:
        for i in range(len(matrix)):
            if matrix[i][len(matrix) - 1] != 0:
                for j in range(len(matrix) + 1):
                    matrix[len(matrix)][j] += matrix[i][j]
                break

    # Приведение матрицы к треугольному виду
    # путем деления каждой строки на соответствующий элемент главной диагонали.
    # c - коэффициент, равный отношению элемента под диагональю к элементу на диагонали.
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            c = matrix[j][i] / matrix[i][i]
            for k in range(len(matrix), i - 1, -1):
                matrix[j][k] -= c * matrix[i][k]

    # Приведение матрицы к диагональному виду путем деления каждой строки
    # на соответствующий элемент главной диагонали.
    for i in range(len(matrix)):
        tmp = matrix[i][i]
        for j in range(len(matrix) + 1):
            matrix[i][j] /= tmp

    # Обратный ход метода Гаусса
    # где all_x - список-вектор решений, в котором все значения равны нулю.
    all_x = [0] * len(matrix)

    # Вычисление значений переменных, с последний по первую итерацию
    all_x[len(matrix) - 1] = matrix[len(matrix) - 1][len(matrix)]

    # Цикл вычитания соответствующих элемента столбца свободных членов суммы
    # произведений значений найденных переменных на соответсвующие коэфиценты матрицы.
    for i in range(len(matrix) - 2, -1, -1):
        all_x[i] = matrix[i][len(matrix)]
        for j in range(i + 1, len(matrix)):
            all_x[i] -= matrix[i][j] * all_x[j]

    # Возврат списка вектора решений all_x
    return all_x