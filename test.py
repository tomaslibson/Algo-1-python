
cd = {"YPF" : [(1,10),(15, 3), (31,100)], "ALUA" : [(1,0), (20, 50), (31,30)]}
l = list(cd.values())


def desarmar_tuplas(s: list[(int, float)]) -> list[float]:
    res = []
    i = 0

    for  l in s:
        k = 0 
        while k < len(l):
            v = l[k][1]
            res.append(v)
            k+=1
        i+=1
    return res                

print(desarmar_tuplas(l))            

w = desarmar_tuplas(l) + [[1]]

print(w)

