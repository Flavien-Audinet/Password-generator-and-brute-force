import random
import time
import string

mot_de_passe = input("entrer un mdp : ")

def mot_aleatoire():
    lettres = string.printable + string.whitespace + string.punctuation
    suiv = ""
    resultat = ""
    for i in range(len(mot_de_passe)):
        while mot_de_passe[i] != suiv:
            print(resultat + suiv)
            suiv = random.choice(lettres)
        resultat += suiv
    return resultat

debut = time.time()
print(mot_aleatoire())
print("Durée : " + str(time.time() - debut) + "secondes")
stop = input("")
