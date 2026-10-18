import numpy as np


def f(r, h):
    return 350 * np.pi * r**2 + 200 * np.pi * r * h


def g(r, h):
    return 500 - np.pi * r**2 * h


def volume(r, h):
    return np.pi * r**2 * h


def penalizacao(r, h):
    violacao = max(0, g(r, h))
    return violacao**2


def FuncaoFinal(r, h, lamb):
    return f(r, h) + lamb * penalizacao(r, h)


d = 1e-5


def dF_dr(r, h, lamb):
    return (
        FuncaoFinal(r+d, h, lamb)
        - FuncaoFinal(r-d, h, lamb)
    ) / (2*d)


def dF_dh(r, h, lamb):
    return (
        FuncaoFinal(r, h+d, lamb)
        - FuncaoFinal(r, h-d, lamb)
    ) / (2*d)


r = 7
h = 6

lamb = 5
alpha = 1e-5

tolerancia = 1e-5


erro = 10
n_norma = 0

k = 0
norma_g = 0

while erro > tolerancia or volume(r, h) < 500:

    var_dF_dr = dF_dr(r, h, lamb)
    var_dF_dh = dF_dh(r, h, lamb)


    norma_g = np.linalg.norm(
        np.array([var_dF_dr, var_dF_dh])
    )

    erro = np.abs((n_norma - norma_g)/norma_g)

    # Critério de parada
    if norma_g < tolerancia and volume(r, h) >= 500:
        break

    n_norma = norma_g

    r = r - alpha * var_dF_dr
    h = h - alpha * var_dF_dh
    k+=1

    if k == 100000:
        print("iterações:", k)
        print("gradiente:", norma_g)
        print("penalização:", penalizacao(r, h))
        print("r:", r)
        print("h:", h)
        print("função final:", FuncaoFinal(r, h, lamb))
        print("custo:", f(r, h))
        print("volume: ", volume(r, h))
        print("\n")
        k = 0

print("iterações:", k)
print("gradiente:", norma_g)
print("penalização:", penalizacao(r, h))
print("r:", r)
print("h:", h)
print("função final:", FuncaoFinal(r, h, lamb))
print("custo:", f(r, h))
print("volume:", volume(r, h))




