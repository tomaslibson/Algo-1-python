import math
from queue import LifoQueue as Pila
import random
from queue import Queue as Cola

def quien_gano_el_tateti_facilito(tablero: list[list[str]]) -> int:
    n = len(tablero)
    hay_tres_x: bool = False             #seteo ambos en falso como caso base
    hay_tres_o: bool = False
    res: int = 0                                       # este resultado termina variando o quedando igual

    for columna in range(n):
        contadorX: int = 0
        contadorO: int = 0

        for fila in range(n):
            if tablero[fila][columna] == 'x':
                contadorX += 1
                contadorO = 0       #reinicio a cero cada que no sea el elemento seguido esperado
            elif tablero[fila][columna] == 'o':
                contadorX = 0
                contadorO += 1
            else:
                contadorX = 0
                contadorO = 0

            if contadorX == 3:          # dentro del for de la fila analizo si aparece tres veces consecutivas
                hay_tres_x = True       # si aparece = True
            elif contadorO == 3:
                hay_tres_o = True

    if hay_tres_x and hay_tres_o:
        res = 3
    elif hay_tres_x:
        res = 1
    elif hay_tres_o:
        res = 2
    else:
        res = 0

    return res