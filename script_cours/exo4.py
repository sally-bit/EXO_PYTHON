#coding:utf-8
"""
    Initialisez deux entiers : a = 0 et b = 10.
    Écrire une boucle affichant et incrémentant la valeur de a tant qu’elle reste inférieure
    à celle de b.
    Écrire une autre boucle décrémentant la valeur de b et affichant sa valeur si elle est
    impaire. Boucler tant que b n’est pas nul.
"""

a = 0 
b = 10

print("#################################### incrementation ###############################################")

while a<b:
    print("la valeur =>",a)
    a+=1

print("#################################### decrementation ###############################################")

while b != 0:
    if b % 2 != 0:
         print("la valeur =>",b)
    b-=1    