+++
title = 'Formatage des chaines'
weight = 1
+++

![Formatage chaines](./formatage-chaines.jpeg?width=20vw)

## La méthode str.format()

```python
nom = "Philippe"
age = 30
print("Je m'appelle {} et j'ai {} ans.".format(nom, age))
```

**Explication**:

- `{}` est un espace réservé pour une valeur qui sera insérée dans la chaîne de caractères.
- La méthode `format(nom, age)` remplace les accolades `{}` par les valeurs des variables `nom` et `age` respectivement.

Donc, lorsque ce code est exécuté, il affiche :

```plaintext
Je m'appelle Philippe et j'ai 30 ans.
```

- Cette méthode est très flexible et permet d’insérer plusieurs variables dans une chaîne de caractères de manière claire et lisible.

##  L'opérateur % 

**Exemple**:

```python
nom = "Nathalie"
age = 30
print("Je m'appelle %s et j'ai %d ans." % (nom, age))
```

**Explication**:

- `%s` est un espace réservé pour une chaîne de caractères (string).
- `%d` est un espace réservé pour un entier (integer).

- La partie ("Je m'appelle %s et j'ai %d ans." % (nom, age)) signifie que Python va remplacer `%s` par la valeur de la variable `nom` et `%d` par la valeur de la variable `age`.

Donc, lorsque ce code est exécuté, il affiche :

```plaintext
Je m'appelle Nathalie et j'ai 30 ans.
```
