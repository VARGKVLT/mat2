import sys

import matplotlib.pyplot as plt
import numpy as np

# Функция проверки интервала умножения функции от a на функцию от b и проверка произведение на отрицательность
# Это нужно для того чтобы понять что границы находяться на противоположных сторонах
def check_interval(func, a, b):
    print("f(a): ", func(a))
    print("f(b): ", func(b))
    if(func(a)*func(b) < 0):
        return True
    else:
        return False
# функция построение графика
def create_graph(func, a, b):
    xnpy = np.linspace(a, b, 100)
    ynpy = func(xnpy)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.plot(xnpy, ynpy, 'g')
    plt.show()

def half_division(func, a,b):

    # проверяем интервал
    if(check_interval(func, a,b) == False):
        return "Bad interval"

    # строим график
    create_graph(func, a, b)

    # Узнаем значение эпсилон
    eps = float(input("Enter epsilon!\n").replace(",", "."))
    # Вычисление начального приблежения методом деления отрезка на пополам и сохранения его в переменную
    x = (a + b)/2

    # Вычисление текущего значение погрешности как a - b по модулю
    cur_eps = abs(a-b)

    # счетчик итераций
    itercount = 0

    # Вход в цикл который выполняеться пока теущеее приближение не станет меньше заданного
    while(cur_eps > eps):
        itercount +=1
        # Вычисление значения нового приближения
        x = (a + b)/2
        # Проверка знаков функции на концах отрезка и в точке x.
        # Если знаки функции на концах отрезка и в точке x разные,
        # то отбрасывается та половина отрезка, в которой знаки функции совпадают.
        # Если значение функции в точке x равно 0, то возвращается x.
        if func(a) * func(x) > 0 > func(b) * func(x):
            a = x
        elif func(b) * func(x) > 0 > func(a) * func(x):
            b = x
        elif func(x) == 0:
            return x
        else:
            # Вывод ошибки если ни одно из словий не подошло
            sys.exit("something wrong in the hd method\n")
        # Вычисление текущего значение погрешности как a - b по модулю
        cur_eps = abs(a-b)
    print("Number of iterations: ", itercount)
    return x

def simple_iter(func, a, b):

    # проверяем интервал
    if(check_interval(func, a, b) == False):
        return "Bad interval!"

    # строим график
    create_graph(func, a, b)

    # Узнаем значение эпсилон
    eps = float(input("Enter epsilon!\n").replace(",", "."))

    # Вычисление производной функции на a границе интервалла используя формулу конечных разностей
    # Формула конечной разности выглядит как f'(x0) = (f(x1) - f(x0)) / (x1 - x0)
    # В нашем случаи x0 это func(a) а x1 это func(a + eps/100) (x1 - x0) = (a - a + eps/100)
    # Берем за x1 func(a + eps/100) так как это даст совсем небольшой сдвиг
    deriv_a = (func(a + eps/100)-func(a))/(eps/100)

    # Вычисление производной функции на b границе интервалла используя формулу конечных разностей
    # Формула конечной разности выглядит как f'(x0) = (f(x1) - f(x0)) / (x1 - x0)
    # В нашем случаи x0 это func(a) b x1 это func(b + eps/100) (x1 - x0) = (b - b + eps/100)
    # Берем за x1 func(b + eps/100) так как это даст совсем небольшой сдвиг
    deriv_b = (func(b + eps/100)-func(b))/(eps/100)

    # Находим наибольшую производную и назначаем x соответствующий данной переменной a или b
    if(deriv_a > deriv_b):
        max_deriv = deriv_a
        x = a
    else:
        max_deriv = deriv_b
        x = b

    # Вычисление лямбды
    lamda = -1 / max_deriv

    # счетчик итераций
    itercount = 0

    # поиск подходящего корня в итерационном цикле
    while(abs(x + lamda * func(x) - x) > eps):
        x = x + lamda * func(x)
        itercount += 1

    print("Number of iterations: ", itercount)
    return x + lamda * func(x)

def secant_methods(func, a, b):

    # проверяем интервал
    if (check_interval(func, a, b) == False):
        return "Bad interval!"

    # строим график
    create_graph(func, a, b)

    # Узнаем значение эпсилон
    eps = float(input("Enter epsilon!\n").replace(",", "."))

    # счетчик итераций
    itercount = 0

    # Назначение переменной
    x = b-(eps/100)

    while(abs(func(x)) > abs(eps)):
        itercount += 1
        tmp = x
        x = x - (1 / (func(x) - func(b) / (x - b)) * func(x))
        b = tmp

    print("Number of iterations: ", itercount)
    return x
