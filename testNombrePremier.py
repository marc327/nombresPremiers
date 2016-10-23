#!/usr/bin/python3.5
# -*-coding:utf-8 -*


import os # On importe le module os qui dispose de variables 
          # et de fonctions utiles pour dialoguer avec votre 
          # système d'exploitation
import package.functions
import time

start_time = time.time()

#tableau de nombres premiers
#lecture du tableau des nombres premies
tableauNombres = package.functions.lireMonFichier("stockageNombres/nombresPremiers_2_999983.txt")
#print (tableauNombres)


#boucle sur un groupe d'éléments
i = 100000000000001 #1000000001	# doit être un nombre impair
while i < 100000000000101 : #1000000182 :
    if package.functions.isPremier(i, tableauNombres) == True :
        print(i)
    i += 2
interval = time.time() - start_time
print('temps en secondes: ', interval)
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
