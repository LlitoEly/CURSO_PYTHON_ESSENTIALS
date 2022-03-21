# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 16:25:51 2022

@author: USUARIO
"""
switch=[]
lista=["R1","R2","R3","R4","R5","S1","S2","S3"]
for item in lista:
    if "R" in item:
        switch.append(item)
print(switch)