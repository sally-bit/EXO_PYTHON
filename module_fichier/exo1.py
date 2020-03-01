from math import*
#coding:uft-8
"""
  Écrire un module de calcul des racines du trinôme réel : ax2 +bx +c.
    Le module définit une fonction trinome avec les trois paramètres du trinôme, a, b et
    c. La fonction doit retourner un tuple dont le premier élément est le nombre de racines
    du trinôme (0, 1 ou 2), et les autres éléments sont les racines éventuelles.
    Testez votre fonction avec les trois jeux de valeurs suivantes : 1,−3, 2, 1,−2, 1 et 1, 1, 1.
"""

def disc(a,b,c):
    return (b**2)-(4*a*c)

def maFonction(a,b,c):
    d=disc(a,b,c)
    
    if d < 0:
        print("le discriminant de la fontion est negatif alors sa solution est l'ensemble vide")
        s1=(0,0)
        print(s1)
    elif d > 0:
        racine=round(sqrt(d))
        x1=(-b + racine)/(2*a)
        x2=(-b - racine)/(2*a)
        s2=(2,x1,x2)
        print(" voici les solutions => ",s2)
        
      
    else: 
        x0 = -b /(2*a)
        s3=(1,x0)
        print("la solution x0 =>",s3)
        
cont=True

while cont:        
    print("RESOLUTION DE LA FONCTION f (x) = ax2 + bx +c ")
    A=int(input("Entrez le nombre a : "))
    B=int(input("Entrez le nombre b : "))
    C=int(input("Entrez le nombre c : "))
    maFonction(A,B,C)
    choix=input("voulez-vous continuez ? oui ou non : ")
    if choix in "non":
        break
    else:
        continue