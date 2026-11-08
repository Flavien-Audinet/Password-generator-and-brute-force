import random
import string

while True:
    menu = input("1: Chiffre\n2: minuscule\n3: MAJUSCULE\n4: Symbole\n5: Tous\n")
    if menu == '1':
        print("\n")
        element = string.digits
        passwd = ""
        choix = input("Choisir la longueur du mdp : ")
        choix = int(choix)
        for i in range(choix): passwd = passwd + element[random.randint(0, len(element) - 1)]
        print(passwd)
        print("\n")

    elif menu == '2':
        print("\n")
        element = string.ascii_lowercase
        passwd = ""
        choix = input("Choisir la longueur du mdp : ")
        choix = int(choix)
        for i in range(choix): passwd = passwd + element[random.randint(0, len(element) - 1)]
        print(passwd)
        print("\n")

    elif menu == '3':
        print("\n")
        element = string.ascii_uppercase
        passwd = ""
        choix = input("Choisir la longueur du mdp : ")
        choix = int(choix)
        for i in range(choix): passwd = passwd + element[random.randint(0, len(element) - 1)]
        print(passwd)
        print("\n")

    elif menu == '4':
        print("\n")
        element = string.punctuation
        passwd = ""
        choix = input("Choisir la longueur du mdp : ")
        choix = int(choix)
        for i in range(choix): passwd = passwd + element[random.randint(0, len(element) - 1)]
        print(passwd)
        print("\n")

    elif menu == '5':
        print("\n")
        element = string.ascii_letters + string.digits + string.punctuation
        passwd = ""
        choix = input("Choisir la longueur du mdp : ")
        choix = int(choix)
        for i in range(choix): passwd = passwd + element[random.randint(0, len(element) - 1)]
        print(passwd)
        print("\n")

    else:
        print("\n")
        print("erreur de saisie")
        print("\n")
