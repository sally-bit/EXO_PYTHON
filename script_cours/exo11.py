from math import sin
#coding:utf-8
"""
Utilisez une exception pour calculer, dans une boucle évoluant de -3 à 3 compris, la
    valeur de sin(x)/x
"""
i=1
for element in range(-3,4):
    try:
        resultat=(sin(element))/element
        print("le resultat de sin(",element,")/",element," est => {:.2f}".format(resultat))

    except:
        print("")
        







