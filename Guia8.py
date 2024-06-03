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


def esta_bien_balanceada(formula: str) -> bool:
    parentesis = Pila()
    res = True

    for caracteres in formula:
        if caracteres == '(':
            parentesis.put('(')
        elif caracteres == ')' and parentesis.empty():
            res = False
    return res


#print (esta_bien_balanceada ( "1 + ) 2 x 3 ( ( )" ))
#print (esta_bien_balanceada( "1 + ( 2 x 3 = ( 2 0 / 5 ) ) 10 * ( 1 + ( 2 * ( =1)))"))

#EJERCICIO 12

def evaluar_expresion(s: str) -> float:
    num = Pila()
    op = Pila()
    operandos = ['+', '-', '*' , '/']

    i = 0 

    while i < len(s):
        if s[i] not in operandos and s[i] != ' ':
            num.put(float(s[i]))
        elif s[i] == operandos[0]:
            scnd = num.get()
            frst = num.get()
            num.put(frst + scnd)
        elif s[i] == operandos[1]:
            scnd = num.get()
            frst = num.get()
            num.put(frst - scnd)
        elif s[i] == operandos[2]:
            scnd = num.get()
            frst = num.get()
            num.put(frst * scnd)
        elif s[i] == operandos[3]:
            scnd = num.get()
            frst = num.get()
            num.put(frst / scnd)

        i+=1
    return num.get()


    
#print (evaluar_expresion ("3 4 + 5 * 2 -"))
#print (evaluar_expresion (" 7 7 * 1 +"))


###########COLAS##################

#EJERCICIO 13

from queue import Queue as Cola

def generar_nros_al_azar(cantidad: int , desde: int, hasta: int) -> Cola[int]:
    c = Cola()

    while cantidad > 0:
        c.put(random.randint(desde, hasta))
        cantidad-=1
    return imprimirCola(c)

def imprimirCola(Cola):
    res = []
    while not (Cola.empty()):
        res.insert(0,Cola.get())
    
    return res

#print(generar_nros_al_azar(5,1,100))

#EJERCICIO 14

def cantidad_elementos(c: Cola):
    p = Cola()
    res = 0
    while not c.empty():
        p.put(c.get())
        res+=1
    return res

miCola = Cola()
miCola.put(1)
miCola.put(1)
miCola.put(1)
miCola.put(1)
miCola.put(5)

#print (cantidad_elementos(miCola))

#EJERCICIO 15

def buscar_el_maximo(c: Cola[int]) -> int:
    res = 0

    while not c.empty():
        i = c.get()
        if i > res:
            res = i 
    return res

tuCola = Cola()
tuCola.put(3)
tuCola.put(33)
tuCola.put(1384)
tuCola.put(1384)


#print(buscar_el_maximo(tuCola))

#EJERCICIO 16
"1"
def armar_secuencia_de_bingo() -> Cola[int]:
    c = Cola()

    i= 12

    while i > 0:
        c.put(random.randint(0,99))
        i-=1
    return imprimirCola(c)

#print(armar_secuencia_de_bingo())

"2"







