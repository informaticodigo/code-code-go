import sympy
from sympy.integrals import *
import numpy as np
import matplotlib.pyplot as plt
import math
import datetime


def graficar(min, max, funcion, nombrex, nombrey):
    e = math.e
    pi = math.pi
    t = math.tau
    x = np.linspace(min, max, 100)
    U = eval(funcion)
    plt.figure()
    plt.plot(x, U, 'k')
    plt.xlabel(nombrex)
    plt.ylabel(nombrey)
    plt.grid()
    plt.show()


# graficar(-10, 10, "x**(0 + pi*1j)", "valor de x", "valor de f(x)")
def diferencial(funcion):
    e = math.e
    t = math.tau
    pi = math.pi
    x = sympy.Symbol('x')
    fx = eval(str(funcion))

    DifCalcPyDifx = sympy.diff(fx)

    return DifCalcPyDifx


def f(funcion, valx):
    e = math.e
    t = math.tau
    pi = math.pi
    x = valx
    op = eval(funcion)
    print(op)
    return op


def f_modulo(funcion, valx):
    e = math.e
    t = math.tau
    pi = math.pi
    x = valx
    op = np.abs(eval(funcion))
    print(op)
    return op


# f("x**2", 3)

# diferencial("x**3 + 5*x**5")
def fp(funcion, valx):
    e = math.e
    t = math.tau
    pi = math.pi
    x = valx
    result = eval(str(diferencial(funcion)))
    # print(result)
    return result


def fp_modulo(funcion, valx):
    e = math.e
    t = math.tau
    pi = math.pi
    x = valx
    resultado = np.abs(eval(funcion))
    result = diferencial(resultado)
    # print(result)
    return result

# fp("x**2 - x", -19000)


def optimizar(funcion, st):
    a = st
    b = 1

    cont = 0
    registro = []

    while (True):

        # Primera derivada en a
        df_a = fp(funcion, a)

        a += 0.0000000001
        b += 0.0000000001

        Ua = f(funcion, a)

        # Condicion de finalizacion
        if round(df_a, 14) == 0:
            print('-------------------------------------------------------------')
            print("Valor de x: {:.10f} - Valor de f(x) en ese punto concreto {:.10f}".format(a, Ua))
            registrar = open("registro_fecha_{}.txt".format(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')), 'a')
            registrar.write(str(registro))
            registrar.close()
            break

        cont = cont + 1
        registro.append(["Contador de intentos", cont, "Valor de x", a, "Valor de f(x) en ese punto", Ua])

    return registro


def optimizar_modulo(funcion, st):
    a = st
    b = 1

    cont = 0
    registro = []

    while (True):

        # Primera derivada en a
        df_a = fp_modulo(funcion, a)

        a += 0.0000000001
        b += 0.0000000001

        Ua = f_modulo(funcion, a)

        # Condicion de finalizacion
        if round(df_a, 14) == 0:
            print('-------------------------------------------------------------')
            print("Valor de x: {:.10f} - Valor de f(x) en ese punto concreto {:.10f}".format(a, Ua))
            registrar = open("registro.txt", 'a')
            registrar.write("\n")
            registrar.write("Registro día {}".format(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')))
            registrar.write(str(registro))
            registrar.close()
            break

        cont = cont + 1
        registro.append([cont, a, Ua])
        # print("It: {:02} - Temp: {:.10f} - Costo {:.10f}".format(cont, a, Ua))

    return registro


# optimizar("x**2", -0.00000009)

def integrar(funcion):
    e = math.e
    t = math.tau
    pi = math.pi
    x = sympy.Symbol('x')
    fx = eval(str(funcion))
    DifCalcPyIntx = integrate(fx)

    return DifCalcPyIntx


# print(integrar("2*x"))


def limite(funcion, lim1, lim2):
    e = math.e
    t = math.tau
    pi = math.pi
    x = sympy.Symbol('x')
    a = sympy.Symbol('a')
    b = sympy.Symbol('b')
    c = sympy.Symbol('c')
    y = sympy.Symbol('y')
    h = sympy.Symbol('h')
    fx = eval(str(funcion))

    DifCalcPyLimx = sympy.limit(fx, lim1, eval(str(lim2)))

    return DifCalcPyLimx


# print(limite("x**2**h", "h", "-9"))
