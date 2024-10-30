+++
title = "La boucle while"
weight = 3
+++


La boucle `while` permet de **répéter** l'exécution d'un bloc de code **tant qu'une** condition donnée est **vraie**. C'est une structure de contrôle utilisée **lorsque le nombre d'itérations n'est pas connu à l'avance**.

## Syntaxe de la boucle while

La syntaxe de base de la boucle `while` est la suivante :

```python
while condition:
    # bloc de code à répéter
```

Le bloc de code à l'intérieur de la boucle `while` sera exécuté tant que la condition est vraie. 
```python
compteur = 0
while compteur < 5:
    print("Compteur :", compteur)
    compteur += 1
```

Dans cet exemple, la boucle s'exécute tant que la variable `compteur` est inférieure à 5. À chaque itération, `compteur` est incrémenté de 1.

## L'Instruction break

L'instruction `break` permet de sortir immédiatement de la boucle, même si la condition de la boucle est toujours vraie. Elle est souvent utilisée pour arrêter la boucle en fonction d'une condition interne. Voici un exemple :

```python
compteur = 0
while True:
    print("Compteur :", compteur)
    compteur += 1
    if compteur == 5:
        break
```

Dans cet exemple, la boucle est théoriquement infinie (`while True`), mais elle s'arrête lorsque `compteur` atteint 5 grâce à l'instruction `break`.

## L'instruction continue

L'instruction `continue` permet de passer immédiatement à l'itération suivante de la boucle, en sautant le reste du code à l'intérieur de la boucle pour l'itération en cours. Voici un exemple :

```python
compteur = 0
while compteur < 10:
    compteur += 1
    if compteur % 2 == 0:
        continue
    print("Compteur impair :", compteur)
```

Dans cet exemple, la boucle incrémente `compteur` de 1 à chaque itération. Si `compteur` est un nombre pair, l'instruction `continue` fait passer immédiatement à l'itération suivante, de sorte que seuls les nombres impairs sont imprimés.

## Boucles infinies

Il est important de faire attention aux boucles infinies, qui se produisent **lorsque la condition de la boucle ne devient jamais fausse**. Cela peut entraîner un programme qui ne se termine jamais. 

Par exemple :

```python
compteur = 0
while compteur < 5:
    print("Compteur :", compteur)
    # Oubli d'incrémenter compteur
```

Dans cet exemple, la boucle ne s'arrêtera jamais car `compteur` n'est jamais incrémenté, et la condition `compteur < 5` reste toujours vraie.

