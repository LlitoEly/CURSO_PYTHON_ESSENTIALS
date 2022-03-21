# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 14:07:16 2022

@author: USUARIO
"""

lista=["R1",4
       ,58.5,
       True,
       False,
       "R2",
       "S1",
       "S1"]
print(type(lista))
print(len(lista))
print(lista)
print("\n"*2)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print(lista[5])
print(lista[6])
print(lista[7])
print(lista[-8])
print(lista[-6])

tupla=("R1",
       4
       ,58.5,
       True,
       False,
       "R2",
       "S1",
       "S1")
print (tupla[-8])
lista[4]="R3"
#tupla[4]="R3"
del lista[3]
del tupla


