+++
alwaysopen = false
title = 'Erreurs communes'
weight = 3
+++

![Erreurs communes](erreur-debogage.jpeg?width=20vw)

Au fil des semaines nous aurons l'occasion de localiser et de corriger différentes erreurs (ou bogues). 
Dans cette section "Erreurs et débogage", vous trouverez des techniques qui permettent de déboguer vos programmes.

## La méthode Print et le débogage

Une erreur de syntaxe signifie que le code n'est pas conforme aux règles de syntaxe du langage. Cela est habituellement détecté immédiatement.

Par exemple, si on oublie d'indenter correctement le code, ou une parenthèse dans une fonction, cela génère une erreur de syntaxe.

## La syntaxe et les erreurs d'exécution en Python

Python est un langage de programmation réputé pour sa simplicité et sa lisibilité. Toutefois, comme tout langage de programmation, il est sujet aux erreurs de syntaxe et d'exécution. 

Comprendre la syntaxe de Python et savoir comment gérer les erreurs d'exécution est essentiel pour écrire des programmes robustes et fiables. La détection et la correction des erreurs, qu'elles soient de syntaxe ou d'exécution, permettent d'améliorer la qualité du code et d'assurer son bon fonctionnement. 

Comprendre comment identifier et corriger ces erreurs est essentiel pour tout développeur. 

Les erreurs que l'on rencontre en programmation sont de 2 types:
- **syntaxique**: Comme dans un langage naturelle, on peut faire des fautes d'orthographe ou de grammaire.
- **logique**: La syntaxe est correcte, mais les opérations ne répondent pas au problème, ou donnent un mauvais résultat.

### La syntaxe en Python

La syntaxe de Python est conçue pour être claire et concise. 

Voici quelques rappel des éléments clés de la syntaxe Python :

- **Indentation**:

    Python utilise l'indentation pour délimiter les blocs de code. Une indentation incorrecte entraînera une erreur de syntaxe.


- **Déclaration des variables**

    Les variables en Python sont créées en les assignant à une valeur sans avoir besoin de déclarer leur type explicitement.


- **Structures de contrôle**

    Les structures de contrôle, comme les boucles et les conditions, doivent être correctement indentées et formées.



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

## Gestion des exceptions

Python permet de gérer les exceptions à l'aide des blocs `try-except`. Cela permet d'attraper les erreurs et de les traiter de manière appropriée sans interrompre l'exécution du programme.

```python
try:
    resultat = 10 / 0
except ZeroDivisionError:
    print("Erreur : division par zéro")
```

Il est également possible de gérer plusieurs types d'exceptions dans un même bloc `try-except`.

```python
try:
    ma_liste = [1, 2, 3]
    print(ma_liste[5])
except IndexError:
    print("Erreur : index de liste incorrect")
except ZeroDivisionError:
    print("Erreur : division par zéro")
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

---

## Vérification du fonctionnement d'un Programme

La méthode `print` est l'une des techniques les plus simples et les plus couramment utilisées pour déboguer un programme en Python. 
Bien que ce ne soit pas la méthode la plus sophistiquée ni la plus efficace pour les projets complexes, `print` peut être extrêmement utile pour comprendre le flux d'exécution d'un programme, inspecter les valeurs des variables et identifier les points où le programme ne fonctionne pas comme prévu. 

## Principe de base

L'idée de base de l'utilisation de `print` pour le débogage est d'insérer des instructions `print` à divers endroits du programme pour afficher les valeurs des variables et les messages d'état. 
Cela permet de suivre l'exécution du programme et de localiser les problèmes.

```python
def addition(a, b):
    print(f"Entrée dans la fonction addition avec a={a} et b={b}")
    resultat = a + b
    print(f"Résultat de l'addition: {resultat}")
    return resultat

# Exemple d'utilisation
resultat = addition(3, 5)
print(f"Le résultat final est: {resultat}")
```

## Suivi du flux d'exécution

En ajoutant des instructions `print` à différents endroits du programme, vous pouvez suivre le flux d'exécution et voir quelles parties du code sont exécutées. 
Cela est particulièrement utile pour les structures de contrôle comme les boucles et les conditions.

```python
def verifier_parite(nombre):
    print(f"Vérification de la parité pour le nombre: {nombre}")
    if nombre % 2 == 0:
        print("Le nombre est pair")
        return True
    else:
        print("Le nombre est impair")
        return False

# Exemple d'utilisation
for i in range(5):
    resultat = verifier_parite(i)
    print(f"Le nombre {i} est pair: {resultat}")
```

## Inspection des variables

L'une des utilisations les plus courantes de `print` est d'inspecter les valeurs des variables à différents points du programme. 
Cela permet de vérifier que les variables contiennent les valeurs attendues.

```python
def calculer_somme_liste(liste):
    somme = 0
    for element in liste:
        print(f"Ajout de {element} à la somme actuelle de {somme}")
        somme += element
    print(f"La somme totale est: {somme}")
    return somme

# Exemple d'utilisation
ma_liste = [1, 2, 3, 4]
resultat = calculer_somme_liste(ma_liste)
print(f"Le résultat final est: {resultat}")
```

## Débogage des fonctions récursives

Le débogage des fonctions récursives peut être particulièrement difficile. L'utilisation de `print` pour afficher les valeurs des arguments à chaque appel récursif peut aider à comprendre le comportement de la fonction.

```python
def factorielle(n):
    print(f"Calcul de factorielle({n})")
    if n == 0:
        return 1
    else:
        resultat = n * factorielle(n - 1)
        print(f"Résultat intermédiaire pour factorielle({n}): {resultat}")
        return resultat

# Exemple d'utilisation
resultat = factorielle(5)
print(f"Le résultat final est: {resultat}")
```

## Messages d'erreur et expressions conditionnelles

Inclure des messages d'erreur conditionnels peut aider à identifier pourquoi une certaine branche du code est exécutée ou pourquoi une erreur se produit.

```python
def division(a, b):
    if b == 0:
        print("Erreur: Tentative de division par zéro")
        return None
    else:
        resultat = a / b
        print(f"Résultat de la division: {resultat}")
        return resultat

# Exemple d'utilisation
resultat = division(10, 0)
if resultat is not None:
    print(f"Le résultat final est: {resultat}")
```

## Les limites de la méthode `print`

Bien que la méthode `print` soit simple et efficace pour les petits projets ou pour un débogage rapide, elle présente des limites, notamment :

- **Verbiage excessif** : Trop d'instructions `print` peuvent rendre la sortie du programme difficile à lire.
- **Performance** : L'utilisation excessive de `print` peut ralentir l'exécution du programme.
- **Gestion des erreurs** : `print` ne gère pas les exceptions ou les erreurs de manière structurée.

Pour ces raisons, il est souvent préférable d'utiliser des outils de débogage plus avancés, comme les tests unitaires ou les débogueurs intégrés, pour les projets plus complexes.
