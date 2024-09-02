+++
title = "Variables et types de données"
weight = 22
+++

![Variable et types de données](../variable.jpg?width=25vw).

## Définition des variables

{{% notice style=info title=Définition %}}
Une **variable** est une zone de la mémoire de l'ordinateur dans laquelle une valeur est stockée. Une variable est définie par un nom et sa valeur.
Vous pouvez imaginer une variable comme une boîte dans laquelle vous pouvez mettre des choses, comme des nombres, du texte, des listes, etc..
{{% /notice %}}

### Comment nommer une variable ?

Pour garantir la lisibilité et la maintenabilité de votre code, il est essentiel de suivre certaines règles de nommage des variables en Python. Voici les principales règles à respecter :

1. **Utiliser des noms significatifs** :
   - Choisissez des noms de variables qui décrivent clairement leur contenu ou leur rôle. Par exemple, `age`, `nom_utilisateur`, ou `total_facture` sont des noms explicites.

2. **Commencer par une lettre ou un underscore** :
   - Les noms de variables doivent commencer par une lettre (a-z, A-Z) ou un underscore (_). Par exemple, `nom`, `_compteur`.

3. **Utiliser des lettres, des chiffres et des underscores** :
   - Après le premier caractère, vous pouvez utiliser des lettres, des chiffres (0-9) et des underscores. Par exemple, `compteur1`, `total_facture_2024`.

4. **Respecter la casse** :
   - Python est sensible à la casse, ce qui signifie que `variable`, `Variable` et `VARIABLE` sont trois variables différentes. Utilisez une convention cohérente, comme le snake_case (mots séparés par des underscores) pour les variables : `nombre_utilisateurs`.

5. **Éviter les mots réservés** :
   - Ne pas utiliser les mots réservés de Python comme noms de variables. Par exemple, `print`, `class`, `for`, `if` sont des mots réservés et ne peuvent pas être utilisés comme noms de variables.

### Exemples de bonnes et de mauvaises pratiques

```python
# Bonnes pratiques
age_utilisateur
nom_utilisateur
total_facture

# Mauvaises pratiques
1valise			# Commence par un chiffre
total-facture		# Utilise un tiret au lieu d'un underscore
class			# Utilise un mot réservé 'class'
point equivalence	# Contient un espace
opposé			# Contient une lettre accentuée
```

## Les commentaires

Les commentaires commencent par le symbole `#` (dièse).

Python ignore les commentaires, c’est-à-dire qu’il ne les exécute pas.

Les commentaires sont utilisés pour :

1. Expliquer le code
2. Rendre le code plus lisible
3. Empêcher l’exécution lors de tests du code

## Déclaration et assignation

Le symbole `=` est appelé **opérateur d'affectation**. Il permet d'assigner une valeur à une variable. 

{{% notice style=warning title=Attention %}}
Cet opérateur s'utilise toujours de la droite vers la gauche. Par exemple, dans l'instruction x = 5, Python attribue la valeur située à droite (ici, 5) à la variable située à gauche (ici, x).
{{% /notice %}}

```python
variable = valeur
```

Par exemple:
```python
x = 5
nom = "Alice"
prix = 19.99
```

### Assignation multiple

Python permet l’assignation multiple, où vous pouvez assigner des valeurs à plusieurs variables en une seule ligne.

```python
a, b, c = 1, 2, 3
```

Vous pouvez également assigner la même valeur à plusieurs variables simultanément.

```python
x = y = z = 0
```

## Types de variables

En programmation, il existe plusieurs types de variables :
- les nombres **entiers** (int)
- les nombres à virgules dit les **flottants** (float)
- les **chaînes de caractères** [(string)](../../Semaine6/chaines_caracteres.md)
- les **booléens** (bool)
- les **listes** [(list)](../../Semaine6/listes.md)
- les **dictionnaires** [(dict)](../../Semaine6/structures_donnees.md/)

Python est un langage à typage dynamique, ce qui signifie que vous n’avez pas besoin de spécifier le type de données lors de la déclaration d’une variable. Le type de la variable est déterminé automatiquement en fonction de la valeur assignée.

```python
age = 30             # type int
nom = "Robert"       # type str
temperature = 36.6   # type float
est_present = True   # type bool
```

La méthode `type()` est une fonction intégrée en Python qui permet de déterminer le type d’une variable. 

Pour utiliser `type()`, il suffit de mettre le nom de la variable ciblée dans les parenthèses. Par exemple :

```python
age = 30
print(type(age))    # Affiche <class 'int'>

nom = "Robert"
print(type(nom))    # Affiche <class 'str'> 

temperature = 36.6
print(type(temperature))     # Affiche <class 'float'>

est_present = True 
print(type(est_present))  # Affiche <class 'bool'>
```

