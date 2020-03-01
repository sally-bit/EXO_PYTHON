from math import*
#coding:uft-8
"""
Écrire une fonction compterMots ayant un dictionnaire contenat plusieurs autre dictionnaire et qui
    renvoie la clé:la valeur de chaque dictionnaire 
"""
dictionnaire = {"salut","bonjour","good morning","hello"}
def compteMots(dicte):
    cle=0
    for elt in dicte:
        print("la cle ",cle,": la valeur ",elt)
        cle += 1


compteMots(dictionnaire)