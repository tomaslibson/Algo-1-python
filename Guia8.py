import math
from queue import Queue as Cola
from queue import LifoQueue as Pila
import random



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

def generar_numero_al_azar(cantidad:int, desde:int,hasta:int) -> Pila[int]:
    p = Pila()
    
    for i in range(cantidad):
        p.put(random.randint(desde,hasta))
        
        
    return imprimirPila(p)

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



def generar_nros_al_azar(cantidad: int , desde: int, hasta: int) -> Cola[int]:
    c = Cola()

    while cantidad > 0:
        c.put(random.randint(desde, hasta))
        cantidad-=1
    return imprimirCola(c)

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

#print(generar_nros_al_azar(5,1,100))

#EJERCICIO 14

def cantidad_elementos(c: Cola):
    p = Cola()
    res = 0
    while not c.empty():
        p.put(c.get())
        res+=1
    while not p.empty():
        c.put(p.get())
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
    
    p = Pila()
    while not c.empty():
        i = c.get()
        if i > res:
            res = i
  
        p.put(i)
    while not p.empty():
            w = p.get()
            c.put(w)

    return res

tuCola = Cola()
tuCola.put(3)
tuCola.put(33)
tuCola.put(1384)
tuCola.put(1384)


#print(buscar_el_maximo(tuCola))
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
def pertenece(s: list[int], n: int) -> bool:
    res = False
    i = 0

    while i < len(s):
        if s[i] == n: 
         res = True

        i+=1
    return res  

  
def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:

    res = 1
    c = Cola()
    papel = []
    while not bolillero.empty() :
        bolilla = bolillero.get()
        if pertenece(carton, bolilla) == True:
            carton.remove(bolilla)
            papel.append(bolilla)
        if len(carton) != 0:
            res+=1
        
        c.put(bolilla)
    while not c.empty():
        w = c.get()
        bolillero.put(w)
    while not papel == []:
        carton.append(papel.pop(0))
    return res



def generar_bolillero() -> Cola[int]:
    c = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
         , 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
           24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
             37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61,
               62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    
    bolillero = Cola()
    
    x = 99
    while c != []:
        i = (random.randint(0,x))
        bolillero.put(c[i])
        c.remove(c[i]) 
        x-=1
    return bolillero

#print(generar_bolillero())
#print (cantidad_elementos(generar_bolillero()))

miBolillero = Cola()
miBolillero.put(1)
miBolillero.put(2)
miBolillero.put(3)
miBolillero.put(4)
miBolillero.put(5)

a1 = [2,4]
a2= [1,5]


#print(imprimirCola(b1))
#print(jugar_carton_de_bingo(a1,miBolillero))
#print(jugar_carton_de_bingo(a2,miBolillero))
#print(jugar_carton_de_bingo(a3,b1))



###EJERCICIO 17

def n_pacientes_urgentes(c: Cola [(int,str,str)]) -> int:
    res = 0
    s = Cola()

    while not c.empty():
        x = c.get()
        if x[0] in [1,2,3]:
            res+=1

        s.put(x)    
    while not s.empty():
        c.put(s.get())
    return res

pacientes = Cola()
pacientes.put((1,"leo","cocina"))
pacientes.put((6,"fwqefwo","cocina"))
pacientes.put((2,"lefw","cocina"))
pacientes.put((6,"rgwrg","cocina"))
pacientes.put((2,"lfh","cocina"))
pacientes.put((10,"lasd","cocina"))
pacientes.put((9,"asd","cocina"))

#print(n_pacientes_urgentes(pacientes))


#EJERCICIO 18

def tipo_de_cliente() -> list[str, int, bool, bool]:
    res = []
    res.append(input("Nombre y Apellido: "))
    res.append(input("DNI: "))
    
    preferencial = input("cuenta preferencial (si/no): ")
    if preferencial == "si":
        res.append(True)
    elif preferencial == "no":
        res.append(False)

    prioridad = input("Es mayor de 65, embarazada o movilidad reducida (si/no): ")
    if prioridad == "si":
        res.append(True)
    elif prioridad == "no":
        res.append(False)

    
    return res

