#coding:utf-8
"""
On désire sécuriser une enceinte pressurisée.
On se fixe une pression seuil et un volume seuil : pSeuil = 2.3, vSeuil = 7.41.
On demande de saisir la pression et le volume courant de l’enceinte et d’écrire un script
qui simule le comportement suivant :
– si le volume et la pression sont supérieurs aux seuils : arrêt immédiat ;
– si seule la pression est supérieure à la pression seuil : demander d’augmenter 
    le volume de l’enceinte ;
– si seul le volume est supérieur au volume seuil : demander de diminuer le volume
de l’enceinte ;
– sinon déclarer que « tout va bien ».
"""

pSeuil = 2.3 
vSeuil = 7.41

epSeuil = float(input("saisissez la pression : "))
evSeuil = float(input("saisissez le volume : "))

if epSeuil > pSeuil and evSeuil > vSeuil:
    print("arrêt immédiat")
elif epSeuil > pSeuil :
    print(" demander d’augmenter le volume de l’enceinte") 
    
elif evSeuil > vSeuil:
    print("demander de diminuer le volume de l’enceinte")
else:
    print("tout va bien")

