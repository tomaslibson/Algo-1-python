import math
import random
from queue import LifoQueue as Pila
from queue import Queue as Cola

###############################

def reordenar_cola_priorizando_vips(fila: Cola) -> Cola:
    res = Cola()
    aux = Cola()
    c2 = Cola()

    while not fila.empty():
        cliente =  fila.get()
        if "vip" in cliente: 
            res.put(cliente)
        else:
            aux.put(cliente)

        c2.put(cliente)
    
    while not aux.empty():
        res.put(aux.get())
    while not c2.empty():
        fila.put(c2.get())

    return res

miCola= Cola()
miCola.put(("1", "vip"))
miCola.put(("3","comun"))
miCola.put(("4", "comun"))
miCola.put(("2", "vip"))


# print(list(miCola.queue))

# print(list(reordenar_cola_priorizando_vips(miCola).queue))


########################################

def cuantos_sufijos_son_palindromos(palabra: str) -> int:
    res = 0

    sufijo = sufijos(palabra)
    print(sufijo)
    for suf in sufijo:
        if capicua(suf) == True:
            res+=1
    return res



def capicua(s: str) -> bool:

    res = True

    i = 0
    while i < len(s):
        if s[i] != s[len(s)-1-i]:
            res = False
        i+=1
    return res


def sufijos(s: str) -> list[str]:
    res = []
 
    i = -1
    aux = ""
    while i < len(s):
        res.append(aux)
        i+=1
        aux = ""
        for k in range(i,len(s)):
            aux+=s[k]
    res.pop(0)
    return res
    

l = "oosoo"

print(cuantos_sufijos_son_palindromos(l))

