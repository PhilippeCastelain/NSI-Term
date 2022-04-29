# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:49:21 2022

@author: pcastelain
"""

def puissance(x,n): # itératif
    res = 1
    for i in range(n):
        res = res * x
    return res

def puissanceRec(x,n): # récursif
    if n == 0:
        return 1
    else:
        return x * puissanceRec(x,n-1)