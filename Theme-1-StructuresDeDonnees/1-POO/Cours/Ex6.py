# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 16:20:55 2022

@author: pcastelain
"""

class Rectangle:
    def __init__(self,longueur,largeur):
        self.longueur = longueur
        self.largeur = largeur
        
    def perimetre(self):
        return 2*(self.longueur + self.largeur)
    
    def surface(self):
        return self.longueur * self.largeur