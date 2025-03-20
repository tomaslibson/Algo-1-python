#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 13:16:35 2025

@author: Estudiante
"""
#1
def pertenece (lista: list[int], elem: int) -> bool :
    
    if elem in lista:
        return True
    return False

print(pertenece([1,2,3,4],2))


#2

def mas_larga (lista1:list, lista2: list) -> list:
    
    if len(lista1) > len(lista2):
        return lista1
    elif len(lista1) < len(lista2):
        return lista2
    else:
        return []
    
print(mas_larga([1,1,1,1], [2,2,2,2,2,2,2]))

#3
def mezclar(cadena1: str, cadena2: str) -> str:
    
    res = ''
    
    if mas_larga(cadena1, cadena2) != cadena2:
        i = 0
        while i < len(cadena2):
            res += cadena1[i]
            res += cadena2[i]
            i+=1
        while i < len(cadena1):
            res += cadena1[i]
            i+=1
        return res
    else:
        i = 0
        while i < len(cadena1):
            res += cadena1[i]
            res += cadena2[i]
            i+=1
        while i < len(cadena2):
            res += cadena2[i]
            i+=1
        return res
     

     
print(mezclar('Pepe','Josefa'))
print(mezclar('hola','ch'))
print(mezclar('hola','chau'))


## 4
#a
años = 30
credito = 5000000
cuotas = 2684.11
total = años * 12 * cuotas
print(total)

#b



# 5
def geringoso(palabra: str) -> str:
    vocales = ['a','e','i','o','u']
    res = ''
    i = 0
    
    while i < len(palabra):
        letra = palabra[i]
        if letra in vocales:
            res+= letra + 'p' + letra
        else:
            res+= letra
        i+=1        
    return res[:-1]
    
    
def traductor_geringoso(lista:list[str]) -> dict:
    
    res = {}
    
    for palabra in lista:
        res[palabra] = geringoso(palabra)
    return res

print(traductor_geringoso(['banana', 'manzana', 'mandarina']))
    




