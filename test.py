import math
from queue import LifoQueue as Pila
import random
from queue import Queue as Cola

def fila_columna(m: list[list]) -> list[list]:
    res = []

    cant_columnas = len(m[0])


    for i in range(cant_columnas):
        res.append([])
    
    for filas in m:
        for k in range(cant_columnas):
            res[k].append(filas[k])
    return res

m = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]

print(fila_columna(m))