from math import*
#coding:uft-8
"""
Définir deux ensembles (sets) : X = {a,b,c,d} et Y = {s,b,d}, puis affichez les résultats
  suivants :
    – les ensembles initiaux ;
    – le test d’appartenance de l’élément 'c' à X ;
    – le test d’appartenance de l’élément 'a' à Y ;
    – les ensembles X −Y et Y − X ;
    – l’ensemble X ∪Y (union) ;
    – l’ensemble X ∩Y (intersection).
"""

def test_list(n,chose):
    if n in chose :
        print(n," appartient a ",chose)
    else:
        print(n," n'appartient pas a  ",chose)


X = {10,5,2,7} 
Y = {6,5,7}
print("les ensembles initiaux")
print(X)
print(Y)

print("le test d’appartenance de l’élément 'c' à X ")
test_list(2,X)

print("le test d’appartenance de l’élément 'a' à Y ")
test_list(10,Y)

print("les ensembles X − Y")
print(X.difference(Y))


print("les ensembles Y − X")
print(Y.difference(X))

print("l’ensemble X ∪ Y (union)")
print(X.union(Y))

print("l’ensemble X ∩ Y (intersection)")
print(X.intersection(Y))