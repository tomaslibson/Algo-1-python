#EJERCICIO 1

def ultima_aparcion(s: list[int] , e: int) -> int:
    res = []
    i = 0

    while i < len(s):
        if s[i] == e:
            res.append(i)
        
        i+=1
    return res[len(res)-1]

l = [-1,4,0,4,100,0,100,0,-1,-1]
x = 0

# print(ultima_aparcion(l, x))

def elementos_exclusivos(s:list[int], t: list[int]) -> list[int]:
    l = []
    res = []
    i = 0
    k = 0

    for x in s:
        if x in t:
            l.append(x)
    while i < len(s):
        if s[i] not in l:
            res.append(s[i])

        i+=1
    while k < len(t):
        if t[k] not in l:
            res.append(t[k])

        k+=1
    return eliminar_repetidos(res)

def eliminar_repetidos(l:list):
    i = 0
    res = []
    
    for n in l:
        if n not in res:
            res.append(n)
    return res

s = [-1,4,0,4,3,0,100,0,-1,-1]
t = [0,100,5,0,100,-1,5]

# print(elementos_exclusivos(s,t))

###EJERCICIO 3


def contar_traducciones_iguales(ing: dict[(str,str)], ale: dict[str,str]) -> int:
    keysingles = list(ing.keys()) 
    keysaleman = list(ale.keys())
    
    res = 0
    i = 0

    while i < len(keysingles):
        w = keysingles[i]
        for k in keysaleman:
            if k == w and ing[w] == ale[k]:
                res+=1
            
        i+=1
    return res

aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
ingles = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}

# print(list(aleman.keys()))
# print(aleman["Mano"])

# print(contar_traducciones_iguales(ingles,aleman))

###EJERCICIO 4

def convertir_a_diccionario(lista: list[int]) -> dict[(int,int)]:
    res = {}

    i = 0

    while i < len(lista):
        e = lista[i]
        if e in res.keys():
            res[e]+=1
        else:
            res[e] = 1

        i+=1
    return res


s = [-1,0,4,100,100,-1,-1]
u = [1,2,3,4,33,3,3,2,2,1,1,33]
# print(convertir_a_diccionario(s))
# print(convertir_a_diccionario(u))