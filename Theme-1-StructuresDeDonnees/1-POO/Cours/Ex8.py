# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 17:11:40 2022

@author: pcastelain
"""

class Robot:
    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.direction = direction
        
    def avancer(self):
        if self.direction == 'E':
            self.x = self.x + 1
        if self.direction == 'O':
            self.x = self.x - 1
        if self.direction == 'N':
            self.y = self.y + 1
        if self.direction == 'S':
            self.y = self.y - 1
            