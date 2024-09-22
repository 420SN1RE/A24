+++
title = "Python: La base"
weight = 71
+++


## Les variables et les types de données

- On utilise des variables en programmation pour **stocker des informations** que l'on peut réutiliser et manipuler plus tard au lieu d'écrire à nouveau la valeur.

### Les types des variables et les transtypage

- Python supporte plusieurs types de données de base. Pour l'instant nous avons vu:

```python
nombre_entier = 15	# int
nombre_flottant = 15.0	# float
chaine_caracteres = "Je suis une chaine de caractères" 	# str
chaine_caracteres = 'Je suis aussi une chaine de caractères'	# str
valeur_booleenne = True	# bool
autre_valeur_booleenne = False	# bool
une_liste = [1, 2, 3, 4, 5]	# list
Une_autre_liste = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]	# list
```

- **Transtypage** : C'est la conversion d'un type de données à un autre. Par exemple, convertir une chaîne en entier avec `int("123")` ou un entier en chaîne avec `str(123)`.


### Utilisation de variables

- Avant d'utiliser une variable, il faut la **déclarer**, c'est-à-dire la nommer et lui donner une valeur.
- Le nom d'une variable doit respecter certains critères:
	- Ils doivent commencer par une lettre ou un underscore (_), suivis de lettres, chiffres ou underscores. 
	- Ils sont sensibles à la casse (`age` et `Age` sont différents).
	- Ils ne peuvent contenir ni espaces, ni lettres accentuées.

{{% notice style=warning title=Attention %}}
Si  vous oubliez de déclarer une variable avant de l'utiliser, ou si vous vous trompez en écrivant son nom, cela causera l'erreur **`NameError`** comme dans l'exemple ci-dessous:
{{% /notice %}}

```python
nombre1 = 5
nombre2 = 10

somme = nombre1 + nombre2 + nombre3

---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[20], line 4
      1 nombre1 = 5
      2 nombre2 = 10
----> 4 somme = nombre1 + nombre2 + nombre3

NameError: name 'nombre3' is not defined

```

## Les commentaires

- Les commentaires sont des lignes de texte dans le code qui sont ignorées par l’interpréteur. 
- Ils sont utilisés pour expliquer le code, pour désactiver des ligne de code ou pour laisser des notes aux programmeurs.
- Python utilise le symbole `#` suivi du texte du commentaire.

## Les opérateurs de division

- **Division classique (`/`)** : Cet opérateur divise deux nombres et retourne un résultat en **nombre flottant** (même si les deux nombres sont des entiers).
   
- **Division entière (`//`)** : Cet opérateur divise deux nombres et retourne le **quotient entier** de la division, en ignorant la partie décimale.
  
- **Modulo (`%`)** : Cet opérateur retourne le **reste** de la division de deux nombres.

## Les nombres flottants et les erreurs d'arrondi

- Les erreurs d’arrondi avec les nombres flottants en Python proviennent de la manière dont les nombres sont représentés en mémoire. Les nombres flottants sont stockés en binaire, ce qui peut entraîner des approximations pour certains nombres décimaux. Par conséquent, **des opérations arithmétiques** peuvent produire des résultats légèrement inexacts.
     
## Lire et traiter des données saisies au clavier

- Lorsqu'on veut utiliser une donnée qui est fournie au programme par l'utilisateur (saisie au clavier), la fonction `input()` est utilisée.
- input() permet de faire trois actions:
	1. Afficher un message pour guider l'utilisateur.
	1. Lire la donnée saisie au clavier par l'utilisateur.
	1. Stocker la donnée dans une variable.

**Exemple général :**

```python
variable = input("Texte pour guider l'utilisateur")
```

{{% notice style=warning title=Attention %}}
Les données lues avec `input()` sont **toujours de type chaîne de caractères**. Il est donc nécessaire de les convertir en un autre type, lorsqu'on souhaite les utiliser dans des calculs. 
{{% /notice %}}

## Les conditions et les instructions IF, ELIF, ELSE

### Les conditions

- Les conditions (ou tests) sont des **expressions booléennes**. Leurs résultats sont soit `True`, soit `False`.
- Elles s'expriment à l'aide d'opérateurs de comparaison (`==, !=, >, >=, <, <=`) et/ou des opérateurs logiques (`and, or, not`).

