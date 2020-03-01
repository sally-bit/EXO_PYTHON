from math import sqrt
#coding:utf-8
continu_saisi=True

while continu_saisi:
    num_float=float(input(" saisisez votre nombre decimal : "))
    if num_float>=0:
        print("la racine de la valeur saisir est {:.2f}".format(sqrt(num_float)))
        continu_saisi=False
    else:
        print("le nombre que vous avez saisir est negatif")
        continu_saisi=True
