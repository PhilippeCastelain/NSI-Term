# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 15:58:40 2022

@author: pcastelain
"""

import csv
reader = csv.DictReader(open('eleves.csv', 'r', encoding='utf8'))
classe = []
for row in reader:
    classe.append(dict(row))
    
    
for e in classe:
    moyenne = (float(e['Programmation'])+float(e['Algorithmique'])
               +float(e['Projet']))/3
    print("moyenne de",e['Prenom'],e['Nom'],'est :'
              ,moyenne)

    
    # moyProg = (float(classe[0]['Programmation'])+float(classe[1]['Programmation'])
    #      +float(classe[2]['Programmation']))/3
    # print('la moyenne de programmation :',moyProg)
print()

for s in ['Programmation','Algorithmique','Projet']:   
    moy = (float(classe[0][s])+float(classe[1][s])+float(classe[2][s]))/3 
    print('moyenne de',s,':',moy)