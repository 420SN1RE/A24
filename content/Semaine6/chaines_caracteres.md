+++
title = "Les chaînes de caractères"
weight =  62
+++

![Chaines de caractères](../chaines.jpeg?width=30vw)


## Quelques rappels sur les chaînes de caractères

- Une **chaîne de caractères** est simplement plusieurs caractères regroupés ensemble, entourés de guillemets simples (`'`) ou doubles (`"`).
- Les caractères peuvent être des lettres, chiffres, symboles ou espaces.
- Les chaines de caractères sont appelées **string**. 
- Nous pouvons concaténer des chaînes, mais ce n'est pas tout...
 
## Opérations sur les chaines de caractères

Les chaînes de caractères en Python sont puissantes et flexibles. En les traitant comme des listes de caractères, vous pouvez effectuer une variété d’opérations pour manipuler et transformer vos données textuelles. 
Par exemple: extraire ou chercher des sous-chaînes, les modifier, etc...

## Les chaines de caractères sont des listes

### Accès aux caractères individuels

Vous pouvez accéder à chaque caractère d'une chaîne en utilisant des indices, de la même manière que vous le feriez avec une liste. Les indices commencent à 0.

```python
chaine = "Bonjour"

print(chaine[0])  # Affiche B
print(chaine[1])  # Affiche o
```

![indices](../chaine_01.png)

### Longueur d'une chaine de caractères

Vous pouvez obtenir le nombre de caractères dans une chaine, avec la méthode `len()`.

```python
chaine = "Bonjour"

longueur = len(chaine)
print("La longueur de la chaîne est:", longueur)
```

Affiche :
```python
La longueur de la chaîne est: 7
```

### Itération sur les caractères

Vous pouvez itérer sur chaque caractère d'une chaîne en utilisant une boucle `for`.

```python
chaine = "Bonjour"

for caractere in chaine:
    print(caractere)
```
Affiche:

```python
B
o
n
j
o
u
r
```

### Slicing (découpage)

Le slicing vous permet d'extraire une sous-chaîne d'une chaîne existante.

```python
chaine = "Bonjour"

# Extraire les caractères aux index 1 à 3 inclus
sous_chaine = chaine[1:4] 
print(sous_chaine)  # Affiche onj
```

## L'immutabilité des chaînes

Les chaînes en Python sont **immuables**, ce qui signifie qu'une fois créées, elles ne peuvent pas être modifiées. 

{{% notice note %}}
Toute opération qui semble modifier une chaîne crée en réalité une nouvelle chaîne.
{{% /notice %}}


```python
chaine = "Bonjour"

# Extraire et concaténer les caractères "Bon" avec "a" et avec "jour"
chaine_modifiee = chaine[:3] + 'a' + chaine[4:]
print(chaine_modifiee)  # Affiche Bonajour
```

### Conversion entre chaînes et listes

Vous pouvez convertir une chaîne en une liste de caractères et vice versa.

```python
chaine = "Bonjour"

liste_caracteres = list(chaine)
print(liste_caracteres)  # Affiche ['B', 'o', 'n', 'j', 'o', 'u', 'r']

chaine_recomposee = ''.join(liste_caracteres)
print(chaine_recomposee)  # Affiche Bonjour
```

### Autres méthodes utiles des chaînes

Python fournit de nombreuses méthodes intégrées pour manipuler les chaînes de caractères.

| Méthode | Description |
| ---- | ----|
|  `upper()` | Convertir en majuscules.|
| `lower()` | Convertir en minuscules.|
| `replace(old, new)` | Remplacer une sous-chaîne par une autre.|
| `split(delim)` | Découper une chaîne en une liste de sous-chaînes.|
| `strip()` | Supprimer les espaces en début et fin de chaîne.|

Exemples: 

```python
print(chaine.upper())  # BONJOUR
print(chaine.replace('o', 'a'))  # Banjaur
print(chaine.split('o'))  # ['B', 'nj', 'ur']
print(chaine.strip())  # Bonjour (si des espaces étaient présents)
```

## Formater les chaines de caractères

### Insertion de variables

Il est possible d'insérer facilement des variables dans des chaînes de caractères.
Une première solution est d'utiliser la concaténation:

```python
nombre1 = 23
nombre2 = 35
la_chaine = "Le nombre " + str(nombre1) + " est plus petit que " + str(nombre2)
print(la_chaine)   # Affiche:  Le nombre 23 est plus petit que 35
```

Mais il est préférable d'utiliser les `f-strings`

### Les f-Strings

**Exemple**:

```python
nombre1 = 23
nombre2 = 35
la_chaine = f'Le nombre {nombre1} est plus petit que {nombre2}'
print(la_chaine)   # Affiche:  Le nombre 23 est plus petit que 35
```

**Explication**:

- `f-string` : Le `f` avant les guillemets indique que la chaîne de caractères est une `f-string`. Cela permet d’incorporer des expressions Python directement dans la chaîne.
- `{ }` : Les accolades `{ }` sont utilisées pour inclure des expressions Python à l’intérieur de la chaîne. Ces expressions sont évaluées au moment de l’exécution et leurs valeurs sont insérées dans la chaîne.

### Les caractères "spéciaux"

**Rappel** : Le `\` permet d'échapper le caractère suivant.

Le tableau ci-dessous présente quelques caractères d’échappement couramment utilisés en Python et leur rôle respectif :

| Caractère |  Rôle|
| --- | --- |
| `\t` | Tabulation |
| `\n` | Retour de ligne |
| `\\` | Barre oblique inversée (Backslash) |


## Manipulation des chaines de caractères

| Méthodes | Définition |
| ---- | ----|
| `[ ]` | Accède à un caractère selon sa position |
| `len()` | Retourne la longueur de la chaîne |
| `str()` | Convertit en chaîne de caractères |
| `lower()` | Convertit tous les caractères de la chaîne en minuscules |
| `upper()` | Convertit tous les caractères de la chaîne en majuscules. |
| `strip()` | Supprime les espaces (ou autres caractères spécifiés) au début et à la fin de la chaîne |
| `replace()` | Remplace toutes les occurrences de la sous-chaîne |
| `split()` | Divise la chaîne en une liste de sous-chaînes |
| `join()` | Concatène une séquence d'éléments (comme une liste) en une seule chaîne |
| `find()` | Renvoie l'indice de la première occurrence de la sous-chaîne |


| Opérations | Définition |
| ---- | ----|
| `*` | Multiplie (répète) une chaîne |
| `+` | Concatène des chaînes |


## Exemples

[Exemples sur les chaînes de caractères](../exemples_caracteres.ipynb)
