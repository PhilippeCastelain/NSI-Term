# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:51:53 2022

@author: pcastelain
"""

def creer_eleve(nom,prenom,date,note1,note2,note3):
    eleve = {'Nom':nom,'Prenom':prenom,'Date':date,'Prog':note1,
             'Algo':note2,'Projet':note3}
    return eleve

def creer_classe3(el1,el2,el3):
    return [el1,el2,el3]

def moyenne_eleve(eleve):
    return (eleve['Prog'] + eleve['Algo'] + eleve['Projet'])/3

def moyenne_matiere(classe):
    moyProg = (classe[0]['Prog'] + classe[1]['Prog'] + classe[2]['Prog'])/3
    moyAlgo = (classe[0]['Algo'] + classe[1]['Algo'] + classe[2]['Algo'])/3
    moyProjet = (classe[0]['Projet'] + classe[1]['Projet'] + classe[2]['Projet'])/3
    return moyProg, moyAlgo, moyProjet
    