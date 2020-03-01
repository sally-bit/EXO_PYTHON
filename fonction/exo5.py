from math import*
#coding:uft-8
"""
.Écrire une fonction somme avec un argument « tuple de longueur variable » qui calcule
      la somme des nombres contenus dans le tuple.
      Tester cette fonction par des appels avec différents tuples d’entiers ou de flottants
"""
tuple_list=(3.7,4.6,2.9,4.2,4.1,5.7)

def somme_tuple(tup):
    resu=0
    for element in tup:
        resu += element
    
    print(resu)


somme_tuple(tuple_list)