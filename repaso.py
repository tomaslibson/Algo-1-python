import math
from queue import LifoQueue as Pila
import random
from queue import Queue as Cola

#EJERCICIO 7


def tieneminus(s: str) -> bool:
    res = False

    for n in s:
        if n >= "a" and n <= "z":
            res = True
    return res

def tienemayus(s: str) -> bool:
    res = False

    for n in s:
        if n >= "A" and n <= "Z":
            res = True
    return res

def tienenum(s: str) -> bool:
    res = False
    l = ["1","2","3","4","5","6","7","8","9","0"]
    for n in s:
        if n in l:
            res = True
    return res


def contraseña(s: str) -> str:
    res = "AMARILLA"

    if len(s) < 5:
        res = "ROJA"
    elif len(s) > 8 and tieneminus(s) == True and tienemayus(s) == True and tienenum(s) == True:
        res = "VERDE"
    return res

# r = "hola"
# a = "amari"
# v = "Am1278oR6"

# print(contraseña(r))
# print(contraseña(a))
# print(contraseña(v))

##EJERCICIO 9

def tresvocalesdistintas(s: str) -> True:
    vocales = ["a","e","i","o","u"]
    aux = ""
    res = False

    for n in s:
        if n.lower() in vocales and n not in aux:
            aux+= n
    if len(aux) == 3:
            res = True
    return res

# print(tresvocalesdistintas("AeI"))


## SEGUNDA PARTE

## EJERCICIO 6

def eliminar_repetidos(s: str) -> str:
    res = ""

    for n in s:
        if n not in res:
            res+=n
    return res

# print(eliminar_repetidos("hhhooolllaaa"))

##EJERCICIO 4.1

def sube():
    saldo = 0
    historial = []
    x = False

   
    while x == False:
        accion = input("Cargar (C)/ Descontar(D)/Finalizar(X): ")
        if accion == "X":
            x = True
        elif accion == "C":
            carga = input("Ingrese su monto a cargar: ")
            saldo+= int(carga)
            historial.append(("C", carga))
        elif accion == "D":
            descuento = input("Ingrese su monto a descontar: ")
            saldo-= int(descuento)
            historial.append(("D", descuento))
    
    res = [saldo, historial]
    return res
    

# print(sube())


##EJERCICIO 5.3

def es_matriz(s: list[list[int]]) -> bool:

    res = True
    i = len(s[0])

    for n in s:
        if len(n) != i:
            res = False
    return res

# print(es_matriz([[1,2],[2,4]]))
# print(es_matriz([[1,2],[2,4,3]]))


## EJERCICIO 5.4

def ordenados(s: list[int])-> bool:
    res = True
    e = s[0]

    for n in s:
        if n > e:
            e = n
        elif n < e:
            res = False
    return res 


def filas_ordenadas(m: list[list[int]]) -> list[bool]:
    res = []
    i = 0

    while i < len (m):
        n = m[i]
        res.append(ordenados(n))
        i+=1
    return res


# m = [[1,2,3,4],[1,2,3,4], [1,2,3,4]]
# m2 = [[1,2,3,4],[1,9,3,4], [8,2,3,4]]
# print(filas_ordenadas(m))
# print(filas_ordenadas(m2))

#############################################
###############################################
################################################

##GUIA 8####

import math
import random
from queue import LifoQueue as Pila
from queue import Queue as Cola

#ejercicio 9

def cantidad_elementos(p: Pila) -> int:

    res = 0
    p2 = Pila()

    while not p.empty():
        e = p.get()
        res+=1
        p2.put(e)
    while not p2.empty():
        p.put(p2.get())
    return res

miPila = Pila()
miPila.put(4)
miPila.put(3)
miPila.put(98)
miPila.put(1)

# print(cantidad_elementos(miPila))
# print(cantidad_elementos(miPila))

#ejercicio 10

def buscar_maximo(p: Pila) -> int:
    res = 0
    p2 = Pila()

    while not p.empty():
        e = p.get()
        p2.put(e)
        if e > res:
            res = e
    while not p2.empty():
        p.put(p2.get())
    return res

# print(buscar_maximo(miPila))
# print(buscar_maximo(miPila))


## ejercicio 11


def esta_bien_balanceada(s: str) -> bool:
    res = True

    l = Pila()

    for n in s:
        if n == "(":
            l.put(n)
        elif n == ")" and l.empty():
            res = False
        elif n == ")" and not l.empty():
            l.get()
    return res 

# print (esta_bien_balanceada ( "1 + ) 2 x 3 ( ( )" ))
# print (esta_bien_balanceada( "1 + ( 2 x 3 = ( 2 0 / 5 ) ) 10 * ( 1 + ( 2 * ( =1)))"))

