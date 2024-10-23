+++
title =  "Les Objets"
weight = 72
+++

![Les objets](../objets.png?width=20vw)

## Qu'est-ce qu'un objet ?

En programmation, un objet est une structure qui regroupe des **données** et des **méthodes** qui manipulent ces données. Les objets sont la pierre angulaire de la programmation orientée objet (POO), un paradigme qui organise le code en entités réutilisables et modulaires.


| Concept | Définition |
| --- | --- |
| Classe | Une classe est un plan ou un modèle pour créer des objets. |
| Objet | Un objet est une instance d'une classe. |
| Attributs | Les attributs sont des variables qui appartiennent à une classe ou à un objet. |
| Méthodes | Les méthodes sont des fonctions définies à l'intérieur d'une classe. |


### Exemple

```python
ma_liste = list()
ma_liste.append(3)
len(ma_liste)

```

`ma_liste` est un *objet* créé à partir de la recette de la *classe* `list`.
`ma_liste` contient plusieurs *méthodes* qui permettront de gérer/manipuler les *données*.
Par exemple, `append` permet d'ajouter une donnée.
`len` est une *fonction* externe à la classe qui permet d'obtenir le nombre de données que `ma_liste` contient.


### Encapsulation

L'avantage des objets est que les méthodes et données sont **encapsulés**.
L'utilisateur n'a pas besoin de comprendre en profondeur comment fonctionne l'objet.
Il doit comprendre comment l'utiliser.  
Dans l'exemple ci-haut, l'utilisateur doit comprendre que la méthode `append` ajoute une nouvelle valeur à la liste. Mais il n'a pas besoin de comprendre le code à l'intérieur de l'objet.


### Méthode vs Fonction

Une **fonction** est un bloc de code qui effectue une tâche spécifique. Elle peut prendre des arguments comme entrée et peut retourner une valeur. Les fonctions sont définies indépendamment des objets et peuvent être appelées n'importe où dans le code.

Une **méthode** est similaire à une fonction, mais elle est associée à un objet. Les méthodes sont définies au sein d'une classe et sont appelées sur des instances de cette classe.


L'une des différences les plus évidentes est dans la manière dont elles sont utilisées.
Les méthodes sont appelées en ajoutant un point après la variable, suivi du nom de la méthode.
Les fonctions, quant à elles, prennent la variable comme argument. Exemple:

```python
x = [1, 2, 3]
x.append(4)  # méthode permettant d'ajouter une valeur
len(x)       # fonction qui permet d'obtenir la longueur de la liste
```

## Atelier

[Les objets](../atelier_objets.ipynb)
