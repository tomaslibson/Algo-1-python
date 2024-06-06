import math
from queue import LifoQueue as Pila
import random
from queue import Queue as Cola

##
def imprimirPila(p: Pila):
    res = []
    c = Pila()
    while not (p.empty()):
        i = p.get()
        res.append(i)
        c.put(i)
    while not c.empty():
        p.put(c.get())
    return res

miPila: Pila = Pila()
miPila.put(5)
miPila.put(5)
miPila.put(5)
miPila.put(5)
miPila.put(5)
miPila.put("seis")

#print(imprimirPila(miPila))
#print(imprimirPila(miPila))

##

def imprimirCola(s: Cola):
    c = Cola()
    res = []
    while not (s.empty()):
        w = s.get()
        res.insert(0,w)
        c.put(w)
    while not c.empty():
        i = c.get()
        s.put(i)
    
    return res

tuCola = Cola()
tuCola.put(3)
tuCola.put(33)
tuCola.put(1384)
tuCola.put(1384)

#print(imprimirCola(tuCola))
#print(imprimirCola(tuCola))

##

def im_not_split(content:str) -> list[str]:
    res = []
    i = 0
    palabra = ""


    while i < len(content):
        if content[i] == " " or content[i] == "\n":
            if palabra != "":
                res.append(palabra)
                palabra = ""
            
        else: 
            palabra+= content[i]
        
        i+=1
    if i == len(content):
        res.append(palabra)
    return res

l = im_not_split("hola como estas \n me llamo tomi")

print (im_not_split("hola como estas \n me llamo tomi"))
print (len(im_not_split("hola como estas \n me llamo tomi")))
print(l[5])

