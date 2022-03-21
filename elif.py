# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 14:51:00 2022

@author: USUARIO
"""

acl=int(input("Ingrese el número de ACL: "))
if acl>=1 and acl<=99:
    print("La ACL es Standar")
elif acl>=100 and acl<=199:
    print("La ACL es Extendida")
else:
    print("El número ingresado no es de ACL normal")