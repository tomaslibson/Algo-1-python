import math

##EJERCICIO 1

def contar_lineas(archivo: str) -> int:
    file = open(archivo, "r")
    texto = file.readlines()
    return len(texto)

#print (contar_lineas ("test.txt"))

#1.2

def existe_palabra(palabra: str ,archivo: str) -> bool:
    file = open (archivo, "r")
    texto = file.readlines()
    
    res = False

    for lineas in texto:
        if palabra in lineas:
            res = True
    return res

#print (existe_palabra("Descenso", "test.txt"))
#print (existe_palabra("boca", "test.txt"))

#1.3

def cantidad_apariciones(archivo: str, palabra: str) -> int:
    file = open (archivo, "r")
    texto = file.readlines()
    res = 0
    i = 0
    while i < len(texto):
        for elemento in texto[i].split():
            if elemento == palabra:
              res+=1

        i+=1      
    return res

#print (cantidad_apariciones ("test.txt" , "esto"))    
#print (cantidad_apariciones ("test.txt" , "boca")) 

##EJERCICIO 2

def clonar_sin_comentarios(archivo: str):
    file = open (archivo, "r")
    texto = file.readlines()
    messi = open("messi.txt","w")
    i = 0
    res = []
    while i < len(texto):
        linea = texto[i].split()
        if linea[0] != "#":
            res.append(texto[i])
        i+=1
    
    messi.writelines(res)
    messi.close()

#clonar_sin_comentarios("test.txt")

##EJERCICIO 3

def invertir_lineas(archivo: str):
    file = open (archivo, "r")
    texto = file.readlines()
    reverso = open("reverso.txt","w")
     
    res = []

    i= len(texto) - 1

    while i >= 0:
        res.append(texto[i])

        i-=1
    
    reverso.writelines(res)
    reverso.close()

#invertir_lineas ("test.txt")
    
##EJERCICIO 4

def agregar_frase_al_final(archivo: str, frase:str):
    file = open (archivo, "r+")
    texto = file.read()

    file.write(frase)
    file.close()

#print (agregar_frase_al_final ("test.txt", " boca"))

##EJERCICIO 5

def agregar_frase_al_principio(archivo: str, frase:str):
    file = open (archivo, "r")
    texto = file.read()
    file.close()

    nuevo = open (archivo, "w")
    nuevo.write(frase + texto)
    nuevo.close()

#agregar_frase_al_principio("test.txt", " y quiero que sepas que ")


##EJERCICIO 6

def listar_palabras_de_archivo(archivo:str) -> list:
    permitidas = ["-","1","2","3","4","5","6","7",
                  "8","9","0","a","b","c","d","e","f","g","h","i","j","k", "l",
                    "m","n" ,"ñ", "o","p","q","r","s","t","u","v","w","x","y","z",
                      "A", "B", "C" , "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                      "N" ,"Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    archivo = open("test.zip", "rb")
    bytes = archivo.read()
    archivo.close()
    palabras = []
    palabra = ""
    
    for b in bytes:
        char = chr(b)
        if char in permitidas:   
            palabra+= char
        elif (char == " ") and (len(palabra) < 5):
            palabra = ""
        elif ((char == " ") or (char == "\n" )) and (len(palabra) >= 5):
            palabras.append(palabra)
            palabra = ""
##falta que te duevuleva la ultima palabra

    return palabras
    


#print( listar_palabras_de_archivo ("test.zip"))

##EJERCICIO 7

##def calcular_promedio_por_estudiante(notas:str, promedios:str):

######PILAS#######

#EJERCICIO 8
from queue import LifoQueue as Pila
import random


def generar_numero_al_azar(cantidad:int, desde:int,hasta:int) -> Pila[int]:
    p = Pila()
    
    for i in range(cantidad):
        p.put(random.randint(desde,hasta))
        
        
    return imprimirPila(p)

def imprimirPila(Pila):
    res = []
    while not (Pila.empty()):
        res.append(Pila.get())
    
    return res


#print( generar_numero_al_azar (6, 1,100) )

#EJERCICIO 9

def cantidad_elementos(p: Pila) -> int:
    res = len(pila_a_lista(p))
    return res

def pila_a_lista(p: Pila) -> list:
    lista = []
    while not (p.empty()):
        lista.append(p.get())
    return lista

miPila: Pila = Pila()
miPila.put(5)
miPila.put(5)
miPila.put(5)
miPila.put(5)
miPila.put(5)
miPila.put("seis")
#print(cantidad_elementos(miPila))

#EJERCICIO 10

def bucar_el_maximo(p: Pila[int]) -> int:
   #lista = pila_a_lista(p)
    i = 0
    res = 0
     
    while not (p.empty()):
        i = p.get()
        if i > res:
            res = i
    """  while i < len(lista):
        if res < lista[i]:
            res = lista[i]

        i+=1            
    return res """
    return res
    

miPInt = Pila()
miPInt.put(1)
miPInt.put(5)
miPInt.put(167)
miPInt.put(0)

#print(bucar_el_maximo(miPInt))

#EJERCICIO 11




