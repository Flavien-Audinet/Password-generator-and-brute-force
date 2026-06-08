import random
import string

def generator(chars):
    passwd = ""
    choix = input("Choisir la longueur du mdp : ")
    for i in range(int(choix)): passwd = passwd + chars[random.randint(0, len(chars) - 1)]
    return passwd

LIBS = [
    string.digits,
    string.ascii_lowercase,
    string.ascii_uppercase,
    string.punctuation,
    string.ascii_letters + string.digits + string.punctuation]

menu = input("1: Chiffre\n2: Minuscule\n3: MAJUSCULE\n4: Symbole\n5: Tous\n")
if menu.isdigit() and 0 < int(menu) <= len(LIBS):
    password = generator(LIBS[int(menu) - 1])
    print(password)
else:
    print("erreur de saisie")
pause = input("press enter")