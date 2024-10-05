+++
title = "Les fonctions récursives"
weight = 4
+++

![fonctions récursives](../fonction-recursive.jpeg?width=25vw)


## Qu'est-ce qu'une fonction récursive ?

Une fonction récursive est une fonction qui s'appelle elle-même. Pour qu'une fonction récursive fonctionne correctement, elle doit avoir deux éléments essentiels :
1. **Un cas de base** : Une condition qui arrête la récursion.
2. **Un appel récursif** : La fonction s'appelle elle-même avec des arguments modifiés.

## Exemple simple : La factorielle d'un nombre 

Calculer la factorielle d'un nombre est un exemple classique de récursion. La factorielle de `n` (notée `n!`) est le produit de tous les entiers de 1 à `n`.

Voici comment on peut définir la factorielle de manière récursive :
- La factorielle de 0 est 1 (cas de base).
- La factorielle de `n` est `n` multiplié par la factorielle de `n-1` (appel récursif).

```python
def factorielle(n):
    if n == 0:
        return 1  # Cas de base
    else:
        return n * factorielle(n - 1)  # Appel récursif

# Exemples d'utilisation
print(factorielle(5))  # Affiche 120
```

## Comment fonctionne la récursion ?

Pour comprendre comment fonctionne la récursion, examinons l'exemple de la factorielle de 3 (`3!`).

1. `factorielle(3)` appelle `factorielle(2)`.
2. `factorielle(2)` appelle `factorielle(1)`.
3. `factorielle(1)` appelle `factorielle(0)`.
4. `factorielle(0)` retourne 1 (cas de base).
5. `factorielle(1)` retourne `1 * 1 = 1`.
6. `factorielle(2)` retourne `2 * 1 = 2`.
7. `factorielle(3)` retourne `3 * 2 = 6`.

## Exemple : La suite de Fibonacci

La suite de Fibonacci est une autre application classique de la récursion. Chaque nombre de la suite est la somme des deux précédents.

```python
def fibonacci(n):
    if n <= 1:
        return n  # Cas de base
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Appel récursif

# Exemples d'utilisation
print(fibonacci(6))  # Affiche 8
```

## Avantages et inconvénients de la récursion

**Avantages :**
- **Simplicité** : Les fonctions récursives peuvent être plus simples et plus élégantes que leurs équivalents itératifs.
- **Décomposition naturelle** : Elles permettent de décomposer naturellement un problème en sous-problèmes similaires.

**Inconvénients :**
- **Performance** : Les fonctions récursives peuvent être moins efficaces en termes de temps et d'espace mémoire, surtout si elles ne sont pas optimisées.
- **Limite de récursion** : Python a une limite sur la profondeur de récursion, ce qui peut poser problème pour des entrées très grandes.
