
import math

#EJERCICIO 1#

def print_hola_mundo():
    print ("Hola Mundo")

#print_hola_mundo()

#1.2

def imprimir_un_verso():
    print ("shaky shaky shaky shaky \n shaky shaky shaky \n whoa")  

#imprimir_un_verso()

#1.3

def raizDe2 ()-> float:
    resultado = (math.sqrt (2))
    print (round (resultado*(10**4)) / 10**4)

#raizDe2()

#1.4

def factorial_de_2()->int:
    print (2)

#factorial_de_2()

#1.5

def perimetro()-> float:
    print (2 * math.pi)

#perimetro()

####EJERCICIO 2####

def imprimir_saludo(nombre: str):
    print ("Hola" , nombre)

#imprimir_saludo("tomi")

#2.2

def raiz_cuadrada_de (numero:int)-> float:
    print (math.sqrt (numero))

#raiz_cuadrada_de(144)

#2.3

def farenheit_a_celsius(temp_far):
    print (((temp_far - 32) * 5 ) / 9)

#farenheit_a_celsius(80)

#2.4

def imprimir_dos_veces_estribillo(estribillo:str):
    print (2 * estribillo)
  
#imprimir_dos_veces_estribillo("hold the line ")

#2.5

def es_multiplo_de(n:int , m:int) -> bool:
    if (n % m == 0):
      print (True)
    else:
      print (False) 
    
#es_multiplo_de (3,2)

#2.6

def es_par(numero: int) -> bool:
    if (es_multiplo_de (numero , 2) == True):
        return True
    else: 
        return False
 
#es_par(24)

#2.7

def cantidad_de_pizzas(comensales: int , min_cant_de_porciones: int):
    print ( math.ceil ((min_cant_de_porciones * comensales) / 8))        

#cantidad_de_pizzas (4,3)

####EJERCICIO 3####

def alguno_es_0(x: float , y: float)-> bool:
    res = x == 0 or y == 0 
    print (res)

#alguno_es_0 ( 1, 0)

#3.2

def ambos_son_0(x: float , y: float)-> bool:
    res = x == 0 and y == 0 
    print (res)

#ambos_son_0 ( 0, 0)

#3.3

def es_nombre_largo (nombre: str) -> bool:
    res = 3 <= len (nombre) <=8
    print (res)

#es_nombre_largo ("tomi")

#3.4

def es_bisiesto (año: int) -> bool:
    res = año % 400 == 0 or (año % 4 == 0 and año % 100 != 0)
    print (res)

#es_bisiesto (2024) 
     
###EJERCICIO 4####

def peso_pino(metros: float) -> float:
    if (metros < 3 ):
     return (metros * 300)
    else: 
        return  (900 + (metros - 3) * 200)


#print (peso_pino (5))   

#4.3

def es_peso_util(peso: float) -> bool:
    res: bool = ( (400 <= peso) and (peso <= 1000) )
    return (res)

#print (es_peso_util (456.1))

#4.4

def sirve_pino(h: float) -> bool:
    res: bool = es_peso_util (peso_pino (h)) 
    return (res)

print (sirve_pino(3)) 