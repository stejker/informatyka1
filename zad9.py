# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:23:21 2020

@author: Adam Sawicki
"""
d=0
for a in range(-100,100):
    c=((a-1)^2)-(4*((-a)^3)*((a^2)+1))
    if c>=0:
        d +=1
print("liczba wyników rzeczywistych:",d)
