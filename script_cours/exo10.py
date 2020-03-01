#coding:utf-8
"""
demander a un utilisateur de saisr un nombre.
     essayez de soumettre une chaine de caractère .
     Vous avez une erreur ?
     A l'aide d'une exception gérez cette erreur
"""
cont=True
while cont:
    saisi_user=input("saisissez un nombre entier : ")

    try:
        saisi_user=int(saisi_user)
        print("saisir enregistre")
        cont=False
    except:
        print("veulliez saisir un nombre entier pas chaine caractere ")
        cont=True


    