+++
title = "Techniques de débogage"
weight = 182
+++

![Débogage](tech-debog.jpg?width=25vw).

## Techniques utilisant la méthode print()

### Gestion des exceptions

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

### Suivi du flux d'exécution

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

### Inspection des variables

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

### Débogage des fonctions récursives

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

### Messages d'erreur et expressions conditionnelles

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

## Technique utilisant un outil intégré (Ex: VS Code)

Les points d'arrêt (breakpoints) sont des outils essentiels pour le débogage dans Visual Studio Code (VS Code). Voici un aperçu de leur utilisation :

### Qu'est-ce qu'un point d'arrêt ?

Un point d'arrêt est un marqueur que vous placez dans votre code pour indiquer à l'outil de débogage où s'arrêter pendant l'exécution. Cela vous permet d'examiner l'état de votre application à des moments spécifiques.

### Comment ajouter un point d'arrêt ?

1. **Ouvrez votre fichier de code** dans VS Code.
2. **Cliquez dans la marge de gauche** à côté de la ligne de code où vous souhaitez ajouter un point d'arrêt. Un point rouge apparaîtra, indiquant que le point d'arrêt est actif.

### Utilisation des points d'arrêt

- **Lancer le débogage** : Appuyez sur `F5` ou allez dans le menu `Run` et sélectionnez `Start Debugging`.
- **Exécution jusqu'au point d'arrêt** : Votre programme s'exécutera normalement jusqu'à ce qu'il atteigne le point d'arrêt, où il s'arrêtera.
- **Examiner les variables** : Une fois arrêté, vous pouvez survoler les variables avec votre souris pour voir leurs valeurs actuelles, ou utiliser le panneau `Variables` pour une vue plus détaillée.
- **Contrôler l'exécution** : Utilisez les commandes de débogage comme `Step Over` (F10), `Step Into` (F11), et `Continue` (F5) pour naviguer dans votre code.

### Gestion des points d'arrêt

- **Activer/Désactiver** : Cliquez droit sur le point d'arrêt et sélectionnez `Enable Breakpoint` ou `Disable Breakpoint`.
- **Supprimer** : Cliquez droit et sélectionnez `Remove Breakpoint` ou cliquez simplement sur le point rouge.

Les points d'arrêt sont des outils puissants pour identifier et corriger les erreurs dans votre code, rendant le processus de débogage plus efficace et moins frustrant.