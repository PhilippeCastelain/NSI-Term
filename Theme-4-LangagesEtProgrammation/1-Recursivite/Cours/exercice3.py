# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 16:18:46 2022

@author: pcastelain
"""
def fact(n):
    res = 1
    if n == 0:
        return 1
    else:
        for i in range(1,n+1):
            res = res * i
        return res
    
def factRec(n):
    if n == 0:
        return 1
    else:
        return n * factRec(n-1)