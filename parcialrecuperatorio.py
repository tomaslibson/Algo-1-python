import math
from queue import LifoQueue as Pila
import random
from queue import Queue as Cola


#EJERCICIO 1

def verificar_transacciones(s:str) -> int:
    res = (350 * ap_antes_corte("r",s)) - (56 * ap_antes_corte("v",s))
    return res

def ap_antes_corte(c:str , s:str) -> int:
    
    res = 0
    w = Pila()
    k = 0

    saldo = 0
    p = False
    i = 0
    while i < len(s) and p == False:
        accion = s[i]
        if saldo < 0:
            w.get()
            p == True
        elif accion == "x":
            p = True
        elif accion == "v":
            saldo-=56
            w.put(accion)
        elif accion == "r":
            saldo+=350
            w.put(accion)  
        elif accion == "s":
            w.put(accion)
        i+=1

    while not w.empty():
        x = w.get()
        if x == c:
            res+=1
        k+=1
    return res


# l = "ssrvvrrvvsvvsxrvvv" #714
# l2 = "ssrvvvvsvvsvvv" # 14
# print(verificar_transacciones(l))
# # print(verificar_transacciones(l2))

##EJERCICIO 2

def valor_minimo(s: list[(float, float)]) -> float:

    res = 0

    i = 0

    while i < len(s):
        min = s[i][0]
        if min < res:
            res = min
        i+=1
    return res

d = [(1.0, 5.2), (10.4, 15.1), (19.7, 28.9), (25.4, 35.6), (-3.1, 1.3)] #-3.1
# print(valor_minimo(d))


##EJERCICIO 3



def devulevemin(s: list) -> int:
    res = s[0]

    for n in s:
        if n < res:
            res = n
    return res

def devulevemax(s: list) -> int:
    res = 0 

    for n in s:
        if n > res:
            res = n
    return res

def valores_extremos(s: dict) -> dict:
    res: dict = {}

    for empresa in s.keys():
        res[empresa] = ()
        valoresempresa = []
        for (dia, temperatura) in s[empresa]:
                 valoresempresa.append(temperatura)
                 res[empresa] = (devulevemin(valoresempresa), devulevemax(valoresempresa))
    return res

l = {"YPF" : [(1,10),(15, 6), (31,100)], "ALUA" : [(1,3), (20, 50), (31,30)]}
print(valores_extremos(l))