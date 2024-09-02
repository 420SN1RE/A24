+++
title = 'Ordinogramme'
weight = 21
+++

![Ordinogramme Moyenne de deux nombres](../algo-ordino1.jpg?width=25vw).

Avant d’implémenter l’algorithme dans un langage en particulier, il existe plusieurs manières / outils pour nous aider à valider formellement le bon fonctionnement de l'algorithme :
- du pseudo-code[^1].
- un ordinogramme / organigramme de programmation.


[^1]: Le Python est un langage tellement proche du pseudo-code, que nous le mentionnons seulement pour que vous en ayez connaissance. Nous ne l'utiliseront pas pour ce cours.

## L'ordinogramme (ou organigramme de programmation)

- Les ordinogrammes est une représentation graphiques des **étapes** de l'algorithme.
- Le programmeur devra traduire l’ordinogramme à l’aide d’un langage de programmation.
- L’organigramme de programmation utilise des symboles normalisés représentés ci- dessous :

![Symboles de base d'un ordinogramme](../ordino_symb.jpg?width=40vw "Symboles de base d'un ordinogramme").

### Exemples d'ordinogrammes

**Exemple 1 : Devinette d'un nombre**

![Ordinogramme Moyenne entre deux nombres](../ordino_devinette.png?width=25vw).


{{% notice note %}}
La compréhension des algorithmes et la capacité à les représenter sous forme d'ordinogrammes sont des compétences précieuses à acquérir.
{{% /notice %}}

## Atelier

Avant d’effectuer vos exercices vous devez installer drawio sur VS Code:

**Etape 1**: Rendez-vous dans la partie de gauche de Visual Studio Code et trouvez le logo “Extensions”, cherchez draw.io dans la barre de recherche.

![draw io](../drawio.png?width=30vw)

**Etape 2**: cliquez sur installer
![draw io](../drawio_installation.png?width=30vw)

### Exercice 1

- Écrire un ordinogramme qui demande à l'utilisateur de saisir trois nombres et calcule la moyenne de trois nombres.

[Fichier pour l'exercice 1](../atelier-ordino1.drawio)

### Exercice 2

- Écrire un ordinogramme qui calcule et affiche l'aire d'un rectangle à partir de la longueur et de la largeur saisies par l'utilisateur.

[Fichier pour l'exercice 2](../atelier-ordino2.drawio)

### Exercice 3

- Écrire un ordinogramme qui demande à l'utilisateur de saisir le rayon d'un cercle, puis calcule la circonférence du cercle.

[Fichier pour l'exercice 3](../atelier-ordino3.drawio)

### Exercice 4

- Écrivez un ordinogramme qui demande à l'utilisateur de saisir une température en Fahrenheit, puis la convertit en Celsius.

[Fichier pour l'exercice 4](../atelier-ordino4.drawio)

### Exercice 5

- Reprenez l'ordinogramme qui fait deviner un nombre à l'utilisateur, et modifiez le pour indiquer à l'utilisateur si le nombre saisi est plus grand ou plus petit.

[Fichier pour l'exercice 5](../atelier-ordino5.drawio)

### Exercice 6

- Écrire un ordinogramme qui demande à l'utilisateur de saisir un nombre puis affiche tous ses diviseurs entiers.

Voici 2 exemples:
- diviseurs de 30: 1, 2, 3, 5, 6, 10, 15, 30
- diviseurs de 45: 1, 3, 5, 9, 15, 45

{{%notice style="tip" title="Astuce"%}}
- Quelle opération mathématique vous permet de savoir si un nombre est un diviseur entier ?
- Quand sait-on lorsqu'on a trouvé tous les diviseurs ?
{{% /notice%}}

[Fichier pour l'exercice 6](../atelier-ordino6.drawio)

--- 

{{% notice info %}}
L'algorithme ci-dessous est la première partie de l'algorithme du plus grand diviseur commun:

1. Dresser la liste des diviseurs de chacun des nombres.
1. Repérer les diviseurs communs.
1. Choisir le plus grand de ces diviseurs.
{{% /notice %}}

{{% expand title="Exemple de calcul de PGCD" %}}
PGCD(30, 45):
1. chercher les diviseurs
    - diviseurs de 30: {1, 2, 3, 5, 6, 10, 15, 30} 
    - diviseurs de 45: {1, 3, 5, 9, 15, 45}
1. repérer les diviseurs commun
    - {1, 3, 5, 15}
1. choisir le plus grand : 15
{{% /expand %}}

## Pause : 5 minutes

![Pause](../pause.jpg?width=25vw)