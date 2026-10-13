import numpy as np

def f(r, h):
    return 350 * np.pi * r**2 + 200 * np.pi * r *h

def g(r, h):
    return 500 - np.pi * r**2 * h

def volume(r, h):
    return np.pi * r**2 * h

def penalizacao(r, h):
    violacao = max(0, g(r, h))
    return violacao**2

def FuncaoFinal(r, h, lamb):
    return f(r, h) + lamb * penalizacao(r, h)

d = 10**-5
def dF_dr(r, h, lamb):
    return (FuncaoFinal(r+d, h, lamb) - FuncaoFinal(r, h, lamb))/d

def dF_dh(r, h, lamb):
    return (FuncaoFinal(r, h+d, lamb) - FuncaoFinal(r, h, lamb))/d




r = 2
h = 3
lamb = 5
alpha = 1e-5
tolerancia = 0.000001
erro = 1
i = 0
k = 0

while np.abs(erro - f(r, h)) > tolerancia:

    var_dF_dr = dF_dr(r, h, lamb)
    var_dF_dh = dF_dh(r, h, lamb)

    norma_g = np.linalg.norm(np.array([var_dF_dr, var_dF_dh]))
    

    if i == 10000:
        print(k)
        k+= 1
        print("modulo vetor: ", norma_g)
        print("penalização: " , penalizacao(r, h))
        print("r: " , r)
        print("h: " , h)
        print("função final: " , FuncaoFinal(r, h, lamb))
        print("custo: " , f(r, h))
        print("volume: ", volume(r, h))
        print("\n")
        i = 0
    
    erro = f(r, h)

    r = r - alpha * var_dF_dr
    h = h - alpha * var_dF_dh

    i += 1
