#!/usr/bin/python3.5
# -*-coding:utf-8 -*


import os # On importe le module os qui dispose de variables 
          # et de fonctions utiles pour dialoguer avec votre 
          # système d'exploitation
import package.functions
import time

start_time = time.time()

#boucle sur un groupe d'éléments
mesNombresPremiers = [2]
i = 3	# doit être un nombre impair
while i < 100001 :
    if package.functions.isPremierStockage(i, mesNombresPremiers) == True :
        mesNombresPremiers.append(i)
    i += 2
#print("mesNombresPremiers: " + str(mesNombresPremiers))

# stocker les nombres premiers dans un fichier
str_mesNombresPremiers = package.functions.toString(mesNombresPremiers)
fichier = open("nombresPremiers_2_test.txt", "w") 
fichier.write(str_mesNombresPremiers)        #Écrit la valeur de la variable a dans le fichier
fichier.close()
interval = time.time() - start_time
print('temps en secondes: ', interval)
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
