from math import *
#coding:uft-8
"""
Écrire une fonction volMasseEllipsoide qui retourne le l'exentricité, le volume et la masse
d’un ellipsoïde.
   Les paramètres sont les trois demi-axes. 
   On donnera à ces quatre paramètres des valeurs par défaut telle que rho = 11.2 .
   On donne : v =(4/3)πabc
   Tester cette fonction par des appels avec différents nombres d’arguments.={{{\sqrt  {a^{2}-c^{2}}}} \over a}.
"""

def exen(a,c):
    rac=(a**2)-(c**2)
    resultat=(sqrt(rac)/a)
    return resultat

def volume(a,b,c):
    rst=(4/3)*pi*a*b*c
    return rst

def masse(a,b,c,p):
    masse=p*volume(a,b,c)
    return masse

def volMasseEllipsoide(a=11.5,b=11.4,c=10.5,p=5.5):
    print("l'exentricité de cet ellipsoïde : e => ",exen(a,c))
    print("le volume de cet ellipsoïde : V => ",volume(a,b,c))
    print("la masse de cet ellipsoïde : M => ",masse(a,b,c,p))
    
A=float(input("Entrez le parametre a : "))
B=float(input("Entrez le parametre b : "))
C=float(input("Entrez le parametre c : "))
P=float(input("Entrez le parametre de la densite p : "))

volMasseEllipsoide(A,B,C,P)




