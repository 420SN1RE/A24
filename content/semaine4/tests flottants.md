+++
title = "Tester des nombres flottants"
weight = 44
+++

![Tests flottants](../flottants.jpeg?width=25vw)

## Les bases des nombres à virgule flottante (floats)

**Rappel**: Les nombres à virgule flottante sont des nombres avec des décimales, comme 0.1, 2.5, ou 3.14. 

{{% notice style=warning title=Attention %}}
En Python, ces nombres peuvent parfois être un peu imprécis à cause de la façon dont les ordinateurs les stockent.
{{% /notice %}}

**Exemple**:

- Imaginez que vous additionnez 0.1 et 0.2. 
- Vous attendez que le résultat soit 0.3, mais en Python, cela peut donner un résultat très légèrement différent, comme 0.30000000000000004. 
- C'est à cause des petites erreurs de calcul.

## Comment tester les floats correctement

1. **Évitez la comparaison directe** : Ne comparez pas directement deux floats avec `==` car cela peut échouer à cause des petites erreurs.
   ```python
   a = 0.1 + 0.2
   print(a == 0.3)  # Cela peut retourner False
   ```

2. **Utilisez une tolérance** : Vérifiez si les nombres sont "assez proches" en utilisant une tolérance.
   ```python
   # On importe le paquet des fonctions mathématiques
   import math

   a = 0.1 + 0.2
   b = 0.3
   print(math.isclose(a, b, rel_tol=1e-9))  # Cela retourne True
   ```

**Explication**:

La fonction `math.isclose(a, b, rel_tol=1e-9)` en Python permet de vérifier si deux valeurs flottantes, `a` et `b`, sont proches l'une de l'autre en utilisant une tolérance relative. 

Voici comment cela fonctionne :
- **`a` et `b`** : Les deux valeurs que vous comparez.
- **`rel_tol`** : La tolérance relative, qui est le maximum de différence autorisée entre `a` et `b`, relative à la magnitude des valeurs. Par défaut, cette tolérance est de \(1 \times 10^{-9}\).

La fonction retourne `True` si les valeurs sont considérées comme proches, sinon `False`. La formule utilisée est :
\[ \text{abs}(a - b) \leq \max(\text{rel\_tol} \times \max(\text{abs}(a), \text{abs}(b)), \text{abs\_tol}) \]


## Atelier

[Tester les flottants](../atelier-tests-flottants.ipynb)