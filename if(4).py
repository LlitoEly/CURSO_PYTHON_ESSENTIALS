# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 17:04:34 2022

@author: USUARIO
"""
nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))
if edad>=1 and edad<=10:
    print(nombre, "Eres un niño")
elif edad>=11 and edad<=17:
    print(nombre, "Eres adolecente")
elif edad>=18 and edad<= 55:
    print(nombre, "Eres un Adulto")
elif edad>=55 and edad<=60:
    print(nombre, "Eres tercera edad")
else:
    print(nombre, "Eres ABUELITO")


