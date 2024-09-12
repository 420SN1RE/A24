+++
title = "Les instructions if else elif"
weight = 42
+++

![if elif else](../if.jpeg?width=25vw)

## Les tests

{{% notice style=info title=Definition %}}
Les **tests** sont très importants en programmation car ils permettent à l'ordinateur de prendre des décisions. Pour coder des tests, on utilise des **structures conditionnelles**.
{{% /notice %}}

## Les structures conditionnelles

Les structures conditionnelles sont essentielles pour la logique d'un programme. Elles permettent d'exécuter différentes actions en fonction de la valeur de certaines variables ou expressions. En Python, les structures conditionnelles sont `if` (Si), `elif` (Sinon Si), et `else` (Sinon). Voici comment elles fonctionnent :

- **if** : Utilisé pour vérifier si une condition est vraie. Si c'est le cas, le bloc de code associé est exécuté.
- **elif** : Utilisé pour vérifier une autre condition si la première est fausse.
- **else** : Utilisé pour exécuter un bloc de code si toutes les conditions précédentes sont fausses.

## Importance de l'indentation

{{% notice style=warning title=Attention %}}
L'indentation est très importante en Python. Elle indique quels blocs de code appartiennent à quelles conditions. 
{{% /notice %}}

Voici deux exemples pour illustrer cela :

```python
nombre = 5

if nombre == 5:
	print("Le test est vrai")
	print("car la variable nombre vaut", nombre)
```

Dans cet exemple, les deux `print` sont exécutés si `nombre` vaut 5.

```python
nombre = 7

if nombre == 5:
    print("Le test est vrai")
print("car la variable nombre vaut, nombre)
```

Dans cet exemple, l pemier`print` ne sera pas exécuté, car la condition `nombre == 5` est fausse (`False`).Le deuxième `print` sera toujours exécuté, peu importe la valeur de `nombre`.

## L'erreur ***IndentationError***

- Cette erreur se produit lorsque l'indentation de votre code n'est pas correcte. 

Voici quelques types courants d'IndentationError :

1. **IndentationError: expected an indented block** : Cette erreur survient lorsque Python s'attend à un bloc de code indenté, mais ne le trouve pas. Par exemple, après une instruction comme `if`, `for`, ou `while`, vous devez indenter le code qui suit.

**Exemple**:
```python
if True:
print("Ce code causera l'erreur IndentationError")
```

```python
Cell In[3],   line 2
    print("Ce code causera l'erreur IndentationError")
    ^
IndentationError: expected an indented block after 'if' statement on line 1
```

2. **IndentationError: unexpected indent** : Cette erreur se produit lorsque vous avez indenter une ligne de code de manière inattendue. Cela peut arriver si vous ajoutez une indentation supplémentaire là où elle n'est pas nécessaire.

**Exemple**:
```python
def my_function():
    print("Hello, world!")
        print("Ce code causera l'erreur IndentationError")
```

```python
  Cell In[4],   line 3
    print("Ce code causera l'erreur IndentationError")
    ^
IndentationError: unexpected indent
```

3. **IndentationError: unindent does not match any outer indentation level** : Cette erreur survient lorsque les niveaux d'indentation ne sont pas alignés correctement. Cela peut se produire si vous mélangez des espaces et des tabulations pour l'indentation.

**Exemple**:
```python
for i in range(5):
    print(i)
  print("Ce code causera l'erreur IndentationError")
```

```python
File <tokenize>:3
    print("Ce code causera l'erreur IndentationError")
    ^
IndentationError: unindent does not match any outer indentation level
```

## L'instruction IF

L'instruction `if` permet de tester une condition. Si la condition est vraie, le bloc de code associé est exécuté.

**Syntaxe générale :**

```python
if condition:
    # bloc de code à exécuter si la condition est vraie
```

**Exemple :**

```python
age = 18
if age >= 18:
    print("Vous êtes majeur.")
```
{{%notice style="note"%}}
Que se passe t-il si l'âge était inférieur à 18?
{{% /notice%}}

## L'instruction ELSE

L'instruction `else` s'utilise avec `if` pour définir un bloc de code à exécuter si la condition du `if` est fausse.

**Syntaxe :**

```python
if condition:
    # bloc de code à exécuter si la condition est vraie
else:
    # bloc de code à exécuter si la condition est fausse
```

**Exemple :**

```python
age = 16
if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")
```

{{%notice style="note"%}}
Comment faire pour pouvoir afficher un message différent selon différentes tranches d'âge adultes ?
{{% /notice%}}

## L'instruction ELIF

L'instruction `elif` permet de tester plusieurs conditions. Si la condition `if` est fausse, Python vérifie la condition `elif`. Si elle est vraie, le bloc de code associé est exécuté.

**Syntaxe :**

```python
if condition1:
    # bloc de code à exécuter si condition1 est vraie
elif condition2:
    # bloc de code à exécuter si condition1 est fausse et condition2 est vraie
else:
    # bloc de code à exécuter si toutes les conditions précédentes sont fausses
```

**Exemple :**

```python
age = 36
if 18 <= age <= 30:
    print("Vous êtes un jeune adulte")
elif 30 < age < 65:
    print("Avez-vous des enfants?")
elif age >= 65:
    print("Bonne retraite!")
else:
    print("Vous êtes mineur")
```
## Ordinogrammes des structures conditionnelles

### Les instructions IF et ELSE

![ordinogramme if-else](../if-else.png?width=35vw)

### L'instruction ELIF

![ordinogramme elif](../elif.png?width=35vw)

## Les opérateurs logiques dans les conditions

Il est possible de combiner plusieurs conditions avec les opérateurs logiques `and` (ET), `or` (OU), et `not` (NON).

**Exemple 1: Meilleure façon d'écrire le code de l'exemple de l'instruction ELIF**

```python
age = 36

if age >= 18 and age <= 30:
    print("Vous êtes un jeune adulte")
elif age > 30 and age < 65:
    print("Avez-vous des enfants?")
elif age >= 65:
    print("Bonne retraite!")
else:
    print("Vous êtes mineur")
```


**Exemple 2:**

```python
age = 20
permis = True

if age >= 18 and permis:
    print("Vous pouvez conduire.")
else:
    print("Vous ne pouvez pas conduire.")
```

## Pause : 5 minutes

![Pause](../pause.jpg?width=25vw)

Voyons maintenant comment tester les nombres flottants.