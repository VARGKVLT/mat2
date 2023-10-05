from matrix import *
from methods import *
from functions import *

while True:
    inp = input("Enter command(s1 - system 1, s2 - system 2, f1 - function 1, f2 - function 2, f3 - function 3):\n")

    if (inp == "s1"):
        system1()
    elif (inp == "s2"):
        system2()
    elif inp == "f1":
        inp1 = input("Select method(half division - half, secant methods - secant, simple iteration - simple)")
        if inp1 == "half":
            a, b = [float(x) for x in input("Your interval(<a> <b>):").replace(",", ".").split()]
            print(half_division(function1, a, b))
        if inp1 == "secant":
            a, b = [float(x) for x in input("Your interval(<a> <b>):").replace(",", ".").split()]
            print(secant_methods(function1, a, b))
        if inp1 == "simple":
            a, b = [float(x) for x in input("Your interval(<a> <b>):").replace(",", ".").split()]
            print(simple_iter(function1, a, b))


    elif inp == "f2":

        inp1 = input("Select method(half division - half, secant methods - secant, simple iteration - simple)")

        if inp1 == "half":
            a, b = [float(x) for x in input("Your interval(<a> <b>):").replace(",", ".").split()]

            print(half_division(function2, a, b))

        if inp1 == "secant":
            a, b = [float(x) for x in input("Your interval(<a> <b>):").replace(",", ".").split()]

            print(secant_methods(function2, a, b))

        if inp1 == "simple":
            a, b = [float(x) for x in input("Your interval(<a> <b>):").replace(",", ".").split()]

            print(simple_iter(function2, a, b))



    elif inp == "f3":

        inp1 = input("Select method(half division - half, secant methods - secant, simple iteration - simple)")

        if inp1 == "half":
            a, b = [float(x) for x in input("Your interval(<a> <b>):").replace(",", ".").split()]

            print(half_division(function3, a, b))

        if inp1 == "secant":
            a, b = [float(x) for x in input("Your interval(<a> <b>):").replace(",", ".").split()]

            print(secant_methods(function3, a, b))

        if inp1 == "simple":
            a, b = [float(x) for x in input("Your interval(<a> <b>):").replace(",", ".").split()]

            print(simple_iter(function3, a, b))
    else:
        print("wrong input!\n")
