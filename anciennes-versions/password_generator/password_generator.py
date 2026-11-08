from random import randint
import json
import string

import os; path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "password.json")
with open(path, "r") as f:
    password = json.load(f)

libs = [string.digits,
    string.ascii_lowercase,
    string.ascii_uppercase,
    string.punctuation,
    string.ascii_letters + string.digits + string.punctuation]
choice = ["1", "2"]

while True:
    user = input("Choice beetween\n1: All Characters\n2: Numbers and Alphabetic\n> ")

    if user == "1":
        password.append(randint(len(libs[0:-1])))

    elif user == "2":
        password.append(randint(len(libs[0:2])))

    else:
        continue

with open(path, "w") as f:
    json.dump(password, f)

print(f)
