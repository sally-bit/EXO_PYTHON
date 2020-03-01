#coding:utf-8

"""
 Écrire une saisie filtrée d’un entier dans l’intervalle 1 à 10, bornes comprises. Affichez
    la saisie.
"""
cont=True
while cont:
    saisi_nb= int(input("saisir un nombre comprise en 1 et 10 : "))
    if saisi_nb > 0 and saisi_nb <=10:
        print("le nombre que vous avez saisir =>",saisi_nb)
        cont=False
    else:
        print("refaire la saisir")
        cont=True
    