### Les instructions IF, ELIF, ELSE

  ```python
  if condition:
      # bloc de code si condition est vraie
  elif autre_condition:
      # bloc de code si autre_condition est vraie
  else:
      # bloc de code si aucune condition n'est vraie
  ```

{{% notice style=warning title=Attention %}}
- N'oubliez pas les `:` après les conditions du `if` et du `elif` et après le `else`.
- Après le `else`, il n'y a pas de condition.
- `elif` et `else` ne sont **pas toujours nécessaires**.
	- `elif`: Si d'autres conditions doivent être vérifiées lorsque la condition du `if` est `True`.
	- `else`: Les traitements à faire lorsque la condition du `if` est `False`.
{{% /notice %}}

## Les boucles WHILE et FOR

- **Boucle `while`** : Répète un bloc de code **tant qu'** une condition est vraie.
  ```python
  while condition:
      # bloc de code
  ```
- **Boucle `for`** : Itère sur une séquence (`range()`, liste, tuple, chaîne, etc.).
  ```python
  for element in sequence:
      # bloc de code
  ```

### Forcer l'arrêt (BREAK) ou forcer le saut (CONTINUE) d'une itération d'une boucle

- `break` : Interrompt la boucle.
- `continue` : Passe à l'itération suivante de la boucle.

{{% notice style=warning title=Attention %}}
- Avec la boucle `while` il faut explicitement modifier la variable de test pour la faire passer à la valeur de l'itération suivante.
- Avec la boucle `for`, ce changement se fait tout seul.
{{% /notice %}}

### Traitement lorsqu'une boucle se termine normalement

- **L'instruction `else` dans les boucles** permet d'exécuter un bloc de code, lorsque la boucle se termine normalement (sans `break`).

### L'indentation et la logique du code

{{% notice style=warning title=Attention %}}
- L’**indentation** est essentielle pour définir les blocs de code qui doivent être exécutés en fonction des conditions.
{{% /notice %}}

#### L'indentation et les instructions IF, ELIF et ELSE

```python
# Début de la structure
if condition1:
    # Code exécuté si condition1 est vraie
elif condition2:
    # Code exécuté si condition1 est fausse ET condition2 est vraie
else:
    # Code exécuté si aucune des conditions précédentes n'est vraie
# Extérieur de la structure conditionnelle
```

#### L'indentation et la boucle WHILE

```python
# Début de la boucle while
while condition:
    # Code exécuté tant que condition est vraie
    # Instructions pour modifier la variable de test pour éviter d'entrer dans une boucle infinie.
# Extérieur de la boucle while
```

#### L'indentation et la boucle FOR

```python
# Début de la boucle for
for element in sequence:
    # Code exécuté pour chaque élément dans la séquence
# Extérieur de la boucle for
```

#### L'indentation et les instructions BREAK et CONTINUE

```python
# Début de la boucle for
for element in sequence:
    if condition_arret:
        # Code exécuté si condition_arret est vraie
        break  # Sort de la boucle
    if condition_continuer:
        # Code exécuté si condition_continuer est vraie
        continue  # Passe à l'itération suivante
    # Code exécuté si aucune des conditions n'est vraie
# Extérieur de la boucle for
```

#### L'indentation et l'instruction ELSE dans les boucles

```python
# Début de la boucle for
for element in sequence:
    if condition_arret:
        # Code exécuté si condition_arret est vraie
        break  # Sort de la boucle
else:
    # Code exécuté si la boucle se termine normalement (sans break)
# Extérieur de la boucle for

# Début de la boucle while
while condition:
    # Code exécuté tant que condition est vraie
    if condition_arret:
        # Code exécuté si condition_arret est vraie
        break  # Sort de la boucle
else:
    # Code exécuté si la boucle se termine normalement (sans break)
# Extérieur de la boucle while
```

## La fonction print

- En Python, la fonction `print()` est utilisée pour afficher des messages ou des valeurs à l'écran. 

### Utilisation de base

```python
print("Bonjour le monde")  # Affiche : Bonjour le monde
```

### Affichage de plusieurs éléments

```python
print("Bonjour", "le", "monde")  # Affiche : Bonjour le monde
```

### L'argument `end`

- Par défaut, `print()` ajoute un saut de ligne (`\n`) à la fin de chaque appel. L'argument `end` permet de modifier ce comportement.

- **Exemple**: Utilisation de `end` pour créer une liste sur une seule ligne :

```python
for i in range(5):
    print(i, end=", ")  # Affiche : 0, 1, 2, 3, 4, 
```


