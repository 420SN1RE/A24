+++
title = "Le concept de la Régression Linéaire"
weight = 131
draft = true
+++

![](../regLineaire.png?width=25vw)


## Le concept de la régression linéaire

La **régression linéaire** est une méthode statistique utilisée pour comprendre la **relation entre deux variables**. 
Imagine que tu veux savoir si la température extérieure influence la consommation d’électricité. Voici comment ça fonctionne, de manière simple :

1. **Deux variables** : La température extérieure (variable indépendante) et la consommation d’électricité (variable dépendante).
2. **Tracer les points** : On collecte des données sur la température et la consommation d’électricité sur plusieurs jours et on trace ces points sur un graphique.
3. **Ligne droite** : On trace une ligne droite qui passe **le plus près possible de tous ces points**. Cette ligne montre comment la consommation d’électricité change en fonction de la température.
**Prédiction** : Une fois la ligne tracée, on peut prédire la consommation d’électricité pour une certaine température.

{{% notice note %}}
La variable **dépendante** = la **variable cible**, c'est-à-dire la variable à prédire.
Les variables **indépendantes** = les **variables d'entrée**. 
{{% /notice %}}

## Les limites de la régression linéaire

La régression linéaire est un outil puissant, mais elle a ses limites. Voici quelques-unes des principales :

1. **Relation linéaire** : La régression linéaire suppose que la relation entre les variables est linéaire (une ligne droite). Si la relation est courbe ou plus complexe, la régression linéaire ne sera pas appropriée.

Exemple:

![courbe quadratique](../courbe.png?width=35vw)

Une relation quadratique entre la variable cible et une variable d'entrée `y = a∗x^2`
 + du bruit comme sur le graphe ci-dessus. On voit bien que la droite de la régression linéaire n'explique en rien la relation entre la variable d'entrée et la cible.

2. **Sensibilité aux valeurs aberrantes** : Les valeurs aberrantes (points de données très éloignés des autres) peuvent avoir un impact important sur la ligne de régression, la rendant moins précise.

3. **Multicolinéarité** : Si on utilises plusieurs variables indépendantes (régression linéaire multiple), ces variables ne doivent pas être fortement corrélées entre elles. Sinon, cela peut compliquer l'interprétation des résultats.

4. **Hypothèses strictes** : La régression linéaire repose sur plusieurs hypothèses, comme la normalité des erreurs, l'homoscédasticité (variance constante des erreurs) et l'indépendance des erreurs. Si ces hypothèses ne sont pas respectées, les résultats peuvent être biaisés.

5. **Prédiction limitée** : La régression linéaire est moins efficace pour prédire des valeurs en dehors de la plage des données observées (extrapolation).

6. **Causalité** : La régression linéaire montre une association entre les variables, mais elle ne prouve pas la causalité. Par exemple, même si la température et la consommation d'électricité sont liées, cela ne signifie pas que l'une cause l'autre.

## Quelques informations permettant d'interpréter une droite de régression linéaire

Interpréter une droite de régression linéaire est une compétence essentielle en analyse de données. Voici un guide simple pour comprendre cette interprétation :

1. **Pente de la droite** :
   - La pente indique la direction et la force de la relation entre les deux variables. Si la pente est positive, cela signifie que lorsque la variable indépendante (x) augmente, la variable dépendante (y) augmente également. Si la pente est négative, y diminue lorsque x augmente.

2. **Ordonnée à l'origine** :
   - L'ordonnée à l'origine est le point où la droite de régression croise l'axe des y. Elle représente la valeur de y lorsque x est égal à zéro. Bien que cette valeur puisse ne pas toujours avoir une signification pratique, elle est importante pour définir la droite.

3. **Visualisation** :
   - En traçant la droite de régression sur un graphique, on peut visualiser comment les points de données se répartissent par rapport à cette droite. Si les points sont proches de la droite, cela indique une bonne adéquation du modèle. Si les points sont dispersés, cela peut indiquer que d'autres facteurs influencent la variable dépendante.


## Régression linéaire avec Python et sa représentation graphique

En bref, voici les étapes à accomplir:

1. Importer les bibliothèques nécessaires (Pandas, NumPy, Matplotlib et scikit-learn), pour utiliser les fonctions et outils de chaque bibliothèque.
	- **Pandas**: pour extraire les données du fichier .csv
	- **NumPy**: pour créer la droite de régression 
	- **Matplotlib**: pour tracer le graphique complet
2. Charger et extraire les données du fichier .csv dans un format que Python peut manipuler et pour s'assurer qu'il existe une relation linéaire entre les variables. 
3. Créer et ajuster le modèle de régression linéaire, pour trouver la meilleure ligne droite qui correspond aux données.
4. Prédire les valeurs de la variable en y à partir des valeurs en x, pour obtenir les valeurs de la ligne de régression.
5. Tracer les points de données et la ligne de régression, pour visualiser les données et la ligne de régression sur un graphique.
6. Ajouter l’équation de la ligne de régression sur le graphique.
7. Ajouter des étiquettes, le titre et la légende du graphique.
8. Afficher le graphique.