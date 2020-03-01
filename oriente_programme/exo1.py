from math import*
#coding:uft-8
"""
Définir une classe MaClasse possédant les attributs suivants :
   données : deux attributs de classes : x = 23 et y = x + 5.
   méthode : une méthode affiche contenant un attribut d’instance z = 42 et les affichages de y et de z.
   Dans le programme principal, instanciez un objet de la classe MaClasse et invoquez la
   méthode affiche.
"""

class MaClasse:
    def __init__(self):
        self.x=23
        self.y= self.x + 5
    def affiche(self):
        self.z=42
        print("l'affiches de y {}".format(self.y))
        print("l'affiches de z {}".format(self.z))



objet=MaClasse()
objet.affiche()