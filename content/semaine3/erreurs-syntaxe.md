+++
title = "Syntaxe et erreurs d'exécution"
weight = 33
+++

![Erreurs de syntaxe](../erreurs-syntaxe.jpeg?width=25vw).

## La syntaxe et les erreurs d'exécution en Python

Python est un langage de programmation réputé pour sa simplicité et sa lisibilité. Toutefois, comme tout langage de programmation, il est sujet aux erreurs de syntaxe et d'exécution. 

Comprendre la syntaxe de Python et savoir comment gérer les erreurs d'exécution est essentiel pour écrire des programmes robustes et fiables. La détection et la correction des erreurs, qu'elles soient de syntaxe ou d'exécution, permettent d'améliorer la qualité du code et d'assurer son bon fonctionnement. 

Comprendre comment identifier et corriger ces erreurs est essentiel pour tout développeur. 

Les erreurs que l'on rencontre en programmation sont de 2 types:
- **syntaxique**: Comme dans un langage naturelle, on peut faire des fautes d'orthographe ou de grammaire.
- **logique**: La syntaxe est correcte, mais les opérations ne répondent pas au problème, ou donnent un mauvais résultat.

### La syntaxe en Python

La syntaxe de Python est conçue pour être claire et concise. 

Voici quelques rappels des éléments clés de la syntaxe Python :

- **Déclaration des variables**

    Les variables en Python sont créées en les assignant à une valeur sans avoir besoin de déclarer leur type explicitement.
    Les noms de variables sont sujets à des règles bien précises qui doivent être respectées.


- **Indentation**:

    Python utilise l'indentation pour délimiter les blocs de code. Une indentation incorrecte entraînera une erreur de syntaxe.


- **Structures de contrôle**

    Les structures de contrôle, comme les [structures conditionnelles](../Semaine4/) et les [boucles](../Semaine5/), doivent être correctement indentées et formées.


### Les erreurs de syntaxe

Les erreurs de syntaxe surviennent lorsque le code ne respecte pas les règles syntaxiques de Python. Ces erreurs sont détectées lors de la phase d'interprétation du code, avant l'exécution du programme.

#### 1. Les erreurs d'indentation

Les erreurs d'indentation sont parmi les plus courantes en Python. Elles se produisent lorsque les blocs de code ne sont pas correctement alignés.

```python
def ma_fonction():
    print("Début de la fonction")
  print("Erreur d'indentation ici")  # Erreur d'indentation
```

#### 2. Parenthèses, crochets et accolades non fermés

Les erreurs de parenthèses et de crochets non fermés se produisent lorsque les parenthèses, crochets ou accolades ne sont pas correctement fermés.

```python
# Manque une parenthèse fermante
print("Bonjour"

# Manque un crochet fermant
ma_liste = [1, 2, 3, 4
```

#### 3. Syntaxe invalide

D'autres erreurs de syntaxe incluent l'utilisation incorrecte des mots-clés ou des opérateurs.

```python
# Utilisation incorrecte du mot-clé
def 123fonction():  # Les noms de fonctions ne peuvent pas commencer par un chiffre

# Opérateur incorrect
resultat = 5 * * 2  # Les opérateurs doivent être correctement espacés
```

#### 4. Erreurs d'exécution

Les erreurs d'exécution, ou exceptions, surviennent pendant l'exécution du programme. Elles sont souvent causées par des opérations illégales, telles que la division par zéro ou l'accès à un index de liste inexistant.

### Les types d'exceptions courantes

##### `ZeroDivisionError`

Cette erreur se produit lorsqu'une division par zéro est tentée.

```python
a = 10 / 0  # ZeroDivisionError
```

##### `IndexError`

Cette erreur se produit lorsqu'un index inexistant est accédé dans une liste.

```python
ma_liste = [1, 2, 3]
print(ma_liste[5])  # IndexError
```

##### `KeyError`

Cette erreur se produit lorsqu'une clé inexistante est accédée dans un dictionnaire.

```python
mon_dict = {"nom": "Alice", "âge": 25}
print(mon_dict["adresse"])  # KeyError
```

##### `TypeError`

Cette erreur se produit lorsqu'une opération ou une fonction est appliquée à un objet de type inapproprié.

```python
print("Bonjour" + 5)  # TypeError
```

## Messages d'erreur et débogage

Les messages d'erreur en Python sont généralement explicites et indiquent la nature de l'erreur ainsi que la ligne du code où elle s'est produite. Analyser ces messages est crucial pour identifier et corriger les erreurs.

### Exemple de message d'erreur

```plaintext
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    a = 10 / 0
ZeroDivisionError: division by zero
```

Dans cet exemple, le message d'erreur indique une `ZeroDivisionError` sur la ligne 2 de `main.py`.

## Vérification du fonctionnement d'un programme

La méthode `print` est l'une des techniques les plus simples et les plus couramment utilisées pour déboguer un programme en Python. 
Bien que ce ne soit pas la méthode la plus sophistiquée ni la plus efficace pour les projets complexes, `print` peut être extrêmement utile pour comprendre le flux d'exécution d'un programme, inspecter les valeurs des variables et identifier les points où le programme ne fonctionne pas comme prévu. 

## Principe de base

L'idée de base de l'utilisation de `print` pour le débogage est d'insérer des instructions `print` à divers endroits du programme pour afficher les valeurs des variables et les messages d'état. 
Cela permet de suivre l'exécution du programme et de localiser les problèmes.

```python
def addition(a, b):
    print("Entrée dans la fonction addition avec a=",a," et b=",b)
    resultat = a + b
    print("Résultat de l'addition: ", resultat)
    return resultat

# Exemple d'utilisation
resultat = addition(3, 5)
print("Le résultat final est: ", resultat)
```

## Les limites de la méthode print

Bien que la méthode `print` soit simple et efficace pour les petits projets ou pour un débogage rapide, elle présente des limites, notamment :

- **Verbiage excessif** : Trop d'instructions `print` peuvent rendre la sortie du programme difficile à lire.
- **Performance** : L'utilisation excessive de `print` peut ralentir l'exécution du programme.
- **Gestion des erreurs** : `print` ne gère pas les exceptions ou les erreurs de manière structurée.

Pour ces raisons, il est souvent préférable d'utiliser des outils de débogage plus avancés, comme les tests unitaires ou les débogueurs intégrés, pour les projets plus complexes.


## Pause : 5 minutes

![Pause](../pause.jpg?width=25vw)

## Révision pour le minitest

**==> Moodle**
