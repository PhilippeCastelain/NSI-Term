# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 15:49:57 2022

@author: pcastelain
"""

class Domino:
    def __init__(self,faceA,faceB):
        self.faceA = faceA
        self.faceB = faceB
        
    def affichePoints(self):
        print("face A :",self.faceA)
        print("face B :",self.faceB)
        
    def total(self):
        return self.faceA + self.faceB