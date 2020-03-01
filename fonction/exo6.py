from math import*
#coding:uft-8
"""
Écrire une autre fonction somme avec trois arguments, et qui renvoie leur somme
"""

def somme_arg(a,b,c):
    tpl=(a,b,c)
    print("la somme de ces trois argument est =>",sum(tpl))

    
A=int(input("Entrez le nombre a : "))
B=int(input("Entrez le nombre b : "))
C=int(input("Entrez le nombre c : "))

somme_arg(A,B,C)
