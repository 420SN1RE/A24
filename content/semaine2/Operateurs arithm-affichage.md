+++
title = "Opérateurs arithmétiques et l'affichage"
weight = 23
+++

![Opérateurs et expressions](../expressions.jpg?width=25vw).

## Les opérateurs arithmétiques

Les opérateurs permettent d’effectuer des opérations sur des variables. 
En Python, il existe plusieurs types d’opérateurs :   
1. Arithmétiques.  
2. De comparaison.   
3. Logiques. 

{{% notice info %}}
Nous verrons les deux derniers types lors de l'études des structures conditionnelles.
Pour l'instant, concentrons nous sur les opérateurs arithmétiques.
{{% /notice %}}

Les **opérateurs arithmétiques** sont utilisés pour effectuer des calculs mathématiques courants.

Soient `a = 10` et `b = 3`

|Opération (opérateur)|Exemple|
|---------------------|-------|
|Addition (`+`)         |`a + b` donne 13|
|Soustraction (`-`)     |`a - b` donne 7|
|Multiplication (`*`)   |`a * b` donne 30|
|Division (`/`)         |`a / b` donne 3.3333...|
|Modulo (`%`)           |`a % b` donne 1|
|Exponentiation (`**`)  |`a ** b` donne 1000|
|Division entière (`//`)|`a // b` donne 3|

## Affichage des données

L'affichage des données se fait à l'aide de la méthode `print()`.

Voici quelques variables à afficher :

```python
# x est un entier
x = 5

# y est un flottant
y = 7.5

# salutations est une chaîne de caractères
salutations = "Bienvenue dans la faille de l'invocateur !"

# ulti_actif est un booléen qui aura pour valeur Vrai ou Faux (Faux dans notre exemple)
ulti_actif = False

```

Pour afficher le résultat de nos variables, rien de plus simple, il suffit de mettre le nom de la variable entre les parenthèses :

```python
# Utiliser la méthode print() pour afficher les résultats
print(x)
print(y)
print(salutations)
print(ulti_actif)

```

Lorsque vous exécuterez votre cellule, vous devriez voir le résultat suivant :

```plaintext
5
7.5
Bienvenue dans la faille de l'invocateur !
False
```

`print` permet d'afficher le contenu de plusieurs variables (quelque soit leur type) en les séparant par des virgules :

```python
age = 32
nom = "Jean"
print(nom, "a", age, "ans") # Affiche Jean a 32 ans
```

## Pause: 5 minutes

![Pause](../pause.jpg?width=25vw).

