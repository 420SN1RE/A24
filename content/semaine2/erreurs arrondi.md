+++
title = "Nombres flottants et erreurs d'arrondi"
weight = 24
+++

![Erreurs d'arrondi](../flottants.jpeg?width=25vw)


## Les nombres flottants 

{{% notice style=warning title=Attention %}}
En Python, c'est le point qui est utilisé comme séparateur décimal. Ainsi, 3.14 est un nombre reconnu comme un flottant, alors que 3,14 ne l'est pas.
{{% /notice %}}

### Les erreurs d'arrondi

Les erreurs d'arrondi sont un phénomène courant en Python. Elles surviennent principalement en raison de la manière dont les nombres à virgule flottante sont représentés en mémoire. Voici une explication détaillée :

1. **Représentation des nombres à virgule flottante** :
   - En Python, les nombres flottants sont représentés en binaire (série de 1 et de 0.
   - Certains nombres décimaux ne peuvent pas être représentés **exactement** en binaire, ce qui entraîne des approximations.

2. **Exemple d'erreur d'arrondi** :
   - Considérez l'exemple suivant :
     ```python
     print(0.1 + 0.2)
     ```
   - On pourrait s'attendre à ce que le résultat soit 0.3, mais en réalité, il affiche quelque chose comme 0.30000000000000004. Cela est dû à l'approximation binaire de 0.1 et 0.2.

3. **Conséquences des erreurs d'arrondi** :
   - Les erreurs d'arrondi peuvent entraîner des résultats inattendus dans les calculs, surtout lorsqu'ils sont accumulés sur de nombreuses opérations.
   - Elles peuvent également poser des problèmes dans les comparaisons de flottants. Par exemple :
     ```python
     # Est-ce que 0.1 + 0.2 est égal à 0.3?
     print(0.1 + 0.2 == 0.3)   # Affiche False (faux)
     ```

## Technique simple pour gérer les erreurs d'arrondi

**Utiliser la fonction `round()`** :

Vous pouvez utiliser la fonction `round()` pour arrondir les nombres à un certain nombre de décimales.

```python
print(round(0.1 + 0.2, 1))  # Affiche 0.3
```

{{% notice note %}}
La bibliothèque NumPy fourni d'autres méthodes permettant de contrer les erreurs d'arrondi avec les nombres flottants. Nous les verrons lors du cours de la semaine 13.
{{% /notice %}}

## Notation scientifique

On peut écrire des nombres très grands ou très petits avec des puissances de 10 en utilisant le symbole `e` :

```python
nombre1 = 1e6 # 1000000.0
nombre2 = 3.12e-3 # 0.00312
```
