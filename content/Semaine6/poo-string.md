+++
title = "La classe, les objets et l'encapsulation"
weight = 63
+++

![POO et String](../poo-string.jpeg?width=25vw)


Nous allons explorer trois concepts fondamentaux de la programmation orientée objet : 
1. la classe
1. les objets (ou instances de classe) et 
1. l'encapsulation. 

Pour rendre ces notions plus accessibles, nous utiliserons des exemples simples avec des chaînes de caractères.

## La classe

Une `classe` peut être vue comme un modèle qui définit les `propriétés` et les comportements (`méthodes`) que ses `objets` auront.

Par exemple, imaginons une classe `Personne` qui a une propriété `prenom`.

## Les objets (instances de classes)

Un objet est une `instance d'une classe`. 

Une **instance de classe** est un **objet concret créé à partir d'une classe**. Pensez à une instance comme à un objet réel construit à partir d'un modèle (la classe). 

Chaque instance de classe possède ses propres valeurs pour les `propriétés` et `méthodes` définies dans la classe.

Par exemple, si nous avons une classe `Personne` définie avec une propriété `prenom`. Nous pouvons créer un objet de cette classe en utilisant le code suivant ::


```python
personne1 = Personne("Nathalie")
personne2 = Personne("Laurent")
```

Ici, `personne1` et `personne2` sont des **instances** de la classe `Personne`. Chacune a sa propre valeur pour la propriété `prenom` (`"Nathalie"` pour `personne1` et `"Laurent"` pour `personne1`).


## L'encapsulation

L'encapsulation consiste à **cacher les détails de l'implémentation** d'un objet et à n'exposer que les aspects nécessaires pour interagir avec cet objet. Cela signifie que les données internes d'un objet sont protégées contre les modifications non autorisées et que l'accès à ces données se fait uniquement par des méthodes définies.

{{% notice note %}}
L'encapsulation permet de séparer ce que l'utilisateur peut voir et utiliser, des détails internes de l'objet.
{{% /notice %}}

**Par exemple**: 
Lorsque vous conduisez une voiture, avez-vous besoin de savoir comment le moteur est fait pour pouvoir la conduire? La réponse est **Non**. Il vous faut simplement savoir où mettre la clé pour démarrer le moteur, quelle pédale appuyer pour accélérer, quel bouton utiliser pour allumer la radio, etc. 

En programmation, l'encapsulation c'est la même chose. Voici quelques exemples que vous connaissez déjà:
- On n'a pas besoin de savoir comment la méthode `print()` est codée à l'intérieur pour l'utiliser pour afficher des phrases. 
- Idem pour `int()`, `float()`, `str()` ou `bool()` pour convertir des données en entier, en nombre à virgule, en chaine de caractère ou en booléen respectivement.


## Manipulation des chaînes de caractères en tant qu'objets

En plus d'être des listes, les chaines de caractères sont aussi des objets (de la classe `String`). On peut alors utiliser leurs propriétés et méthodes sur des instances de `String`.

Par exemple, pour convertir une chaîne en majuscules, nous pouvons utiliser la méthode `upper()` :

```python
prenom = "Julie"
prenom_majuscule = prenom.upper()
print(prenom_majuscule)  # Affiche "JULIE"
```
**Essayez le code ci-dessous. Qu'est-ce qui s'affiche ?:**

```python
print("nathalie".upper())
```

{{% notice info %}}
Grâce aux guillemets, Python reconnait que "nathalie" est une chaine de caractères. C'est pour cela qu'on peut utiliser `.upper()` pour la mettre en lettres majuscules.
{{% /notice %}}

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
chaine1 = "Bonjour"
chaine2 = "   Bonjour    "
print(chaine1.replace('o', 'a'))  # Affiche Banjaur
print(chaine1.split('o'))  # Affiche ['B', 'nj', 'ur']
print(chaine2.strip())  # Affiche Bonjour 
```
