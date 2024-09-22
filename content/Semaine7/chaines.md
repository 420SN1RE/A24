+++
title = "Les chaines de caractères"
weight = 74
+++

## L'échappement de caractères

- L'échappement de caractères permet d'inclure des caractères spéciaux dans une chaîne de caractères. Cela se fait en utilisant le caractère de barre oblique inverse (`\`).

1. **Caractères spéciaux courants** :
   - `\'` : Apostrophe ou guillemet simple
   - `\"` : Guillemets doubles
   - `\\` : Barre oblique inverse
   - `\n` : Nouvelle ligne
   - `\t` : Tabulation

   ```python
   chaine = "Ceci est une ligne.\nEt ceci est une nouvelle ligne."
   print(chaine)
   # Affiche :
   # Ceci est une ligne.
   # Et ceci est une nouvelle ligne.
   ```

2. **Inclure des guillemets dans une chaîne** :
   ```python
   chaine = "Il a dit : \"Bonjour tout le monde!\""
   print(chaine)  # Affiche : Il a dit : "Bonjour tout le monde!"
   ```

3. **Utilisation de la barre oblique inverse** :
   ```python
   chemin = "C:\\Utilisateurs\\NomUtilisateur\\Documents"
   print(chemin)  # Affiche : C:\Utilisateurs\NomUtilisateur\Documents
   ```

## La concaténation de chaînes de caractères

- La concaténation consiste à assembler plusieurs chaînes de caractères en une seule. En Python, il existe plusieurs méthodes pour y parvenir :

1. Utilisation de l'opérateur `+`
2. Utilisation de la méthode `join()`
3. Utilisation de l'opérateur `*` pour répéter une chaîne

## Accès aux caractères d'une chaine

- On utilise les `[]` et l'indice de position du caractère, comme avec les listes.
- **NB** : L'indiice du premier caractères ets toujours 0.

## Obtenir la longueur d'une chaine de caractères

- La méthode `len()` est utilisée.

## Lire les caractères d'une chaine un à un

- La boucle `for` permet de parcourir chaque caractères d'une chaine.


## Mettre en MAJUSCULES ou en minuscule

- La méthode `upper()` permet de mettre les caractères en MAJUSCULES.
- La méthode `lower()` permet de mettre les caractères en minuscules.

## Extraire une partie d'une chaine de caractère (slicing)

- L'utilisation de `[debut : fin]` permet d'extraire une sous-chaine de la chaine initiale, à partir du caractères à l'indice `debut` et jusqu'au caractères en position `fin-1` inclus.


## Diviser une chaine en spécifiant un délimiteur de sous-chaines

- La méthode `split()` divise une chaîne de caractères en une liste de sous-chaînes, en utilisant un séparateur spécifié (par défaut, un espace).


## Convertir une chaine de caractère en liste

- La fonction `list()` crée une liste où chaque élément est un caractère de la chaîne. En d’autres termes, elle transforme la chaîne de caractères en une liste de ses caractères individuels.

## Formatage à l'aide de f-strings

- Les f-strings permettent d'incorporer des expressions à l'intérieur de chaînes de caractères en utilisant des accolades `{}`.

```python
age = 25
nom = "Nathalie"
message = f"{nom} a {age} ans et dans 5 ans, elle aura {age + 5} ans."
print(message) # Affiche: Nathalie a 25 ans et dans 5 ans , elle aura 30 ans.
```




   



