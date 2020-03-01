#coding:utf-8
#L’ordre lexicographique est celui du dictionnaire.
#Saisir deux mots, comparez-les pour trouver le « plus petit » et affichez le résultat
con_trou=True
mots_1=str(input("saisissez le premier mots : "))
mots_2=str(input("saisissez le premier mots : "))

if mots_1 < mots_2 :
    print("le mots le plus petit est ",mots_1)
else:
    print("le mots le plus petit est ",mots_2)
