import math
from queue import LifoQueue as Pila
import random
from queue import Queue as Cola


#ejercicio 1

def stock_productos(s: list[(str, int)]) -> dict:

    res = {}

    for (producto, precio) in s:
        res[producto] = [precio,precio]
    
    for (producto, precio) in s:
        for (producto2,precio2) in s:
            if producto == producto2:
                if precio2 < precio:
                    res[producto][0] = precio2
                if precio2 > precio:
                    res[producto][1] = precio2
                
    return lista_a_tupla (res)

def lista_a_tupla(d: dict) -> dict:
    res = {}
    
    for (k,[min, max]) in d.items():
        res[k] = (min,max)
    return res

stock = [("cartera", 10), ("moño", 5), ("cartera", 5), ("moño", 1)]

print(stock_productos(stock))

##ejercicio 2

def filtrar_codigos(c: list[int]) -> list[int]:
    res = []

    for codigo in c:
        if es_primo(ultimos3(codigo)) == True:
            res.append(codigo)
    return res

def ultimos3 (n : int) ->int:
    res = ""

    t = int( n % 10)
    s = int((n/10) % 10)
    p = int( ((n/10)/10) % 10) 

    res+=str(p)
    res+=str(s)
    res+=str(t)
    
    return int(res)



def es_primo(n: int) -> bool:
    res = True

    aux = []
    i = 2
    while i < n:
        if n % i == 0:
            aux.append(i)
        i+=1
    if len(aux) != 0:
        res = False
    return res    
        
s = [2002,1330013, 512, 11101, 12331231017, 107]

print(filtrar_codigos(s))

#ejercicio 3

def subsecuencias_mas_larga(pacientes: list[int]) -> int:

    res = [0,0]

    cant = 0
    indice = 0

    i = 0
    while i < len(s):
        if s[i] == "perro" or s[i] == "gato" :
            indice = i - cant
            cant+=1
            if cant > res[0]:
                res = [cant, indice]
        else:
            cant= 0
            indice = 0
        i+=1
    return res[1]



s = ["gato","gato","gao","gato", "tucan","p", "p", "gato", "perro", "perro", "gato"]

# print(subsecuencias_mas_larga(s))

#ejercicio 4

def fila_columna(m: list[list]) -> list[list]:
    

    aux = []
    
    for i in range(len(m[0])):
        aux.append([])
    
    for fila in m:
        for k in range(len(m[0])):
            aux[k].append(fila[k])
    
    return aux

m = [["T", "P", "T", "T", "P", "T","T"], 
     ["T", "P", "P", "T", "T", "T","T"],
       ["T", "P", "T", "T", "T", "T","T"],
         ["T", "P", "T", "P", "T", "P","T"],
                    # f  f    f     f     
         ["P", "T", "T", "T", "T", "T","T"], 
         ["P", "T", "T", "T", "T", "T","T"], 
         ["P", "T", "T", "T", "T", "T","T"], 
         ["P", "T", "T", "T", "T", "T","P"]]
                                        # False

# print(fila_columna(m))


def un_responsable_por_turno(grilla: list[list[str]]) -> list[(bool,bool)]:
    res = []
    columnas = fila_columna(grilla)
    mediodia = int(len(columnas[0]) / 2)
    dia = len(columnas[0])
    

    for dias in columnas:
            aux = []
            aux2 = []
            tupla = [True,True]
            for i in range(mediodia):
                    aux.append(dias[i])
                    for e in aux:
                        for e2 in aux:
                            if e != e2:
                                tupla[0]= False
            for k in range(mediodia,dia):
                    aux2.append(dias[k])
                    for a in aux2:
                        for a2 in aux2:    
                            if a != a2:
                                tupla[1]= False
                    
            res.append(tupla)
    return res
        
            



# print(fila_columna(m))
# print(un_responsable_por_turno(m)) 
        
                 
            
    
            



