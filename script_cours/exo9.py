#coding:utf-8
"""
Utilisez l’instruction continue pour modifier une boucle for d’affichage de tous entiers
    de 1 à 10 compris,
   sauf lorsque la variable de boucle vaut 5
"""
i=1
for element in range(1,11):
    if element == 5:
        continue
    print("element",i," est => ",element)
    i+=1
