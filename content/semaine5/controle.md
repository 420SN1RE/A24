+++
title = "Le contrôle des boucles"
weight = 54
+++

![Contrôle des boucles](../controle-boucles.jpeg?width=20vw)

## Les instructions BREAK et CONTINUE

Les instructions `break` et `continue` sont utilisées pour contrôler le flux des boucles.

### L'instruction BREAK

L'instruction `break` permet de sortir immédiatement d'une boucle, même si la condition de la boucle n'est pas encore remplie.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```
Dans cet exemple, la boucle s'arrête lorsque `i` vaut 5, donc les nombres de 0 à 4 sont imprimés.

### L'instruction CONTINUE

L'instruction `continue` permet de passer immédiatement à l'itération suivante de la boucle, en sautant le reste du code à l'intérieur de la boucle pour l'itération en cours.

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```
Dans cet exemple, seuls les nombres impairs de 0 à 9 sont imprimés, car `continue` saute les itérations où `i` est pair.

## l'instruction ELSE avec les boucles

En Python, les boucles `for` et `while` peuvent avoir une clause `else`. 
Le bloc `else` est exécuté lorsque la boucle se termine normalement (c'est-à-dire sans rencontrer une instruction `break`).

**Fonctionnement et exemples :**

```python
for i in range(5):
    print(i)
else:
    print("La boucle s'est terminée normalement.")
```
Dans cet exemple, le message "La boucle s'est terminée normalement." est affiché après que la boucle `for` ait terminé toutes ses itérations.

Un autre exemple avec une condition de sortie :

```python
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("La boucle s'est terminée normalement.")
```
Dans cet exemple, le message `else` n'est pas affiché car la boucle est interrompue par l'instruction `break` lorsque `i` vaut 3.

## Atelier

[Instructions break et continue](../atelier-controle.ipynb)