import math

#EJERCICIO 1

#1.1

def pertenece(s: list , e:int)->bool:
    res = (e in s)
    return res

#print (pertenece ([1,2,4,5], 7))

#1.2

def  divide_a_todos (s: list , e: int)-> bool:
    i: int = 0
    res: bool = True
    while (i < len(s)) and (res == True):
         if (s[i] % e != 0):
          res = False
    i+=1
    return res
    

divide_a_todos ([6,7,10,8], 2)

