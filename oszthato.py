import math
import random

def szamsorozat():
    lista=[]
    for i in range(0, 50, 1):
        szam:int=random.randint(1, 100)
        lista.append(szam)
    return lista

def hettelOszthato(lista):
    szamlalo=0
    for i in range(0, len(lista),1):
        if lista[i]%7==0:
            szamlalo+=1
    return szamlalo