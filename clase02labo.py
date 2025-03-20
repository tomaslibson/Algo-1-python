#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 14:35:26 2025

@author: Estudiante
"""
import random


nombre_archivo = 'datame.txt'

f = open(nombre_archivo, 'rt' ) # abrir para lectura ('r' de read, 't' de text)
data = f.read()
f.close()
data
# print(data)


archivo2 = 'cronograma_sugerido.csv'

with open(archivo2, 'rt' ) as file:
    for linea in file:
        datos_linea = linea.split(',')
        #print(datos_linea[1])

def juego(lista:list) -> str:
    
    aux = [0,0,0,0,0,0]
    
    for elem in lista:
        aux[elem -1 ] += 1
    
    if 4 in aux:
        return 'poker'
    elif 3 in aux and 2 in aux:
        return 'full'
    elif 5 in aux:
        return 'generala'
    elif aux.count(0) == 1 and (aux[0]==0 or aux[1]== 0 or aux[5]==0):
        return 'escalera'
    

def generala_tirar() -> list:
    
    res = []
    i = 0
    while i < 5 :
        res.append(random.randint(1,6))
        i+=1
        
    return [res, juego(res)]


def generala(lista: list) -> bool:
    
    i = 0
    while i < len(lista):
        if lista[i] != lista[i+1]:
            return False
    return True


print(juego([2,5,4,1,3]))
print(generala_tirar())
    
    

#print(generala_tirar())
            

    
    
    return res
