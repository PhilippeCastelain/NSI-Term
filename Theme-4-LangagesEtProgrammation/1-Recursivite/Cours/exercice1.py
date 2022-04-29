# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:39:38 2022

@author: pcastelain
"""

def maximum(a,b):
    if a > b:
        return a
    else:
        return b
    
def maxiRec(L):
    if len(L) == 1:
        return L[0]
    else:
        return maximum(L[0],maxiRec(L[1:]))