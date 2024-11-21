+++
title = "NumPy"
weight = 130
+++

![NumPy](../numpy.jpg?width=18vw)


## Qu'est-ce que NumPy?

NumPy (*Numerical Python*) est une bibliothèque pour le langage Python, ajoutant le support de grands tableaux (listes) ainsi qu’une large collection de fonctions mathématiques de haut niveau pour les opérer.
C’est une bibliothèque essentielle pour la science des données.

{{% notice note %}}
Un des intérêts de NumPy est qu’il travail directement avec les tableaux (listes) et gère lui même les boucles nécessaire pour faire les calculs. Ca allège le code et il s’exécute plus rapidement.
{{% /notice %}}

NumPy est un module Python qui s’importe comme tous les autres. De ce fait, il nous suffit d’écrire et d’exécuter le code ci-dessous dans une cellule sur Jupyter Notebook afin d’importer cette librairie.

```python
import numpy as np
```

Pour vérifier que NumPy est bien installé à votre environnement :

```python
# Version de Numpy
np.__version__
```

Vous devriez voir la version installée sous la forme de 1.XX.X. Si tel n'est pas le cas, il faudra installer NumPy comme ceci :

```plaintext
pip install numpy
```

## Les tableaux NumPy

Avec NumPy, il existe un équivalent plus puissant des listes python, les `ndarray`. Comme les listes, il est possible d’accéder aux valeurs du tableau avec des `[]`, il est également possible de faire des tableau a plusieurs dimensions.

Ces tableaux sont généralement construit à partir de liste python.

```python
nd_array = np.array([10,20,30,40,50,60])

print(f"{nd_array[3]}")
print(f"{nd_array[3:5]}, {type(nd_array[3:5])}")
```python

```plaintext
40
[40 50], <class 'numpy.ndarray'>
```

## Accès indicé d'un tableau NumPy

Comme tous tableaux, il est possible d'accéder aux éléments à l'aide des indexes.

```python
tableau = np.arange(-10, 10, 0.5)

# Accès au premier élément
premier = tableau[0] # Affiche -10
tableau[2] # Affiche 10
```

## Valeurs uniques d'un tableau NumPy

La fonction `unique()` permet de retourner les valeurs uniques d'un tableau NumPy et de compter le nombre d'occurrences de ces valeurs.

```python
tableau = np.array([1, 1, 2, 3, 3, 3, 1, 5, 6, 2]
np.unique(tableau, return_counts=True)
```

```plaintext
(array([1, 2, 3, 5, 6]), array([3, 2, 3, 1, 1], dtype=int64))
```

## Conversion des listes en tableau NumPy

Il est possible de convertir une liste python en `ndarray` et inversement:

```python
liste = [10,20,30,40,50,60]
nd_array = np.array(liste)
conversion_liste = nd_array.tolist()

print(type(liste))
print(type(nd_array))
print(type(conversion_liste))
```

```plaintext
<class 'list'>
<class 'numpy.ndarray'>
<class 'list'>
```

## Conversion d'un DataFrame en tableau NumPy

```python
df = pd.DataFrame(donnees)

# Extraction des données d'une colonne du DataFrame, et création d'un tableau Numpy
tableau = df['colonne'].to_numpy()
```

## Filtrer des données d'un DataFrame et convertir en tableau NumPy

```python
df = pd.DataFrame(donnees)

# Filtre sur une colonne du DataFrame et création d'un tableau Numpy
tableau = df['colonne' > valeur]['colonne'].to_numpy()
```

## Les fonctions mathématiques

Voici un ensemble de fonctions mathématique disponibles dans NumPy:

| Fonction  | Inverse    | Description                                      |
|-----------|------------|--------------------------------------------------|
| `np.sin()`| `np.asin()`| Fonction sinus et son inverse par éléments       |
| `np.cos()`| `np.acos()`| Fonction cosinus et son inverse par éléments     |
| `np.tan()`| `np.atan()`| Fonction tangente et son inverse par éléments    |
| `np.exp()`| `np.log()` | Fonction exponentielle et logarithmique par éléments |

