from math import*
#coding:uft-8
"""
définir la liste : liste =[17, 38, 10, 25, 72], puis effectuez les actions suivantes :
      – triez et affichez la liste ;
      – ajoutez l’élément 12 à la liste et affichez la liste ;
      – renversez et affichez la liste ;
      – affichez l’indice de l’élément 17 ;
      – enlevez l’élément 38 et affichez la liste ;
      – affichez la sous-liste du 2eau 3eélément ;
      – affichez la sous-liste du début au 2eélément ;
      – affichez la sous-liste du 3eélément à la fin de la liste ;
      – affichez la sous-liste complète de la liste ;
      – affichez le dernier élément en utilisant un indiçage négatif.
"""

liste =[17, 38, 10, 25, 72]
liste.sort()
print("TRIE LA LISTE")
print(liste)

liste.append(12)
print("AJOUTE DE 12 A LA LISTE")
print(liste)

liste.reverse()
print("RENVERSE DE LA LISTE")
print(liste)


print("AFFICHAGE DE L'INDICE DE L'ELEMENT 17")
print(liste.index(17))


liste.remove(38)
print("ENLEVEZ L'ELEMENT 38 DE L'AFFICHE")
print(liste)


print("la sous-liste du 2eau 3eélément")
print(liste[1:3])




print("affichez la sous-liste du début au 2eélément")
print(liste[:2])


print(" affichez la sous-liste du 3eélément à la fin de la liste ")
print(liste[2:])




print("affichez la sous-liste complète de la liste ")
print(liste[0:])


print("affichez le dernier élément en utilisant un indiçage négatif ")
print(liste[-1])
