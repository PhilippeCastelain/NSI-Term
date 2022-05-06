# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 16:39:07 2022

@author: pcastelain
"""

from random import randint

class Personnage:
    def __init__(self,nom,ptVie):
        self.nom = nom
        self.ptvie = ptVie
        
    def combat(self,other):
        other.ptvie = other.ptvie - randint(0,5)
        self.ptvie = self.ptvie - randint(0,5)
        
        