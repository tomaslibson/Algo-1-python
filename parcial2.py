import math
from queue import LifoQueue as Pila
import random
from queue import Queue as Cola

##EJERCICIO 1

def acomodar(s: list[str]) -> list[str]:
    res = []
    l = []
    
    for n in s:
        if n == "UP":
            res.append(n)
        else: 
            l.append(n) 
    return res + l


lista= ["LLA", "UP", "LLA", "LLA", "UP"]

# print(acomodar(lista))

#EJERCICIO 2

def pos_umbral(s: list[int], u: int) -> int:
    res = -1
    tot = 0

    i = 0

    while tot < u:
        if s[i] > 0:
            tot+= s[i]
        res = i
        i+=1   
    return res

flujo = [1,-2,0,5,-7,3]
limite = 5  

# print(pos_umbral(flujo,limite))

##EJERCICIO 3

def columnas_repetidas(mat: list[list[int]]) -> bool:
    columnas = len(mat[1])
    mitad = int(columnas / 2)
    res = True

    for f in mat:
        i = 0
        while i < mitad and res == True:
            if f[i] != f [i + mitad]:
                res = False

            i+= 1
    return res



    
    return res

T = [[1,2,1,2],[-5,6,-5,6],[0,1,0,1]]
F = [[1,2,1,2],[-5,6,-5,6],[0,1,0,2]]

tr = [[1,2,1,1,2,1],[-5,6,-5,-5,6,-5],[0,1,0,0,1,0]]
fa = [[1,2,1,1,2,1],[-5,6,-5,0,1,3],[0,1,0,0,1,0]]

# print(columnas_repetidas(T))
# print(columnas_repetidas(F))

# print(columnas_repetidas(tr))
# print(columnas_repetidas(fa))

##EJERCICIO 4

def cuenta_posiciones_por_nacion(naciones: list[str], torneos: dict[int, list[str]]) -> dict[str, list[int]]:
    res: dict = {}
    for nacion in naciones:
        res[nacion] = [0] * len(naciones)

    for anio in torneos.keys():
        for i in range(len(torneos[anio])):
            res[torneos[anio][i]][i] += 1
    
    return res

    
                    
naciones = ["arg", "aus", "nz", "sud"]
torneos = {2023:["nz", "sud", "arg", "aus"], 2022:["nz", "sud", "aus", "arg"]}

print(cuenta_posiciones_por_nacion(naciones, torneos))