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
    for char in c:
        if("a" <= char <="z"):
           res=True
        else: 
            res=False
    return res
      
def tiene_mayus(c: str) -> bool:
    for char in c:
        if("A" <= char <="Z"):
           res=True
        else:
            res=False
    return res

def tiene_numero(c: str) -> bool:
    for num in c:
        if ("0" <= num <="9"):
            res=True
        else:
            res=False
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


print (tiene_minuscula("123Ar2565y"))
print (tiene_mayus ("123Ar2565y"))
print (tiene_numero("123Ar2565y"))