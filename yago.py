import math
from queue import LifoQueue as Pila
import random
from queue import Queue as Cola

#########################

def imprimirCola(c: Cola) -> list:

    res = []
    c2 = Cola()
    while not c.empty():
        n = c.get()
        res.append(n)
        c2.put(n)
    while not c2.empty():
        c.put(c2.get())
    return res

############################


#EJERCICIO 1

def reordenar_cola_priorizando_vips(f: Cola) -> Cola:
    res = Cola()

    f2 = Cola()

    aux = Cola()

    while not f.empty():
        cliente = f.get()
        if cliente[1] == "vip":
            res.put(cliente)
        else:
            aux.put(cliente)
        f2.put(cliente)
    while not aux.empty():
        res.put(aux.get())
    while not f2.empty():
        f.put(f2.get())
    return res

fila = Cola()
fila.put(("tomi","vip"))
fila.put(("t","comun"))
fila.put(("o","vip"))
fila.put(("m","vip"))
fila.put(("tomi","vip"))

print(imprimirCola(reordenar_cola_priorizando_vips(fila)))
print(reordenar_cola_priorizando_vips(fila).queue)

#ejercicio 2

desvio = "me desvio siempre"
banco = "me la banco y no me desvio"

def torneo_de_gallinas(estrategias: dict[(str,str)]) -> dict[(str, int)]:
    desvio = "me desvio siempre"
    banco = "me la banco y no me desvio"

    puntajes = {}
    keys = list(estrategias.keys())
    listado = list(estrategias.items())

    for k in keys:
        puntajes[k] = 0

    for (jugador, play) in listado:
            for (jugador2, play2) in listado:
                if jugador != jugador2:
                    if play == desvio and play2 == desvio:
                        puntajes[jugador]-= 10
                    elif play == desvio and play2 == banco:
                         puntajes[jugador]-= 15
                    elif play == banco and play2 == desvio:
                         puntajes[jugador]+= 10
                    elif play == banco and play2 == banco:
                         puntajes[jugador]-= 5
    return puntajes

d = {"tomi": desvio, "chomas": desvio, "pedro": banco, "jero": banco}

# print(torneo_de_gallinas(d))
                

##ejercicio 3

def quien_gano_el_tateti_facilito(tablero: list[list]) -> int:
    num  = len(tablero[0])
   

    Xtot = 0
    Otot = 0

    TresXseguidas = False
    TresOseguidas = False
    
    res = 0
    for columnas in tablero:
        cantidadDeX= 0
        cantidadDeO= 0
        for n in columnas:
            if cantidadDeX == 3:
                TresXseguidas = True
            elif cantidadDeO == 3:
                TresOseguidas = True
            elif n == "":
                cantidadDeO = 0
                cantidadDeX = 0
            elif n == "x":
                cantidadDeO = 0
                cantidadDeX += 1
                Xtot +=1
            elif n == "o":
                Otot +=1
                cantidadDeX = 0
                cantidadDeO += 1

    if TresXseguidas == True and TresOseguidas == False:
        res = 1
    elif TresXseguidas == False and TresOseguidas == True:
        if (Otot == Xtot or Otot == Xtot + 1):
            res = 2
        else:
            res = 3
    elif TresXseguidas == False and TresOseguidas == False:
        res = 0     
    return res

x = "x"
o = "o"

m1 = [[o,o,x,o,o],  [x,o,"",o,x], [x,o,o,x,x], ["",o,o,x,x], [x,x,x,o,o]] # gana x
m2 = [[x,o,o,o,x],  [x,o,"",o,""], [x,o,"",x,x], ["",o,o,x,x], [x,x,o,o,x]] # gana o
m0 = [[x,o,"",o,x],  [x,o,"",o,""], [x,o,"",x,x], ["",o,o,x,x], [x,x,o,o,x]] # empatan
m3 = [[x,o,o,o,x],  [x,o,"",o,o], [x,o,"",x,o], ["",o,o,x,x], [x,x,o,o,x]] # trampa


# print(quien_gano_el_tateti_facilito(m1))
# print(quien_gano_el_tateti_facilito(m2))
# print(quien_gano_el_tateti_facilito(m0))
# print(quien_gano_el_tateti_facilito(m3))

#ejercicio 4

def cuantos_sufijos_son_palindromos(s: str) -> int:
    num = len(s)
    sufijos = []
    aux = []
    k = 0
    res = 0
    while k < num:
        aux = []
        i = k
        k+=1
        while i < num:
            aux.append(s[i])
            i+=1

        sufijos.append(aux)
    for n in sufijos:
        if capicua(n) == True:
            res+=1
    return res
    

def capicua(s: str) -> bool:
    res = True
    aux = []
    num = len(s)
    i = 0

    while i < num:
        if s[i] != s[num - 1 - i]:
            res = False
        i+=1
    return res




print(cuantos_sufijos_son_palindromos("Diego"))


        



