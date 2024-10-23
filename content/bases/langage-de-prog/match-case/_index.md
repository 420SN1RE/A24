+++
title = 'Match Case'
weight = 6
+++

![match-case](./match-case.jpeg?width=25vw)


## L’instruction MATCH-CASE

- L’instruction `match-case` est inspirée des structures de correspondance de motifs (switch-case) présentes dans d’autres langages de programmation. 
- Elle permet **généralement** de simplifier le traitement de différentes conditions en rendant le code plus lisible et plus structuré.

## Syntaxe de base

{{% notice style=tip title=Astuce %}}
La syntaxe de l’instruction `match-case` est similaire à celle d’une série de conditions `if-elif-else`, mais elle est souvent plus concise et expressive. 
{{% /notice %}}

Syntaxe générale:

```plaintext

def action(commande):
    match commande:
        case "demarre":
            print("Démarrage...")
        case "stop":
            print("Arrêt...")
        case "pause":
            print("Pause...")
        case _:
            print("Commande inconnue")
```
- Dans cet exemple, la fonction `action` utilise `match` pour comparer la variable `commande` à différents motifs ("demarre", "stop", "pause"). 
- Si aucun motif ne correspond, le cas par défaut `(_)` est exécuté.

Voici deux exemples concrets simples: 

**Exemple 1**: Sélection de fruit:

```python
def selectionner_fruit(fruit):
    match fruit:
        case "pomme":
            return "C'est une pomme"
        case "banane":
            return "C'est une banane"
        case "cerise":
            return "C'est une cerise"
        case _:
            return "Fruit inconnu"


# Exemple d'utilisation
print(selectionner_fruit("pomme"))  # C'est une pomme
print(selectionner_fruit("kiwi"))   # Fruit inconnu
```

**Explication**:

1. **`match fruit:`** 
   - Compare la valeur de la variable `fruit` à différents motifs.

2. **`case "pomme"`**
   - Vérifie si `fruit` est égal à `"pomme"`. 
   - Si `fruit` correspond à "pomme", le code suivant `return "C'est une pomme"` est exécuté.
3. **`case "banane"`**
   - Vérifie si `fruit` est égal à `"banane"`. 
   - Si `fruit` correspond à "banane", le code suivant `return "C'est une banane"` est exécuté.
4. **`case "cerise"`**
   - Vérifie si `fruit` est égal à `"cerise"`. 
   - Si `fruit` correspond à "cerise", le code suivant `return "C'est une cerise"` est exécuté.
5. **`case _:`**
   - Le symbole `_` est un motif générique qui correspond à n'importe quelle valeur qui n'a pas été capturée par les motifs précédents.
   - **`return "Fruit inconnu"`** : Si `fruit` ne correspond à aucun des motifs précédents, la fonction retourne `"Fruit inconnu"`.

**Exemple 2**: Classification d'animaux en fonction de leur type :

```python
def classifier(animal):
    match animal:
        case "chien" | "chat" | "lapin":
            return "Mammifère"
        case "aigle" | "canari" | "perroquet":
            return "Oiseau"
        case "serpent" | "lézard" | "tortue":
            return "Reptile"
        case _:
            return "Inconnu"

# Exemple d'utilisation
animal = "chat"
print(f"{animal} est un {classifier(animal)}.") # chat est une Mammifère
```

**Explication**:

1. **`match animal:`** 
   - Compare la valeur de la variable `animal` à différents motifs.

2. **`case "chien" | "chat" | "lapin":`**
   - Vérifie si `animal` est égal à `"chien"`, `"chat"` ou `"lapin"`. 
   - Le symbole `|` signifie "ou". Si `animal` correspond à l'un de ces trois mots, le code suivant est exécuté.
   - **`return "Mammifère"`** : Si `animal` est `"chien"`, `"chat"` ou `"lapin"`, la fonction retourne la chaîne de caractères `"Mammifère"`.

3. **`case "aigle" | "canari" | "perroquet":`**
   - Vérifie si `animal` est égal à `"aigle"`, `"canari"` ou `"perroquet"`.
   - **`return "Oiseau"`** : Si `animal` est l'un de ces trois mots, la fonction retourne `"Oiseau"`.

4. **`case "serpent" | "lézard" | "tortue":`**
   - Vérifie si `animal` est égal à `"serpent"`, `"lézard"` ou `"tortue"`.
   - **`return "Reptile"`** : Si `animal` est l'un de ces trois mots, la fonction retourne `"Reptile"`.

5. **`case _:`**
   - Le symbole `_` est un motif générique qui correspond à n'importe quelle valeur qui n'a pas été capturée par les motifs précédents.
   - **`return "Inconnu"`** : Si `animal` ne correspond à aucun des motifs précédents, la fonction retourne `"Inconnu"`.

## Exemple de IF-ELIF-ELSE avec MATCH-CASE

Soit l'exemple suivant vu précédemment. Re-écrivons-le avec `match-case`:

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

Voici le même algorithme, mais avec `match-case`:

```python
age = 36

match age:
    case age if 18 <= age <= 30:
        print("Vous êtes un jeune adulte")
    case age if 30 < age < 65:
        print("Avez-vous des enfants?")
    case age if age >= 65:
        print("Bonne retraite!")
    case _:
        print("Vous êtes mineur")
```

{{% notice info %}}
Comme vous pouvez le voir, le code n'est pas vraiment plus simple. Dans ce cours, nous utiliserons principalement `if-elif-else`. Ceci dit, lorsque les directives ne vous obligent pas à utiliser `if-elif-else`, l'instruction `match-case` sera acceptée.
{{% /notice %}}
