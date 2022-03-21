# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 18:48:32 2022

@author: USUARIO
"""

def validarNumero(prompt, min, max):
    while (True):
        try:
            print("Ingrese un valor entre ",min," y ",max)
            x = int(input(prompt))
            assert x >= min and x <= max
            return x
        
        except ValueError:
            print("Ingresar solo numeros")
        except:
            print("Error, el valor debe estar dentro del RANGO ")
    
v = validarNumero("Ingrese un valor en el rango:", -10, 10)

print("El número es:", v)