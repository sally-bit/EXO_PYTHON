from math import *
#coding:uft-8
"""
Écrire une fonction cube qui retourne le cube de son argument.
   Écrire une fonction volumeSphere qui calcule le volume d’une sphère de rayon r fourni
   en argument et qui utilise la fonction cube.
   Tester la fonction volumeSphere par un appel dans le programme principal.
"""

def cube(a): 
    return a**3

def volumeSphere(r):
    resultat=(4/3)*pi*cube(r)
    print(" le volume d’une sphère de rayon r est V => {:.2f}  m3".format(resultat))
    

count=True
while count:
    choix=input("Entrez le rayon du sphere pour calculer son volume V : ")
    try:
        choix=float(choix)
        volumeSphere(choix)
        count=False
    except:
        print("veulliez entrez un nombre reel")
        count=True
        