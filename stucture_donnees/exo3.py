from math import*
#coding:uft-8
"""
Utilisez une liste en compréhension pour obtenir la liste ['ad', 'ae', 'bd', 'be',
    'cd', 'ce'] à partir des chaînes "abc" et "de"
"""

chaine1="abc"
chaine2="de"
list_ch=list()


for elt1 in chaine1:
    for elt2 in chaine2:
        resultat= elt1 + elt2
        list_ch.append(resultat)


print(list_ch)