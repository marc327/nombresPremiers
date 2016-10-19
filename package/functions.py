#!/usr/bin/python3.5
# -*-coding:utf-8 -*


"""module multipli contenant la fonction table"""

def table(nb, max=10):
    """Fonction affichant la table de multiplication par nb de
    1 * nb jusqu'à max * nb"""
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1


"""fonction de lecture du fichier contenant les nombres premiers stockés"""
def lireMonFichier(nomFichier):
    f = open(nomFichier, 'r')
    #print (f.read())
    numéroLigne = 0
    liste = []
    for line in f:
#       print (line)
        liste.append(int(line[0:-1]))
        numéroLigne += 1
    f.closed
    return liste


"""fonction contrôle de la primalité"""
def isPremier(monNombre, tableauNombres):
    j = 0 # 1 ou 0?
    i = tableauNombres[j]
    #je prend chacune des valeurs de mon tableau pour vérifier la primalité
    while i < ((monNombre+1)//(tableauNombres[len(tableauNombres)-1])):	# définir la limite jusqu'à laquelle il est nécessaire de rechercher la division entière
        if monNombre % i == 0:		# 
            return False
        j += 1
        if j <= len(tableauNombres):
            i = tableauNombres[j-1]	#la première case est en 0, donc la dernière en len()-1. Len donne le nombre de données dans le tableau
        else:
            i += 2				# utiiser un dénominateur premier: en utilisant mon tableau, puis quand mon tableau complètement utilisé, utiliser le +2
    return True

