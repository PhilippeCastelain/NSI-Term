# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:09:19 2022

@author: pcastelain
"""

class Eleve:
    matiere1 = "Programmation" 
    matiere2 = "Algorithmique" 
    matiere3 = "Projet"
    def __init__(self,Nom, Prenom, Date, Note1, Note2, Note3):
        self.nom = Nom 
        self.prenom=Prenom 
        self.date=Date 
        self.note_mat1=Note1 
        self.note_mat2=Note2 
        self.note_mat3=Note3
        
    def moyenne(self):
        return (self.note_mat1 + self.note_mat2 + self.note_mat3)/3
    
camilleO = Eleve('Onette','Camille','01/07/2004',7,14,11)
modesteO = Eleve('Oma','Modeste','01/11/2002',13,8,17)

for eleve in [camilleO,modesteO]:
    print('Résultat de',eleve.prenom,eleve.nom)
    print(eleve.matiere1,':',eleve.note_mat1)
    print(eleve.matiere2,eleve.note_mat2)
    print(eleve.matiere3,eleve.note_mat3)
    print('moyenne :',eleve.moyenne())
    print()
    
