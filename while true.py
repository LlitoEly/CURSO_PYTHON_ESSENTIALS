# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 16:55:15 2022

@author: USUARIO
"""

numero=input("Ingrese un número que desee que cuente: ")
numero=int(numero)
contador=1
while True:
    print(contador)
    contador+=1
    if contador>numero:
        break
    