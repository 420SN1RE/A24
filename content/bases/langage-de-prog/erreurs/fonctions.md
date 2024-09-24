+++
title = "Erreurs avec les fonctions"
weight = 8
+++

![erreurs fonctions](../erreur-fonctions.jpeg?width=20vw)

Les fonctions sont des blocs de code essentiels en Python, mais leur utilisation peut parfois entraîner des erreurs, surtout pour les débutants. Voici un aperçu des erreurs les plus courantes et des conseils pour les éviter.

## 1. Oublier de définir la fonction avant de l'appeler

En Python, une fonction doit être définie avant d'être appelée. Si vous essayez d'appeler une fonction avant sa définition, vous obtiendrez une erreur `NameError`.

```python
# Mauvais exemple
resultat = addition(5, 3)

def addition(a, b):
    return a + b
```

**Solution :** Toujours définir la fonction avant de l'appeler.

```python
# Bon exemple
def addition(a, b):
    return a + b

resultat = addition(5, 3)
```

## 2. Mauvaise utilisation des arguments

Les erreurs liées aux arguments incluent l'oubli de passer les arguments nécessaires ou le passage d'un nombre incorrect d'arguments.

```python
def addition(a, b):
    return a + b

# Mauvais exemple
resultat = addition(5)  # TypeError: missing 1 required positional argument: 'b'
```

**Solution :** Vérifiez toujours que vous passez le bon nombre d'arguments.

```python
# Bon exemple
resultat = addition(5, 3)
```

## 3. Utilisation incorrecte des variables globales et locales

Confondre les variables globales et locales peut entraîner des comportements inattendus.

```python
a = 10

def addition(b):
    return a + b

# Mauvais exemple
print(addition(5))  # Fonctionne, mais peut être source de confusion
```

**Solution :** Utilisez des variables locales autant que possible et évitez de modifier les variables globales à l'intérieur des fonctions.

```python
def addition(a, b):
    return a + b

a = 10
print(addition(a, 5))
```

## 4. Oublier de retourner une valeur

Une fonction qui ne retourne pas explicitement une valeur retourne `None` par défaut.

```python
def addition(a, b):
    somme = a + b

# Mauvais exemple
resultat = addition(5, 3)
print(resultat)  # Affiche None
```

**Solution :** Assurez-vous de retourner une valeur si nécessaire.

```python
# Bon exemple
def addition(a, b):
    return a + b

resultat = addition(5, 3)
print(resultat)  # Affiche 8
```

## 5. Ne pas gérer les exceptions

Les fonctions peuvent échouer pour diverses raisons, et ne pas gérer ces exceptions peut rendre le débogage difficile.

```python
def division(a, b):
    return a / b

# Mauvais exemple
resultat = division(5, 0)  # ZeroDivisionError: division by zero
```

**Solution :** Utilisez des blocs `try` et `except` pour gérer les exceptions.

```python
# Bon exemple
def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erreur : division par zéro"

resultat = division(5, 0)
print(resultat)  # Affiche "Erreur : division par zéro"
```