Pour une version plus exhaustive, voir la [documentation officielle](https://numpy.org/doc/stable/reference/routines.math.html)

On peut utiliser ces fonctions comme vous le feriez sur votre calculatrice, c’est à dire en donnant une valeur, on obtient en retour le résultat de cette fonction.

```python
print(round(np.sin(0),2))
print(round(np.cos(0),2))
print(round(np.sin(np.pi),2))
print(round(np.cos(np.pi),2))
```

```plaintext
0.0
1.0
0.0
-1.0
```

On peut également fournir un tableau de valeur, alors la fonction va calculer le résultat de chacun des élément du tableau.

```python
x = np.linspace(-10, 10, 50)
y_sin = np.sin(x)
print(y_sin)
```

```plaintext
[ 0.54402111  0.16628279 -0.23877532 -0.60460332 -0.8710967  -0.99447137
 -0.9544572  -0.75762842 -0.43632343 -0.04333173  0.35677924  0.6982724
  0.92504137  0.99982867  0.91034694  0.67129779  0.32195632 -0.08028167
 -0.46932961 -0.78126802 -0.96484631 -0.98990308 -0.85232157 -0.57470604
 -0.20266794  0.20266794  0.57470604  0.85232157  0.98990308  0.96484631
  0.78126802  0.46932961  0.08028167 -0.32195632 -0.67129779 -0.91034694
 -0.99982867 -0.92504137 -0.6982724  -0.35677924  0.04333173  0.43632343
  0.75762842  0.9544572   0.99447137  0.8710967   0.60460332  0.23877532
 -0.16628279 -0.54402111]
```

Avec ces valeurs, on a tout ce qu’il faut pour tracer la fonction :

```python
x = np.linspace(-10, 10, 100)
y_sin = np.sin(x)

plt.plot(x,y_sin, color="b", label="sin")

plt.legend(loc="upper right")
plt.show()
```

![Sinus](../sinus.jpg?width=30vw)

## Fonctions statistiques pour les tableaux

Voici quelques fonctions statistiques de NumPy:

```python
liste = [10,20,30,40,50,60]
nd_array = np.array([10,20,30,40,50,60])

print(f"Moyenne: {np.mean(liste)}")
print(f"Somme: {np.sum(liste)}")
print(f"Écart-type: {np.std(liste)}")
print(f"Produit: {np.prod(nd_array)}")
print(f"Valeur minimum: {np.min(liste)}")
print(f"Valeur maximum: {np.max(nd_array)}")
```
```plaintext
Moyenne: 35.0
Somme: 210
Écart-type: 17.07825127659933
Produit: 720000000
Valeur minimum: 10
Valeur maximum: 60
```

Remarquez que ces fonctions peuvent prendre en argument des `ndarray` NumPy ou des `list` python.

## Les opérateurs avec un tableau NumPy

Contrairement aux listes les opérations entre un tableau et une valeur numérique sont possibles.

Dans ce cas, l’opération est faite élément par élément du tableau.

```python
# ajoute 10 a tous les elements du tableau
nd_array_2 = nd_array + 10
print(nd_array_2)

# multiplie par 10 tous les éléments du tableau
nd_array_3 = nd_array * 10
print(nd_array_3)

# additionne 2 tableaux élément par élément
nd_array_4 = nd_array + nd_array
print(nd_array_4)
```

```plaintext
[20 30 40 50 60 70]
[100 200 300 400 500 600]
[ 20  40  60  80 100 120]
```

{{% notice style=waring title=Attention %}}
Si vous faites ces opérations avec une liste python, vous obtiendrez une erreur, votre code ne s’exécutera pas.
{{% /notice  %}}


## Génération de tableau NumPy

Il y a de nombreux cas de figure où peut avoir besoin de tableau remplie de valeurs suivant des propriétés précises.

On a vu avec les boucles l’utilité de générer un tableau de valeur pour accéder à une liste par ses indexes, grâce à la fonction `range()`. Pour les tableaux NumPy, il y a les fonctions `arrange()` et `linespace()`.

### La fonction np.arange()

C’est l’équivalent de la fonction python de base `range()`. Ses arguments sont les mêmes: minimum, maximum et pas. Mais elle retourne un `ndarray`.

```python
tableau = np.arange(-10, 10, 0.5)
print(type(tableau))
print(tableau)
```

```plaintext
<class 'numpy.ndarray'>
[-10.   -9.5  -9.   -8.5  -8.   -7.5  -7.   -6.5  -6.   -5.5  -5.   -4.5
  -4.   -3.5  -3.   -2.5  -2.   -1.5  -1.   -0.5   0.    0.5   1.    1.5
   2.    2.5   3.    3.5   4.    4.5   5.    5.5   6.    6.5   7.    7.5
   8.    8.5   9.    9.5]
```

### La fonction np.linspace()

La fonction `linspace()` génère un tableau de valeur entre 2 bornes, mais ici la taille du tableau est précisé en paramètre et le pas est calculé automatiquement.

Contrairement à `arange()` qui a un pas précisé en paramètre, mais la taille du tableau est déterminée en fonction du pas.

```python
tableau = np.linspace(-10, 10, 50)
print(type(tableau))
print(tableau)
```

```plaintext
<class 'numpy.ndarray'>
[-10.          -9.59183673  -9.18367347  -8.7755102   -8.36734694
  -7.95918367  -7.55102041  -7.14285714  -6.73469388  -6.32653061
  -5.91836735  -5.51020408  -5.10204082  -4.69387755  -4.28571429
  -3.87755102  -3.46938776  -3.06122449  -2.65306122  -2.24489796
  -1.83673469  -1.42857143  -1.02040816  -0.6122449   -0.20408163
   0.20408163   0.6122449    1.02040816   1.42857143   1.83673469
   2.24489796   2.65306122   3.06122449   3.46938776   3.87755102
   4.28571429   4.69387755   5.10204082   5.51020408   5.91836735
   6.32653061   6.73469388   7.14285714   7.55102041   7.95918367
   8.36734694   8.7755102    9.18367347   9.59183673  10.        ]
```

## Les polynômes

NumPy offre une fonction pour utiliser des polynômes de degré n, la fonction `np.poly1d()`. Elle prend un paramètre un tableau qui contient les coefficients du polynôme par ordre décroissant de puissance.

Pour générer le polynôme suivant dans NumPy:

$$ y = x^2 + x - 2 $$

Il faut utiliser la liste de coéfficients [1, 1, -2], on obtient alors le code suivant:

```python
polynome = np.poly1d([1, 1, -2])
print(polynome)
print(f"Les racines de ce polynomes sont: {polynome.r}")
print(f"La valeur de ce polynomes quand x=10 est: {polynome(10)}")
```

```plaintext
   2
1 x + 1 x - 2
Les racines de ce polynomes sont: [-2.  1.]
La valeur de ce polynomes quand x=10 est: 108
```

Une fois le polynôme définie, on peut l’utiliser de la même manière que les fonctions mathématiques vues ci-dessus.

```python
x = np.linspace(-10, 10, 100)
y = polynome(x)

plt.plot(x, y)
plt.savefig('polynome.jpg', dpi=150, bbox_inches="tight")
plt.show()
```

![Polynome](../polynome.jpg?width=30vw)


## Les coefficient de corrélation

La fonction `corrcoef()` de NumPy calcule le coefficient de corrélation de Pearson entre deux ensembles de données. Ce coefficient mesure la force et la direction de la relation linéaire entre deux variables.

### Comment utiliser corrcoef() ?

1. **Préparer les données** : Vous avez besoin de deux ensembles de données `x`, `y` sous forme de tableaux NumPy.
2. **Calculer le coefficient de corrélation** : Utilisez `np.corrcoef()` pour calculer le coefficient de corrélation. Cette fonction retourne une matrice de corrélation.

```python
matrice_correlation = np.corrcoef(x, y)
```
3. **Interpréter les résultats** : La matrice de corrélation est une matrice 2x2 où les valeurs diagonales sont toujours 1 (car une variable est parfaitement corrélée avec elle-même) et les valeurs hors diagonale sont les coefficients de corrélation entre les variables.

```python
print(matrice_correlation)
```

Par exemple, si `matrice_correlation` est :

```plaintext
[[1.         0.8       ]
 [0.8        1.        ]]
```

Cela signifie que le coefficient de corrélation entre `x` et `y` est 0.8, indiquant une forte corrélation positive.

### Interprétation du coefficient de corrélation :

- **1** : Corrélation parfaite positive
- **0** : Aucune corrélation
- **-1** : Corrélation parfaite négative
- **Entre 0 et 1** : Corrélation positive (plus proche de 1, plus forte est la corrélation)
- **Entre 0 et -1** : Corrélation négative (plus proche de -1, plus forte est la corrélation)

## Liste non exhaustive de fonctions

NumPy est doté d'une grande quantité de fonction permettant de gérer des tableaux. Il est aussi possible de faire des calculs mathématiques tel que le calcul de la moyenne, la médiane, l'écart type etc...

| Fonction/Méthode      | Description                                                                  | Exemple d'utilisation                          |
|-----------------------|------------------------------------------------------------------------------|------------------------------------------------|
| `np.array()`          | Crée un tableau NumPy à partir d'une liste ou d'une séquence.                | `arr = np.array([1, 2, 3])`                    |
| `np.arange()`         | Génère un tableau contenant une séquence d'entiers.                          | `arr = np.arange(0, 10, 2)`                    |
| `np.linspace()`       | Génère un tableau de nombres espacés uniformément sur un intervalle spécifié.| `arr = np.linspace(0, 1, 5)`                   |
| `np.zeros()`          | Crée un tableau de zéros.                                                    | `arr = np.zeros((2, 3))`                       |
| `np.ones()`           | Crée un tableau de uns.                                                      | `arr = np.ones((2, 3))`                        |
| `np.random.rand()`    | Génère un tableau de nombres aléatoires uniformément distribués entre 0 et 1.| `arr = np.random.rand(2, 3)`                   |
| `np.random.randn()`   | Génère un tableau de nombres aléatoires suivant une distribution normale.    | `arr = np.random.randn(2, 3)`                  |
| `np.unique()`         | Renvoie les éléments uniques dans un nouveau tableau trié                    | `arr = np.unique([1, 2, 1, 1, 3, 3, 1])`       |
| `np.sort()`           | Tri le tableau                                                               | `np.sort(arr)`                                 |
| `np.sum()`            | Calcule la somme des éléments d'un tableau.                                  | `total = np.sum(arr)`                          |
| `np.mean()`           | Calcule la moyenne des éléments d'un tableau.                                | `mean = np.mean(arr)`                          |
| `np.median()`         | Calcule la médianne des éléments d'un tableau.                               | `mediane = np.median(arr)`                     |
| `np.std()`            | Calcule l'écart-type des éléments d'un tableau.                              | `ecart_type = np.std(arr)`                     |
| `np.var()`            | Calcule la variance des éléments d'un tableau.                               | `variance = np.var(arr)`                       |
| `np.size()`           | Renvoie le nombre d'éléments dans le tableau.                                | `taille = np.size(arr)`                        |
| `np.ndim()`           | Renvoie le nombre de dimension du tableau.                                   | `dimension = np.ndim(arr)`                     |
| `np.max()`            | Renvoie la valeur maximale d'un tableau.                                     | `max_val = np.max(arr)`                        |
| `np.min()`            | Renvoie la valeur minimale d'un tableau.                                     | `min_val = np.min(arr)`                        |
| `np.argmax()`         | Renvoie l'indice de la valeur maximale d'un tableau.                         | `index_max = np.argmax(arr)`                   |
| `np.argmin()`         | Renvoie l'indice de la valeur minimale d'un tableau.                         | `index_min = np.argmin(arr)`                   |
| `np.shape()`          | Renvoie la forme du tableau.                                                 | `forme = np.shape(arr, (3, 2))`                |
| `np.reshape()`        | Change la forme d'un tableau sans changer ses données.                       | `deforme = np.reshape(arr, (3, 2))`            |
| `np.transpose()`      | Transpose un tableau (inverse les axes).                                     | `transpose = np.transpose(arr)`                |
| `np.dot()`            | Calcule le produit matriciel de deux tableaux.                               | `produit = np.dot(arr1, arr2)`                 |
| `np.corrcoef()`       | Calcule le coefficient de corrélation entre deux ensembles de données.       | `matrice_correlation = np.corrcoef(x, y)`      |
| `np.polyfit()`        | Ajuste un polynôme à des données.                                            | `coefficients = np.polyfit(x, y, 2)`           |


Pour plus de fonctions : [Site officiel NumPy](https://numpy.org/doc/stable/index.html "Numpy").