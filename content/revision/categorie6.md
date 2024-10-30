+++
title = "Les chaines de caractères"
weight = 6
+++

Les chaînes de caractères (ou strings) sont des séquences de caractères utilisées pour représenter du texte. 

## Création de chaînes de caractères

Vous pouvez créer des chaînes de caractères en utilisant des guillemets simples (`'`) ou doubles (`"`).

```python
chaine1 = 'Bonjour'
chaine2 = "Monde"
chaine3 = "C'est une chaîne avec des guillemets simples"
chaine4 = 'Il a dit "Bonjour"'
```

## Concaténation et répétition

Vous pouvez concaténer (joindre) des chaînes de caractères en utilisant l'opérateur `+` et les répéter en utilisant l'opérateur `*` :

```python
salutation = "Bonjour" + " " + "Monde"
print(salutation)  # Affiche "Bonjour Monde"

repetition = "Ha" * 3
print(repetition)  # Affiche "HaHaHa"
```

## Accès aux caractères

Les caractères individuels d'une chaîne peuvent être accédés en utilisant des indices, qui commencent à 0, comme les listes :

```python
chaine = "Python"
print(chaine[0])  # Affiche "P"
print(chaine[1])  # Affiche "y"
print(chaine[-1])  # Affiche "n" (dernier caractère)
```

## Slicing (découpage)

Le slicing permet d'extraire des sous-chaînes en utilisant la syntaxe `chaine[debut:fin:saut]` :

```python
chaine = "Python"
print(chaine[1:4])  # Affiche "yth"
print(chaine[:2])  # Affiche "Py"
print(chaine[2:])  # Affiche "thon"
print(chaine[::2])  # Affiche "Pto"
print(chaine[::-1])  # Affiche "nohtyP" (inversion de la chaîne)
```

## Méthodes utiles

Python fournit de nombreuses méthodes intégrées pour manipuler les chaînes de caractères. Voici quelques-unes des plus courantes :

- `lower()`: Convertit tous les caractères en minuscules.
```python
chaine = "Bonjour"
print(chaine.lower())  # Affiche "bonjour"
```

- `upper()`: Convertit tous les caractères en majuscules.
```python
print(chaine.upper())  # Affiche "BONJOUR"
```

- `strip()`: Supprime les espaces au début et à la fin de la chaîne.
```python
chaine = "  Bonjour  "
print(chaine.strip())  # Affiche "Bonjour"
```

- `replace(ancien, nouveau)`: Remplace toutes les occurrences de `ancien` par `nouveau`.
```python
chaine = "Bonjour Monde"
print(chaine.replace("Monde", "Python"))  # Affiche "Bonjour Python"
```

- `split(sep)`: Divise la chaîne en une liste de sous-chaînes en utilisant `sep` comme séparateur.
```python
chaine = "Bonjour,Monde,Python"
print(chaine.split(","))  # Affiche ['Bonjour', 'Monde', 'Python']
```

- `join(iterable)`: Concatène une liste de chaînes en une seule chaîne, en utilisant la chaîne appelante comme séparateur.
```python
liste = ["Bonjour", "Monde", "Python"]
print(" ".join(liste))  # Affiche "Bonjour Monde Python"
```