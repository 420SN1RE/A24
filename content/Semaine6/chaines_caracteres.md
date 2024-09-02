+++
title = "Les chaînes de caractères"
weight =  62
+++

![Chaines de caractères](../chaines.jpeg?width=30vw)


## Qu'est-ce qu'une chaîne de caractères ?

{{% notice style=info title=Définition %}}
Une **chaîne de caractères** est simplement plusieurs caractères regroupés ensemble.
{{% /notice %}}

- Les caractères peuvent être des lettres, chiffres, symboles ou espaces.
- Les chaînes de caractères sont des objets que nous pouvons manipuler.
- Nous pouvons concaténer des chaînes, extraire ou chercher des sous-chaînes, les modifier, etc...

En python, les chaînes de caractères sont appelées **string** ou **str**. Elles sont entourées de guillemets simples (`'`) ou doubles (`"`):

```python
une_chaine = 'Bonjour'
une_autre = "Allo"
```

- Les chaînes en Python sont **immuables**, ce qui signifie qu'une fois créées, elles ne peuvent pas être modifiées. 
- Toute opération qui semble modifier une chaîne crée en réalité une nouvelle chaîne. 
- Pour l'utilisateur (programmeur), l'immutabilité est transparente dans la plupart des cas.

## Formater les chaines

### Les f-Strings

**Exemple**:
```python
nom = "Laurence"
age = 30
print(f"Je m'appelle {nom} et j'ai {age} ans.")
```

**Explication**:

- `f-string` : Le `f` avant les guillemets indique que la chaîne de caractères est une `f-string`. Cela permet d’incorporer des expressions Python directement dans la chaîne.
- `{ }` : Les accolades `{ }` sont utilisées pour inclure des expressions Python à l’intérieur de la chaîne. Ces expressions sont évaluées au moment de l’exécution et leurs valeurs sont insérées dans la chaîne.

- `nom` est une variable contenant la chaîne "Laurence".
- `age` est une variable contenant le nombre 30.

Lorsque le code est exécuté, l’expression `f"Je m'appelle {nom} et j'ai {age} ans."` est évaluée, et les valeurs des variables `nom` et `age` sont insérées à leurs emplacements respectifs dans la chaîne. Le résultat sera :

```plaintext
Je m'appelle Laurence et j'ai 30 ans.
```

## Comment utiliser une chaîne de caractères ?

### Fonctions, opérations et méthodes

| Fonctions |  |
| ---- | ----|
| `len()` | Retourne la longueur de la chaîne |
| `str()` | Convertit en chaîne de caractères |


| Opérations |  |
| ---- | ----|
| `*` | Multiplie une chaîne |
| `+` | Concatène des chaînes |


| Méthodes |  |
| ---- | ----|
| `[ ]` | Accède à un caractère selon sa position |
| `lower()` | Convertit tous les caractères de la chaîne en minuscules |
| `upper()` | Convertit tous les caractères de la chaîne en majuscules. |
| `strip()` | Supprime les espaces (ou autres caractères spécifiés) au début et à la fin de la chaîne |
| `replace()` | Remplace toutes les occurrences de la sous-chaîne |
| `split()` | Divise la chaîne en une liste de sous-chaînes |
| `join()` | Concatène une séquence d'éléments (comme une liste) en une seule chaîne |
| `find()` | Renvoie l'indice de la première occurrence de la sous-chaîne |

### Les indices

![indices](../chaine_01.png)

#### Exemples

[Exemples sur les chaînes de caractères](../exemples_caracteres.ipynb)

#### Caractères "spéciaux"


| Caractère |  |
| --- | --- |
| `\t` | Tabulation |
| `\n` | Retour de ligne |
| `\\` | Barre oblique inversée (Backslash) |

Le `\` permet d'échapper le caractère suivant.

### Insertion de variables

Il est possible d'insérer facilement des variables dans des chaînes de caractères.
Une première solution est d'utiliser la concaténation:

```python
var1 = 23
var2 = 35
la_chaine = "Le nombre " + str(var1) + " est plus petit que " + str(var2)
print(la_chaine)   # Affiche:  Le nombre 23 est plus petit que 35
```

Mais il est préférable d'utiliser le f-strings :

```python
var1 = 23
var2 = 35
la_chaine = f'Le nombre {var1} est plus petit que {var2}'
print(la_chaine)   # Affiche:  Le nombre 23 est plus petit que 35
```

### Dans une boucle

Il est possible d'itérer sur chaque lettre de la chaîne:

```python
for lettre in "Bonjour":
    print(lettre)
```

## Atelier

[Les chaînes de caractères](../atelier_caracteres.ipynb)
