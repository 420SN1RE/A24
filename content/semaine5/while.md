+++
title = "La boucle while"
weight = 52
+++

![Boucle for](../boucle-while.jpeg?width=20vw)

## La boucle WHILE

La boucle `while` permet d'exécuter un bloc de code **tant qu'**une condition donnée est vraie. 

La syntaxe de base est la suivante :
```python
while condition:
    # bloc de code à exécuter
```

**Principe de base**: la condition de la boucle `while` est évaluée avant chaque exécution du bloc de code. Si la condition est vraie, le bloc de code s'exécute. Après chaque exécution, la condition est réévaluée. Ce processus se répète jusqu'à ce que la condition devienne fausse, auquel moment la boucle se termine et le programme continue avec les instructions suivantes.

{{% notice style=info %}}
La boucle `while` s'utilise, lorsque le nombre d'itérations (répétitions) **n'est pas** connu d'avance..
Typiquement avec des saisies utilisateurs
{{% /notice %}}


**Exemple simple :**

```python
compteur = 0
while compteur < 5:
    print(compteur)
    compteur -= 1
```

```plaintext
0
1
2
3
4
```

Dans cet exemple, la boucle s'exécute tant que la valeur de `compteur` est inférieure à 5.

### Boucle WHILE dans un ordinogramme

Pour la boucle `while`, l'ordinogramme commence par une décision basée sur la condition de la boucle. Si la condition est vraie, le flux continue vers les instructions à répéter, puis retourne à la condition initiale.

**Exemple:**

```
+-------------------+
| Début             |
+-------------------+
         |
         V
+-------------------+
| i = 0             |
+-------------------+
         |
         V
+-------------------+
| Tant que i < 5    |
+-------------------+
         | Oui
         V
+-------------------+
| Afficher i        |
+-------------------+
         |
         V
+-------------------+
| i = i + 1         |
+-------------------+
         | (retour à la condition)
         |
         | Non
         V
+-------------------+
| Fin               |
+-------------------+
```

## Conditions et boucles infinies

{{% notice style=warning title=Attention %}}
La boucle `while` nécessite une **condition de sortie** pour éviter les boucles infinies.  
Il est courant d'utiliser une variable de contrôle qui est modifiée à chaque itération.
{{% /notice %}}

### Importance de la condition de sortie

**Exemple où la condition de sortie est omise

```python
# Boucle sans la condition de sortie
nombre = 10
while nombre > 0:
    print(nombre)
```
On obtient ce qu'on appelle une **boucle infinie**, car la valeur de `nombre` reste toujours à 10:

```plaintext
10
10
10
10
10
10
...
```

{{% notice style=note title=Astuce %}}
Pour sortir d’une boucle infinie, il faut utiliser le clavier et taper les touches `CTRL+C`.
{{% /notice %}}

**Exemple corrigé avec la condition de sortie**:

```python
# Boucle avec condition de sortie
nombre = 10
while nombre > 0:
    print(nombre)
    # Condition de sortie
    nombre -= 1
```

```plaintext
10
9
8
7
6
5
4
3
2
1
```

Dans cet exemple, l'instruction `nombre -= 1` permet de faire changer (**décrémenter**) la valeur la variable `nombre` jusqu'à ce qu'elle atteigne 0.


## Atelier

[Boucle while](../atelier-while.ipynb)
