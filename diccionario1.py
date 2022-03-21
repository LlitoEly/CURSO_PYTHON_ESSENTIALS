# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 16:07:08 2022

@author: USUARIO
"""

dict1={"R1":"10.10.10.1",
       5:"CodigoEMP",
       False:"Estado Civil",
       "R2":"10.10.10.2",
       "R3":"10.10.10.3","R1":"10.10.10.10.4"
       }
print(dict1)
print(dict1[5])
print(dict1[False])
print(dict1["R1"])
dict1["S1"]="10.10.11.1"
dict1[1]="ESTADO"
print("S2" in dict1)