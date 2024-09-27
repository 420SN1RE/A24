+++
title = "Exercices récapitulatifs"
weight = 75
+++

![Exos Récapitulatifs](../exos.jpg?width=25vw)

**Objectif :** Ces exercices visent à évaluer votre compréhension de la syntaxe de base, la manipulation des listes et les concepts de programmation orientée objet (POO) en manipulant des chaînes de caractères.

# Exercice 1

## Contexte

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

# Exercice 2

## Contexte

Vous allez créer un programme qui gère une liste de produits dans un magasin. Le programme doit permettre à l’utilisateur d’ajouter des produits, de les afficher, et de rechercher des produits spécifiques en fonction de leur nom ou de leur prix.

## Instructions

1. **Variables et types de données** :
- Créez une liste vide produits pour stocker les produits.
- Chaque produit doit être représenté par un dictionnaire contenant les clés nom (chaîne de caractères) et prix (nombre flottant).

2. **Entrées au clavier** :
- Demandez à l’utilisateur combien de produits il souhaite ajouter.
- Utilisez une boucle pour permettre à l’utilisateur d’entrer le nom et le prix de chaque produit.

3. **Transtypage** :
- Assurez vous de convertir les entrées de l’utilisateur en types de données appropriés (par exemple, convertir le prix en nombre flottant).

4. **Structures conditionnelles** :
- Ajoutez une option pour rechercher un produit par son nom ou par son prix.
- Si l’utilisateur choisit de rechercher par nom, demandez le nom et affichez les produits correspondants.
- Si l’utilisateur choisit de rechercher par prix, demandez le prix et affichez les produits dont le prix est inférieur ou égal à ce montant.

5. **Boucles** :
- Utilisez des boucles pour parcourir la liste des produits et afficher les résultats de la recherche.

6. **Listes et chaînes de caractères** :
- Affichez la liste complète des produits avec leur nom et leur prix formatés correctement.


## Jeu de test 1 : Ajout et affichage de produits

1. **Entrées** :
   - Nombre de produits : 3
   - Produit 1 : Nom = "Pomme", Prix = 1.5
   - Produit 2 : Nom = "Banane", Prix = 0.8
   - Produit 3 : Nom = "Orange", Prix = 1.2

2. **Sortie Attendue** :
   - Liste des produits :
     ```
     Nom: Pomme, Prix: 1.5
     Nom: Banane, Prix: 0.8
     Nom: Orange, Prix: 1.2
     ```

## Jeu de test 2 : Recherche par nom

1. **Entrées** :
   - Nombre de produits : 2
   - Produit 1 : Nom = "Lait", Prix = 2.5
   - Produit 2 : Nom = "Pain", Prix = 1.0
   - Recherche : nom
   - Nom à rechercher : "Lait"

2. **Sortie Attendue** :
   - Produit trouvé :
     ```
     Produit trouvé - Nom: Lait, Prix: 2.5
     ```

## Jeu de test 3 : Recherche par prix

1. **Entrées** :
   - Nombre de produits : 4
   - Produit 1 : Nom = "Chocolat", Prix = 3.0
   - Produit 2 : Nom = "Bonbon", Prix = 0.5
   - Produit 3 : Nom = "Biscuit", Prix = 1.5
   - Produit 4 : Nom = "Jus", Prix = 2.0
   - Recherche : prix
   - Prix maximum : 2.0

2. **Sortie Attendue** :
   - Produits trouvés :
     ```
     Produit trouvé - Nom: Bonbon, Prix: 0.5
     Produit trouvé - Nom: Biscuit, Prix: 1.5
     Produit trouvé - Nom: Jus, Prix: 2.0
     ```

## Jeu de test 4 : Entrée invalide pour la recherche

1. **Entrées** :
   - Nombre de produits : 1
   - Produit 1 : Nom = "Eau", Prix = 0.7
   - Recherche : couleur (option invalide)

2. **Sortie Attendue** :
   - Message d'erreur :
     ```
     Option de recherche invalide.
     ```

## Jeu de test 5 : Aucun produit trouvé

1. **Entrées** :
   - Nombre de produits : 2
   - Produit 1 : Nom = "Café", Prix = 3.5
   - Produit 2 : Nom = "Thé", Prix = 2.5
   - Recherche : nom
   - Nom à rechercher : "Lait"

2. **Sortie Attendue** :
   - Aucun produit trouvé (aucune sortie spécifique attendue pour ce cas, mais le programme ne doit pas planter).


## Points à vérifier :

- Assurez vous que les entrées de l’utilisateur sont correctement converties en types de données appropriés.
- Vérifiez que les boucles et les conditions fonctionnent comme prévu.
- Testez le programme avec différents scénarios pour vous assurer qu’il gère correctement les entrées et les recherches.