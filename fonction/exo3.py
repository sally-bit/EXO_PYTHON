from math import *
#coding:uft-8
"""
Écrire une fonction maFonction, une fonction qui premet de resoudre une equation de type
   f (x) = ax2 + bx +c.
   seul la partie entiere des solution doit etre affichée
"""

def disc(a,b,c):
    return (b**2)-(4*a*c)

def maFonction(a,b,c):
    d=disc(a,b,c)
    racine=round(sqrt(d))
    if d < 0:
        print("le discriminant de la fontion est negatif alors sa solution est l'ensemble vide")
    elif d > 0:
        print("le discriminant de la fontion est positif alors ces solutions sont x1 et x2")
        x1=(-b + racine)/(2*a)
        x2=(-b - racine)/(2*a)
        print(" la solution x1 => ",((-b + racine)),"/",2*a)
        print(" la solution x2 => ",((-b - racine)),"/",2*a)
        
    else:
        print("le discriminant de la fontion est egal a zero donc sa solution est x0")
        x0 = -b /(2*a)
        print("la solution x0 =>",x0)
        
print("RESOLUTION DE LA FONCTION f (x) = ax2 + bx +c ")
A=int(input("Entrez le nombre a : "))
B=int(input("Entrez le nombre b : "))
C=int(input("Entrez le nombre c : "))

maFonction(A,B,C)
