from math import*
#coding:uft-8
"""
Initialisez truc comme une liste vide, et machin comme une liste de cinq flottants nuls.
    Affichez ces listes.
    Utilisez la fonction range() pour afficher :
    – les entiers de 0 à 3 ;
    – les entiers de 4 à 7 ;
    – les entiers de 2 à 8 par pas de 2.
    Définir chose comme une liste des entiers de 0 à 5 et testez l’appartenance des éléments 3 et 6 à chose.
"""

truc = list()
machin =[0.0,0.0,0.0,0.0,0.0]
print(truc)
print(machin)

print("les entiers de 0 à 3 ")
for elt in range(0,4):
    print(elt)



print("les entiers de 4 à 7 ")
ent2=range(4,8)
for elt in ent2:
    print(elt)


print("les entiers de 2 à 8 ")
ent3=range(2,9,2)
for elt in ent3:
    print(elt)

chose=list(range(0,6))
print(chose)

def test_list(n):
    if n in chose :
        print(n," appartient a la liste chose")
    else:
        print(n," n'appartient pas a la liste chose")

test_list(3)
test_list(6)
        

    
