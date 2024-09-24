+++
title = "Exercice récapitulatif"
weight = 75
+++

![Exo Récapitulatif](../exos.jpg?width=25vw)

**Objectif :** Cet exercice vise à évaluer votre compréhension de la syntaxe de base, la manipulation des listes et les concepts de programmation orientée objet (POO) en manipulant des chaînes de caractères.

## Contexte :

Vous allez créer un programme en Python pour analyser une chaîne de caractères saisie au clavier. Le programme doit compter le nombre de caractères, identifier les caractères uniques et calculer la fréquence de chaque caractère.

## Ce que le programme doit faire :

**Déterminer si l'utilisateur a le droit d'utiliser le programme**

- Demander à l'utilisateur d'entrer son prénom.
- Demander à l'utilisateur d'entrer son âge.
- Si l'utilisateur à moins de 18 ans, à l'aide de `f-string`, on l'informe qu'il n'a pas le droit d'utiliser ce programme et le programme s'arrête.
- Si l'utilisateur à plus de 18 ans, on lui demande d'entrer une phrase au clavier. Par exemple "Bonjour tout le monde" et l'analyse de la phrase se fait.

**Gestion de la chaine de caractères à analyser.**

- Utiliser trois listes pour stocker :
   1. Les caractères de la chaine.
   1. Les caractères uniques.
   1. La fréquence de chaque caractère.

**Analyse de la chaine de caractères pour déterminer les caractères uniques et la fréquence.**

- Utiliser une boucle pour parcourir chaque caractère de la chaîne.
- Utiliser les fonctions et méthodes de listes/chaines:
   - `append()` pour ajouter des caractères dans une liste.
   - `lower()` pour ne traiter que des caractères en minuscules.
   - `len()` pour obtenir la longueur d'une chaine ou liste.
   - `index()` pour trouver la position (l’indice) d’un élément spécifique dans une liste.

**Logique de l'analyse**

- Créer une liste pour stocker tous les caractères de la chaîne.
- Utiliser une boucle pour ajouter chaque caractère de la chaîne à la liste de caractères.
- Créer une liste pour stocker les caractères uniques.
- Utiliser une liste de fréquence des caractères pour compter la fréquence de chaque caractère.
- Implémentez une condition pour vérifier si un caractère est déjà présent dans la liste des caractères uniques avant de l'ajouter.
- Une fois le décompte terminé, à l'aide de `f-string` afficher les résultats (nombre de caractères analysés, liste des caractères uniques) 

## Exemple de résultats 

- Si le prénom saisi est "Nathalie" et l'âge 16

```plaintext
Bonjour Nathalie, malheureusement, ce programme est réservé au plus de 18 ans et vous n'avez que 16 ans.
```

- Si le prénom saisi est "Nathalie" et l'âge 30 et le texte est "Bonjour tout le monde"

```plaintext
Nombre de caractères: 21
Caractères uniques: ['b', 'o', 'n', 'j', 'u', 'r', ' ', 't', 'l', 'e', 'm', 'd']
Fréquence des caractères: [1, 4, 2, 1, 2, 1, 3, 2, 1, 2, 1, 1]
```


