+++
title = 'Introduction à la programmation'
weight = 13
+++

![Intro à la programmation](../bases-prog2.jpg?width=25vw).

## Qu'est-ce qu'un programme ?

Un programme, ou une application, ou encore un logiciel, est un *outil* permettant la réalisation de tâches.

- Traitement de texte
- Envois de messages
- Prévision météorologique
- Gestion de stock
- Montage vidéo

Pour réaliser ces tâches, un programme va implémenter un ou plusieurs **algorithmes** dans un **langage de programmation**.

## Qu'est-ce qu'un algorithme ?

- Un algorithme est une **suite d'actions** qui suivent un **ordre précis**.
- Cette suite d'actions représente les traitements sur les données.
- Un algorithme doit être **clair** et **précis**.
- Pour aider à concevoir la solution, un algorithme peut être traduit en [**ordinogramme**](../Semaine2/ordinogramme.md).

{{%notice style="warning" title="Attention"%}}
- Un algorithme **ne s'exécute pas**, il représente les étapes que le programme devra faire.
    - C'est **l'implémentation** (le code) avec un langage qui s'**exécute**.
    - Il peut y avoir plusieurs **implémentations** d'un même algorithme.
{{% /notice%}}

**Exemples d'algorithmes que vous connaissez déjà :**

- Une recette de cuisine.
- Les instructions pour assembler un meuble.
- Les instructions pour préparer un café chaud avec du lait.
- La méthode pour calculer la somme des nombres de 1 à 100.
- Etc.

## Qu'est-ce qu'un langage de programmation ?

- Un langage de programmation est un **ensemble de mots clés** et des **règles de syntaxe** qui permettent d'écrire un __programme__ exécutable par un système informatique.

- **NB:** un système informatique ne comprend que le binaire (0 et 1), un langage de programmation est le meilleur moyen d'avoir un langage intelligible pour faire une interface entre l'homme et la machine (le binaire).

- Le rêve ultime est d'utiliser le langage naturel (le français par exemple) pour écrire un programme. C'est ce qu'essaye d'entreprendre certaines compagnies d'intelligence artificielle. Les résultats pour le moment restent mitigés.

En attendant la réalisation de cette promesse, voici quelques langages couramment utilisés:

- **Ex**: Python, C/C++, C#, java, Matlab, ....
- Langages de programmation les plus populaires : [TIOBE Index](https://www.tiobe.com/tiobe-index/)

{{% notice info %}}
Aucun langage n'est parfait pour toutes les tâches. On doit choisir le meilleur compromis pour la tâche à accomplir.

En général les gros logiciels professionnels sont écrit avec plusieurs langages de programmation.
{{% /notice%}}

## Cycle de développement logiciel

Le cycle de développement d'un logiciel se décompose en plusieurs étapes que nous pouvons retrouver à travers ce schéma :

![Cycle de développement](../cycle.png)

[Goffinet, F. (2021, 11 novembre). Concepts de développement logiciel.](https://cisco.goffinet.org/devasc/concepts-dev-developpement-logiciel/)

Le schéma représente un cercle fermé car un logiciel n'est jamais complètement fini. Il est en constante évolution dû à des besoins utilisateurs grandissants.

## Pourquoi Python ?

- Ce langage est très utilisé dans la communauté scientifique, car il est facile à prendre en main et il offre une bonne compatibilité avec les autres outils scientifiques. Il est souvent défini comme une colle entre ces outils.

- Il propose aussi un grand nombre de librairies d'analyse scientifique très robustes comme : [*NumPy*](../Semaine13), [*Pandas*](../Semaine11/Pandas.md), [*MatplotLib*](../Semaine12/Matplotlib.md)...

- Python est un langage interprété orienté objet. Sa syntaxe simple offre une multitude de possibilité de développement. Il est possible de créer **ses propres modules** qui seront ensuite partagés à la communauté.
Exemple : [pipy](https://pypi.org/).

C’est un langage de programmation assez classique, il propose les mécanismes standards suivants :
- **Données typées** : entiers, réels, booléens, chaînes de caractères.
- **Structures avancées de données** : listes, dictionnaires, classes.
- **Séquences d’instructions** : écrire et exécuter une série de commandes sans avoir à intervenir entre les instructions.
- **Structures algorithmiques** : branchements conditionnels et boucles.
- **Programmation structurée** : utiliser les procédures et fonctions pour mieux organiser son code.
- Appeler plusieurs fichiers d’extension “.py” dans d’autres programmes à l’aide de la commande “import”.

Il offre aussi l'avantage d'être un langage **libre** et **open source**.

## Comment écrire un programme ?

### Visual Studio Code

![Logo de VS Code](../VSCode.png?width=5vw&classes=left)

Dans ce cours, nous allons utiliser un environnement de développement (IDE) pour développer nos programmes d'analyse scientifiques avec Python. Il s'agit de [Visual Studio Code](../outils/VSCode-Jupyter/_index.md).

- *Visual Studio Code* est comme un cahier de notes pour écrire du code.
- Il est **gratuit** et peut être utilisé avec beaucoup de langages de programmation, dont Python.
- Il a des fonctionnalités pratiques, comme :
    + aider à compléter le code.
    + executer le programme en cours de développement.
    + trouver des erreurs.
    + mettre en forme le code, etc.

- On peut aussi ajouter des **extensions** pour avoir plus de fonctionnalités, comme intégrer des **bibliothèques scientifiques**, des vérificateurs de code, des testeurs, etc.

### Interface de Visual Studio Code

![Interface de VS Code](../VSCode-GUI.png?width=150vw)

### Premier exemple de programme en Python

Exemple de programme simple dans python :

```python
# Exemple d'un programme simple qui effectue la somme de 2 nombres
# Données en entrée
x = 5
y = 7

# Traitement
somme = x + y

# Affichage
print('La somme x + y est égale à : ', somme)
```

{{% notice style="info" %}}
 Un programme informatique fait ce que vous lui dites de faire, pas ce que vous voulez qu'il fasse.
{{% /notice%}}

Voyons ensemble comment exécuter ce programme.

[Exemple à télécharger](../exemple_programme.py)

[Outils: VS Code et Jupyter](../outils/VSCode-Jupyter/_index.md)

## PAUSE 5 minutes

![PAUSE 5 mins](../pause.jpg?width=25vw).