### Le transtypage (_Casting_) ou la conversion de types

- L'opération de *transtypage* consiste à convertir une variable en un type différent de son type original. 
- Pour ce faire, il existe différentes méthodes selon le type de données désiré.

	- `int()`: Converti en nombre entier.
	- `float()`: Converti en type flottant ou nombre à virgule.
	- `str()`: Converti en chaine de caractères.

**Exemple**:

```
x = 10  # entier
y = "20" # chaine

# y est changé en entier pour l'additionner à x
somme = x + int(y)
```
Ce code affichera 30

{{% notice note %}}
La fonction `int()` est couramment utilisée pour convertir un nombre flottant en un entier en le tronquant, c’est-à-dire en supprimant la partie décimale sans arrondir. Par exemple, int(9.9) renverra 9. Il est important de noter que `int()` ne fait que tronquer le nombre et ne l’arrondit pas. Pour arrondir un flottant à l’entier le plus proche, vous pouvez utiliser la fonction `round()`.
{{% /notice%}}

{{%notice style="warning" title="Attention"%}}
Dans le cas où vous essayez de modifier une variable de type chaîne de caractères vers un entier ou un flottant, une erreur surviendra car la conversion n'est pas possible.

Exemple :
```python
float("Valorant")
```
```plaintext
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[3], line 1
----> 1 float("Valorant")

ValueError: could not convert string to float: 'Valorant'
```
{{% /notice%}}

## Les chaines de caractères

Pour définir une chaîne de caractères, il faut l'entourer de guillemets (doubles `" "` ou simples `' '`) afin d'indiquer à Python le début et la fin de la chaîne de caractères.

**Exemples de chaines de caractères**

```Python
message_accueil = "Bonjour tout le monde!"
message = 'Comment allez-vous?'
```
Lorsqu’une chaine de caractères contient **plus de deux guillemets simples** ou **plus de deux guillemets doubles**, à l’exécution cela peut causer une **erreur de syntaxe** et **l'arrêt du programme**. comme dans l'exemple ci-dessous:

```python
message_guillemets_simples = 'Bonjour, comment allez vous aujourd'hui ?'
message_guillemets_doubles = "Bonjour, comment allez "vous ?"
print(message_guillemets_simples)
print(message_guillemets_doubles)
```

**Le résultat**

![Affichage guillemet en trop](../print_trop_guillemets.jpg?width=50vw "Affichage guillemet en trop").

{{% notice note %}}
**NB:** Remarquez l'absence de l'affichage du deuxième print
{{% /notice %}}

### Comment éviter ce problème ?

Il existe deux solutions:

1. **Mélanger les types de guillemets** : Utiliser les guillemets doubles pour encadrer la chaine de caractères et le guillemet simple dans sont usage naturel, comme dans le mot **aujourd'hui**.
2. Il faut **'échapper'** le guillemet qu'on veut qui s'affiche comme un guillemet.

L'échappement se fait en précédent le guillemet visé par une barre oblique inversée **\ (backslash)**. Comme dans l'exemple suivant:

```python
message_guillemets = "Bonjour, comment allez vous aujourd'hui ?"
message_guillemet_echappe = 'Bonjour, comment allez vous aujourd\'hui ?'
print(message_guillemets)
print(message_guillemet_echappe)
```
**Le résultat**

![Exemple chaines corrigées](../print_chaines_corrigees.jpg?width=50vw "Exemple chaines corrigées").

### La concaténation de chaines de caractères

La **concaténation** de chaînes en programmation c'est la combinaison de deux chaînes ou plus pour former une seule chaîne. 
En Python, cela se fait à l'aide de l'opérateur `+` et elle est simple :
- Vous prenez deux chaînes de caractères.
- Vous utilisez l'opérateur `+` pour les joindre.
- Python combine les chaînes pour en faire une seule.

**Exemple :**

```python
# Définir deux chaînes de caractères
chaine1 = "Bonjour, "
chaine2 = "monde !"

# Concaténer les chaînes
chaine_concatenee = chaine1 + chaine2

# Afficher la chaîne concaténée
print(chaine_concatenee)
```

**Résultat :**
```
Bonjour, monde !
```

{{% notice style=warning  title=Attention %}}
Types identiques : Seules les chaînes peuvent être concaténées entre elles. Si vous essayez de concaténer une chaîne avec un autre type de données (comme un entier ou un float), Python renverra une erreur.
Conversion nécessaire : Pour concaténer une chaîne avec un nombre, vous devez d'abord convertir le nombre en chaîne à l'aide de la fonction `str()`. 
{{% /notice %}}