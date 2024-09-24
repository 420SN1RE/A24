+++
title= "Erreurs avec les noms des variables"
weight= 1
+++

![Opérateurs](../erreur-variables.jpeg?width=20vw)

## Pourquoi bien nommer les choses ?

La raison est simple, **on passe plus de temps a lire du code qu'a l'écrire**, donc pour se simplifier la tâche de lecture du code, quel que soit le langage de programmation, il est important de bien nommer les différentes variables, méthodes etc.

## Conventions de nommage en python

En plus des règles liées au langage qui mèneront à un problème d'exécution (par exemple, un nom de variable ne doit pas commencer par des chiffres), il existe un nombre de convention concernant le nommage en python.

https://peps.python.org/pep-0008/#naming-conventions
| Type                         | Public               |
| ---------------------------- | -------------------- |
| Packages                     | `lower_with_under`   |
| Modules                      | `lower_with_under`   |
| Classes                      | `CapWords`           |
| Exceptions                   | `CapWords`           |
| Fonctions                    | `lower_with_under()` |
| Constantes Global / Class    | `CAPS_WITH_UNDER`    |
| Variables Global / Class     | `lower_with_under`   |
| Variables d'Instance         | `lower_with_under`   |
| Nom de Methode               | `lower_with_under()` |
| Paramètres Function / Method | `lower_with_under`   |
| Variables locales            | `lower_with_under`   |

## La logique de nommage

Bien nommer, va au dela des règles et convention du langage.
- Être le plus explicite possible, écrivez un nom complet. Préférez `minutes` à `min`.
- Si vous avez du mal à donner un nom à votre fonction, il y a probablement un problème de logique dans votre fonction.

## Variable non définie

L'erreur **"variable undefined"** en Python se manifeste généralement sous la forme d'une exception `NameError`. Cela se produit lorsque vous essayez d'utiliser une variable qui n'a pas été définie ou déclarée dans le contexte actuel. Voici quelques scénarios courants où cette erreur peut survenir et comment les éviter :

### 1. Utilisation d'une variable non définie

Si vous essayez d'accéder à une variable avant de l'avoir définie, Python ne saura pas de quoi il s'agit et lèvera une `NameError`.

```python
# Mauvais exemple
print(x)  # NameError: name 'x' is not defined
```

**Solution :** Assurez vous que la variable est définie avant de l'utiliser.

```python
# Bon exemple
x = 10
print(x)  # Affiche 10
```

### 2. Erreur de typographie

Une simple faute de frappe dans le nom de la variable peut entraîner une `NameError`.

```python
# Mauvais exemple
variable = 5
print(varible)  # NameError: name 'varible' is not defined
```

**Solution :** Vérifiez l'orthographe des noms de variables.

```python
# Bon exemple
variable = 5
print(variable)  # Affiche 5
```

### 3. Portée des variables

Les variables définies à l'intérieur d'une fonction ne sont pas accessibles en dehors de cette fonction.

```python
def ma_fonction():
    y = 20

ma_fonction()
print(y)  # NameError: name 'y' is not defined
```

**Solution :** Si vous avez besoin d'utiliser une variable en dehors de la fonction, vous devez la retourner ou la définir comme variable globale (ce qui est généralement déconseillé).

```python
def ma_fonction():
    y = 20
    return y

y = ma_fonction()
print(y)  # Affiche 20
```

### 4. Variables locales et globales

Confondre les variables locales et globales peut également causer des `NameError`.

```python
z = 30

def autre_fonction():
    print(z)  # Fonctionne si z est global

autre_fonction()
```

Cependant, si vous essayez de modifier une variable globale sans la déclarer comme telle, vous obtiendrez une erreur.

```python
z = 30

def encore_une_fonction():
    z += 1  # UnboundLocalError: local variable 'z' referenced before assignment

encore_une_fonction()
```

**Solution :** Utilisez le mot-clé `global` pour modifier une variable globale à l'intérieur d'une fonction.

```python
z = 30

def encore_une_fonction():
    global z
    z += 1

encore_une_fonction()
print(z)  # Affiche 31
```