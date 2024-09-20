# addition_2.py
# Programme utilisant des arguments

import sys

print("Programme:", sys.argv[0])    # Affichera le nom du programme, soit "addition.py"

if len(sys.argv) != 3:
    print("Vous devez fournir 2 arguments pour l'addition")
    sys.exit(1)

if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    print("Vous devez fournir des arguments numériques pour l'addition")
    sys.exit(2)

nombre_1 = int(sys.argv[1])         # "nombre_1" devient la valeur numérique du 1er argument
nombre_2 = int(sys.argv[2])         # "nombre_2" devient la valeur numérique du 2e argument
reponse = nombre_1 + nombre_2

print("Réponse:", reponse)
