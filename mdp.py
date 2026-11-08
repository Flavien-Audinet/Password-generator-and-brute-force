#!/usr/bin/env python3
"""mdp.py — générer des mots de passe solides et estimer la robustesse d'un mot de passe.

  python3 mdp.py generer                 # 1 mot de passe de 20 caractères, tous les types
  python3 mdp.py generer -l 32 -n 5      # 5 mots de passe de 32 caractères
  python3 mdp.py generer --sans-symboles # lettres + chiffres seulement
  python3 mdp.py analyser                # demande un mot de passe (saisie masquée) et l'évalue

La génération utilise le module `secrets` (aléa cryptographique du système), pas `random`,
dont la suite est prévisible et ne doit jamais servir à fabriquer des secrets.
L'analyse est faite localement : le mot de passe n'est ni affiché, ni enregistré, ni envoyé.
"""
from __future__ import annotations

import argparse
import getpass
import math
import secrets
import string

# Vitesse d'essai d'un attaquant hors ligne (empreinte rapide type MD5/NTLM sur plusieurs GPU).
ESSAIS_PAR_SECONDE = 1e11


def generer(longueur: int, minuscules=True, majuscules=True, chiffres=True, symboles=True) -> str:
    familles = [f for f, ok in ((string.ascii_lowercase, minuscules), (string.ascii_uppercase, majuscules),
                                (string.digits, chiffres), (string.punctuation, symboles)) if ok]
    if not familles:
        raise ValueError("choisis au moins un type de caractères")
    if longueur < len(familles):
        raise ValueError(f"longueur minimale : {len(familles)}")
    alphabet = "".join(familles)
    while True:  # on redessine jusqu'à avoir au moins un caractère de chaque famille demandée
        mdp = "".join(secrets.choice(alphabet) for _ in range(longueur))
        if all(any(c in f for c in mdp) for f in familles):
            return mdp


def entropie(mdp: str) -> float:
    """Entropie en bits, estimée d'après la taille de l'alphabet utilisé (borne haute)."""
    taille = sum(len(f) for f in (string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation)
                 if any(c in f for c in mdp))
    taille += 1 if any(c not in string.printable for c in mdp) else 0
    return len(mdp) * math.log2(taille) if taille else 0.0


def duree_lisible(secondes: float) -> str:
    for unite, s in (("milliards d'années", 3.15e16), ("millions d'années", 3.15e13), ("ans", 3.15e7),
                     ("jours", 86400), ("heures", 3600), ("minutes", 60), ("secondes", 1)):
        if secondes >= s:
            return f"{secondes / s:,.0f} {unite}".replace(",", " ")
    return "moins d'une seconde"


def analyser(mdp: str) -> None:
    bits = entropie(mdp)
    temps = 2 ** bits / 2 / ESSAIS_PAR_SECONDE  # en moyenne, la moitié de l'espace est parcourue
    niveau = "très faible" if bits < 40 else "faible" if bits < 60 else "correct" if bits < 80 else "fort"
    print(f"Longueur : {len(mdp)} caractères")
    print(f"Entropie estimée : {bits:.0f} bits ({niveau})")
    print(f"Force brute hors ligne (~{ESSAIS_PAR_SECONDE:.0e} essais/s) : {duree_lisible(temps)} en moyenne")
    if bits >= 60:
        print("Attention : un mot du dictionnaire ou un motif connu se casse bien plus vite que cette estimation.")


def main() -> None:
    p = argparse.ArgumentParser(description="Générer et évaluer des mots de passe.")
    sub = p.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("generer", help="générer des mots de passe")
    g.add_argument("-l", "--longueur", type=int, default=20)
    g.add_argument("-n", "--nombre", type=int, default=1)
    g.add_argument("--sans-symboles", action="store_true")
    g.add_argument("--chiffres-seulement", action="store_true")
    sub.add_parser("analyser", help="évaluer un mot de passe (saisie masquée)")
    a = p.parse_args()

    if a.cmd == "generer":
        options = dict(minuscules=not a.chiffres_seulement, majuscules=not a.chiffres_seulement,
                       chiffres=True, symboles=not (a.sans_symboles or a.chiffres_seulement))
        for _ in range(a.nombre):
            mdp = generer(a.longueur, **options)
            print(f"{mdp}    ({entropie(mdp):.0f} bits)")
    else:
        analyser(getpass.getpass("Mot de passe à évaluer (non affiché) : "))


if __name__ == "__main__":
    main()
