import sys

if len(sys.argv) != 2:
    print("Pas le bon nombre d'arguments")
    sys.exit(1)
print(f'Bonjour {sys.argv[1]}')
