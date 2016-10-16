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

"""fonction contrôle de la primalité"""
def isPremier(monNombre):
    i = 2
    while i < ((monNombre+1)//2):
        if monNombre % i == 0:
            return False
        i += 1
    return True