def atencion_a_cliente(c: Cola[str, int, bool, bool]) -> Cola[str, int, bool, bool]:
    segunda = Cola()
    tercera = Cola()
    res = Cola()
    c2 = Cola()
    while not c.empty():
        cliente = c.get()
        if cliente[3] == True:
            res.put(cliente)
        else:
            segunda.put(cliente)

        c2.put(cliente)   

    while not segunda.empty():
        cliente2 = segunda.get()
        if cliente2[2] == True:
            res.put(cliente2)
        else:
            tercera.put(cliente2)
    
    while not tercera.empty():
        res.put(tercera.get())

    while not c2.empty():
        c.put(c2.get())
    
    return res

laFila = Cola()
laFila.put(("1", 123415454, True, True))
laFila.put(("5", 123415454, False, False))
laFila.put(("3", 123415454, True, False))
laFila.put(("4", 123415454, True, False))
laFila.put(("2", 123415454, True, True))



#print(imprimirCola(atencion_a_cliente(laFila)))
#print(imprimirCola(laFila))

######DICCIONARIOS################

#EJERCICIO 19
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


def agrupar_por_longitud(archivo:str) -> dict:
    file = open(archivo, "r")
    texto = file.readlines()
    palabras = []
    i = 0
    diccionario = {} 

    while i < len(texto):
        palabras.append(im_not_split(texto[i]))
        i+=1
    for x in palabras:
        for n in x:
            l = len(n)
            if l in diccionario:
                diccionario[l] += 1
            else:
                diccionario[l] = 1 

    file.close()          
    return diccionario

# print(agrupar_por_longitud("diccionarios.txt"))

####### EJERCICIO 21
 
def la_palabra_mas_frecuente(archivo: str) -> str:
    file = open(archivo, "r")
    texto = file.readlines()
    palabras = []
    i = 0
    diccionario = {} 
    max = 0
    valor = "" 
    res = ""
    while i < len(texto):
        palabras.append(im_not_split(texto[i]))
        i+=1
    for n in palabras:
        for x in n:
            if x in diccionario:
                diccionario[x] += 1
            else:
                diccionario[x] = 1
    
    valores = diccionario.values()         
    for valor in valores:
        if valor > max:
            max = valor
    for n in diccionario.items():
        if n[1] == max:
            res+= n[0]
            res+= ","
    file.close()
    return res        
             

# print(la_palabra_mas_frecuente("diccionarios.txt"))


##EJERICICIO 22

historiales = {}


#1
def visitar_sitio(hitoriales: dict[str, Pila[str]], usuario: str, sitio:str):

    if usuario in historiales:
            historiales[usuario].put(sitio)
    else: 
            userPila = Pila()
            historiales[usuario] = userPila
            userPila.put(sitio)  

# visitar_sitio(historiales, "tomi" , "plm")
# visitar_sitio(historiales, "alfre" , "comodo.com")
# visitar_sitio(historiales, "tomi" , "youtube")
# visitar_sitio(historiales, "tomi" , "iggg")
# visitar_sitio(historiales, "soyuntarado" , "la trote en hd")

t = historiales["tomi"]
a = historiales["alfre"]
s = historiales["soyuntarado"]

#print(imprimirPila(t))
# print(imprimirPila(a))
# print(imprimirPila(s))



#2

def navegar_atras(historiales: dict[str, Pila[str]],usuario: str):
    ultimo = historiales[usuario].get()
    n = historiales[usuario].get()

    historiales[usuario].put(n)
    historiales[usuario].put(ultimo)
    historiales[usuario].put(n)


#navegar_atras(historiales, "tomi")
#print(imprimirPila(t))