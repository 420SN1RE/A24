+++
title = "La boucle for et la fonction range"
weight = 53
+++

![Boucle for](../boucle-for.jpeg?width=20vw)

## La boucle FOR

{{% notice style=info %}}
La boucle `for` est utilisée pour itérer sur une séquence d'éléments, comme une liste, une chaîne de caractères, ou un tuple.   
Elle s'utilise, lorsque le nombre d'**itérations** (répétitions) est connu d'avance.
{{% /notice %}}

La syntaxe de base est la suivante :

```python
for élément in séquence:
    # bloc de code à exécuter
```

**Exemple simple :**

```python
liste_nombres = [1, 2, 3, 4, 5]
for nombre in liste_nombres:
    print(nombre)
```

Dans cet exemple, chaque élément représenté par la variable `nombre` de la `liste_nombres` est affiché à l'écran.

**Voici comment cela fonctionne**: 
- la boucle `for` commence par prendre le premier élément de la liste et exécute le bloc de code indenté qui suit. 
- Après avoir exécuté le bloc de code pour cet élément, elle passe au suivant, et ainsi de suite, jusqu'à ce qu'elle ait parcouru tous les éléments de la séquence.

**Résultat:**

```plaintext
1
2
3
4
5
```

{{% notice info %}}
Nous étudierons ces types de séquences dans ce cours, en commençant par les listes, dès la semaine prochaine.
{{% /notice %}}

## Utilisation avec des listes et des chaînes de caractères

La boucle `for` est particulièrement utile pour parcourir des listes et des chaînes de caractères.

**Parcourir une liste :**

```python
fruits = ["pomme", "banane", "cerise"]
for fruit in fruits:
    print(fruit)
```

**Parcourir une chaîne de caractères :**

```python
mot = "Python"
for lettre in mot:
    print(lettre)
```

```plaintext
P
y
t
h
o
n
```

## La fonction RANGE()

La fonction `range()` génère une séquence de nombres entiers (pas de flottants), ce qui est très utile pour les boucles `for`.
`range(n)` génèra `n-1` entiers en commençant par 0. Exemple, si n = 3, `range(n)` donnera 0, 1, 2.
Une instruction `for` est toujours de la forme:

```python
for variable-de-contrôle in itérable :
```

{{% notice style=info title=Définition %}}
Un **itérable** est un objet ou une structure de données sur lequel on peut parcourir ou répéter des actions. 
Imaginez une liste de courses : vous pouvez passer en revue **chaque élément un par un**. 
De la même manière, en programmation, un **itérable** permet de traiter chaque élément de manière séquentielle, comme une liste, un tableau, etc..
{{% /notice %}}

La fonction `range()` est un **itérable**, dans le sens qu'elle génère une séquence de nombres.

**Générer des séquences de nombres (entiers):**

```python
for i in range(5):
    print(i)
```
Cela affichera les nombres de 0 à 4. `range(5)` génère la séquence de 5 entiers suivants: 0, 1, 2, 3, 4

### Le nombre d'arguments de la fonction RANGE

La fonction `range()` peut accepter un, deux ou trois arguments, selon les besoins. 

Voici un aperçu des différents cas où `range()` peut accepter plus d'un argument :

1. **Deux arguments :**

- Lorsque `range()` accepte deux arguments, ils représentent le **début** et la **fin** de la séquence. 
Par exemple, `range(3, 10)` génère une séquence de nombres commençant à 3 et se terminant juste avant 10 (c'est-à-dire 3, 4, 5, 6, 7, 8, 9).

   ```python
   for i in range(3, 10):
       print(i)
   ```

   ```plaintext
   3
   4
   5
   6
   7
   8
   9
   ```

2. **Trois arguments :**
   Avec trois arguments, le premier représente le début de la séquence, le deuxième la fin, et le troisième le pas (ou l'incrément). Par exemple, `range(3, 10, 2)` génère une séquence de nombres commençant à 3, se terminant juste avant 10, avec un pas de 2 (c'est-à-dire 3, 5, 7, 9).

   ```python
   for i in range(3, 10, 2):
       print(i)
   ```

{{% notice style=tip title=Astuce %}}
De manière générale, pour générer une séquence croissante d'entiers consécutifs dont le premier terme est **debut** et le dernier terme est **fin**, on peut écrire:
```python
range(debut,fin+1)
```
{{% /notice %}}

{{% notice style=info %}}
Nous verrons les fonctions `arrange()` et `linespace()` dans le cours sur la [bibliothèque NumPy](/Semaine13/numpy.md).
{{% /notice %}}

### Boucle FOR dans un ordinogramme

Dans un ordinogramme, une boucle `for` est représentée par un rectangle qui contient la condition de la boucle, avec une flèche qui boucle vers l'arrière pour indiquer la répétition.

![Ordinogramme FOR](../ordino-boucle-FOR.png?width=35vw)

## Les boucles imbriquées

{{% notice style=info title=Définition %}}
Les **boucles imbriquées** sont des boucles à l'intérieur d'autres boucles. 
Elles sont utiles pour travailler avec des structures de données multidimensionnelles.
{{% /notice %}}

**Exemple :**

{{% notice style=info %}}
Nous verrons les tableaux 1D dans le cours sur la [bibliothèque NumPy](/Semaine13/numpy.md).
{{% /notice %}}

```python
# Tableau 2D
tableau = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for ligne in tableau:
    for élément in ligne:
        print(élément, end=" ")
    print()
```
Cet exemple parcourt chaque élément d'un tableau 2D et les affiche.

## Ateliers

[Boucle for](../atelier-for.ipynb)