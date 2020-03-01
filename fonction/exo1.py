from math import *
#coding:uft-8
"""
Écrire une procédure table avec quatre paramètres : base, debut, fin et inc.
Cette procédure doit afficher la table des base, de debut à fin, de inc en inc.
Tester la procédure par un appel dans le programme principal
"""
def table(base,debut,fin,inc):
    while debut <= fin:
        print(base," x ",debut," => ",base*debut)
        debut += inc

print("OBTENIR LA TABLE DE MUTPLICATION QUE VOUS VOULEZ ")
cont=True       
while cont:
    b=input(" saisir la base de la multiplication : ")
    d=input(" saisir le debut de la multiplication : ")
    f=input(" saisir la fin de la multiplication : ")
    i=input(" saisir incrementation de la multiplication : ")
    try:
        b=int(b)
        d=int(d)
        f=int(f)
        i=int(i)
        table(b,d,f,i)
        cont=False
    except:
        print("saisir des nombres entiers pas de chaine de caracteres")
        cont=True
