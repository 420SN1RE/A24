+++
title = 'Lecture et affichage de données'
weight = 31
+++

![Lecture et affichage](../interaction.jpg?width=25vw).


Pour qu’un programme soit réutilisable, il faut que l'utilisateur puisse interagir avec, c'est-à-dire lui fournir des données en entrée à volonté.

La capacité d'un programme de lire des données au clavier est essentielle en programmation. 

## Lecture de données au clavier

La méthode `input()` est utilisée pour lire une ligne de texte entrée par l'utilisateur. Elle permet de capturer les données saisies au clavier et de les utiliser dans un programme. Voici un exemple simple :

```python
# Demander à l'utilisateur de saisir son nom
nom = input("Entrez votre nom : ")

# Afficher un message de bienvenue
print("Bonjour", nom)
```

Dans cet exemple :
1. La fonction `input("Entrez votre nom : ")` affiche le message "Entrez votre nom : " et attend que l'utilisateur saisisse quelque chose.
2. Une fois que l'utilisateur a saisi son nom et appuyé sur Entrée, le texte saisi est stocké dans la variable `nom`.
3. La fonction `print("Bonjour", nom)` affiche un message de bienvenue en utilisant le nom saisi par l'utilisateur.

Quelques points importants à noter :
- La méthode `input()` retourne toujours une chaîne de caractères. Si vous avez besoin d'un autre type de données (comme un nombre), vous devrez convertir la chaîne en utilisant des fonctions comme `int()` ou `float()`.
- Vous pouvez personnaliser le message affiché par `input()` pour guider l'utilisateur sur ce qu'il doit saisir.

Par exemple, pour demander un âge et l'utiliser dans un calcul :

```python
# Demander à l'utilisateur de saisir son âge
age = input("Entrez votre âge : ")

# Convertir l'âge en entier
age = int(age)

# Calculer l'année de naissance approximative
annee_naissance = 2024 - age

# Afficher l'année de naissance
print("Vous êtes probablement né(e) en ", annee_naissance)
```
### Ordinogramme

Pour représenter la saisie et la lecture d'une donnée, on utilise le rectangle (traitement) et le parallélogramme (entrée de données). Par exemple, l'ordinogramme du code précédent est:

![Ordinogramme input](../ordino-input.png?width=25vw)

## Affichage textuel des résultats

**Rappel**: La fonction `print()` affiche les données qui sont indiquées entre les parenthèses, séparés par une virgule. Ces données s'affichent séparées par des espaces.

Si l'on veut personnaliser l'affichage des nos données. il va falloir les formater.

### Formater l'affichage

Python permet de formater des chaînes de caractères de différentes manières, notamment avec 
1. Les `f-strings` (recommandés) 
2. La méthode `format()` (encore utilisée)
3. L’opérateur de formatage `%`(désuet).

Aujourd’hui les méthodes 2 et 3 sont obsolètes, la méthode préconisée pour le formatage est les `f-string` que nous verrons plus en détail [ici](https://420sn1re.github.io/A24/semaine6/chaines_caracteres/index.html#les-f-strings).
