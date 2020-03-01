#coding:utf-8
"""
Utilisez l’instruction break pour interrompre une boucle for d’affichage des entiers
   de 1 à 10 compris, lorsque la variable de boucle vaut 5
"""
i=1
for element in range(1,11):
    if element == 5:
        break
    print("element",i," est => ",element)
    i+=1

    