import math



#EJERCICIO 1

#1.1

def pertenece(s: list , e:int)->bool:
    res = (e in s)
    return res

#print (pertenece ([1,2,3,4], 2))

#1.2

def  divide_a_todos (s: list , e: int) -> bool:
    i: int = 0
    res: bool = True
    
    while ((i < len(s)) & (res == True)):
        if (s[i] % e != 0):
          res = False
        i+=1
    return res
    

#print (divide_a_todos ([6,4,10,8], 2))


#1.3

def suma_total (s: list) -> int:
    i: int = 0
    res: int = 0
    while (i < len (s)):
          res+= s[i]
          i+=1
    return res     

#print (suma_total ([20,1,1,2])) 

#1.4

def ordenados (s: int) -> bool:
    i: int = 0
    e: int = 1
    res: bool = True
     
    while ((e < len (s)) and (res == True)):
        if (s[i] > s[e]):
            res = False
        i+=1
        e+=1
    return res

#print (ordenados ([1,10,198,2000,111111111,0]))       

#1.5

def palabra_7 (s: list) -> bool:
    i: int = 0
    res: bool = False

    while ((i < len (s)) and (res == False)): 
        if ( len (s[i]) > 7):
           res = True
        i+=1
    return res

#print (palabra_7 (["hola", "no", "hay", "muchoss7"]))

#1.6

def capicua (palabra: str) -> bool:
    i: int=0
    e: int= len(palabra) - 1
    res: bool = True 

    while ((i < len (palabra)) and (res == True)):
        if (palabra[i] != palabra[e]):
           res = False 
        i+=1
        e-=1
    return res

#print (capicua ("neuquen"))       


#1.7

def tiene_minuscula (c: str) -> bool:
    res = False
    for char in c:
        if("a" <= char and char <="z"):
           res = True
    return res
      
def tiene_mayus(c: str) -> bool:
    res = False
    for char in c:
        if("A" <= char and char <="Z"):
           res=True
    return res

def tiene_numero(c: str) -> bool:
    res = False
    for num in c:
        if ("0" <= num) and (num <="9"):
            res=True
    return res

def es_Verde(c: str) -> bool:
    if ((len(c) > 8) and (tiene_minuscula(c) == True) and (tiene_mayus(c) == True) and (tiene_numero(c) == True)):
        res = True
    else:
        res = False
    return res

def fortaleza_contraseña (c: str) -> str:
    if (es_Verde(c) == True):
       res = "VERDE"
    else:
        if(len(c) < 5):
            res = "ROJA"
        else:
            res = "AMARILLA"
    return res

#print(fortaleza_contraseña ("12Ar")) #roja
#print(fortaleza_contraseña ("123rrrrrrrr")) #amarilla
#print(fortaleza_contraseña ("123Ar2565y")) #verde    

#1.8

def saldo_actual(list)-> int:
    res = 0
    for tuplas in list:
        if (tuplas[0] == "I"):
          res+= tuplas [1]
        elif (tuplas[0] == "R"):
            res-= tuplas [1]
    return res

#print (saldo_actual ([("I", 2000), ("R", 20),("R", 1000),("I", 300)]))

     
#1.9

def tiene_3_vocales(string: str)->bool:
    vocales = ["a","e","i","o","u"]
    c = 0
    for l in string:
        if l.lower() in vocales:
            c+=1
            vocales.remove(l.lower())  
        
    return c >= 3
          

    
#print (tiene_3_vocales("aeio"))


##EJERCICIO 2

def coloca_0_en_par(s:list):
    i = 0
    while i < len(s):
        if i % 2 == 0:
            s[i] = 0
        i+=1    
    return s                   

#print (coloca_0_en_par([1,2,3,4,1,1,1,1,1,1,1]))

#2.2

def coloca_0_en_par_lista(s:list):
    i = 0
    l = []
    while i < len(s):
        if i % 2 == 0:
            l.append(0)
        else:
            l.append(s[i])     
        i+=1   
    return l

#print (coloca_0_en_par_lista([1,2,3,4,1,1,1,1,1,1,1]))

#2.3 

def cadena_sin_vocales(s:str):
    vocales = ["a","e","i","o","u"]
    l = ""
    for c in s:
        if c not in vocales:
            l+=c
    return l

#print (cadena_sin_vocales ("abce"))

#2.4

def remplaza_vocales(s:str):
    vocales = ["a","e","i","o","u"]
    l = ""
    for c in s:
        if c in vocales:
           l+="-"
        else:
            l+=c
    return l

#print (remplaza_vocales ("hola"))

#2.5

def da_vuelta_str(s:str):
    i = len(s) - 1
    l = ""
    while i >= 0:
      l+= s[i]
      i-=1
    return l

#print (da_vuelta_str ("no es la nave es el piloto"))  

#2.6

def eliminar_repetidos(s:str):
    l = ""
    for c in s:
        if c not in l:
            l+=c
    return l

#print (eliminar_repetidos ("hhhhooohhhlllaaa"))

#EJERCICIO 3

def aprobado(list: int)->int:
    k= 0
    i = 0
    res = 0
 
    while i < len(list):
        k+=list[i]
        i+=1 

    promedio = k / len(list) 
    
    for notas in list:
        if notas < 4:
            return 3

    if  promedio < 4:
            res = 3
    elif promedio >= 4 and promedio < 7:
            res= 2
    elif promedio >= 7:
            res = 1
    return res 

#print (aprobado ([7,6]))

#EJERCICIO 4

def nombres_estudiantes() -> list:
    res = []
    listo = False
     
    while not listo:
      nombre = input("Ingrese un nombre: ")
      if nombre == "listo":
          listo = True
      else:
          res.append(nombre)    
    return res

#print(nombres_estudiantes())

#4.2





print (tiene_minuscula("123Ar2565y"))
print (tiene_mayus ("123Ar2565y"))
print (tiene_numero("123Ar2565y"))
