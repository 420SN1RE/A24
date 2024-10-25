+++
title = "Suivre l'exécution du programme"
weight = 91
+++

![debogage avec print](../debogage-print.jpeg?width=25vw)


Le code que nous écrivons ne fonctionne pas toujours comme prévu et peut parfois produire des résultats inattendus. Lorsqu’un problème survient, il est plus efficace d’utiliser une technique de débogage plutôt que de rester perplexe devant le code. 

Un débogueur permet d’exécuter le code pas à pas pour identifier précisément où se trouve l’erreur et comprendre les corrections nécessaires. Bien que l’utilisation d’un débogueur demande du temps et des efforts, c’est une compétence essentielle pour tout développeur.

## L’importance du débogage

Le débogage est une étape très importante dans le développement de logiciels. Il permet de détecter et de corriger les erreurs dans le code, garantissant ainsi que le programme fonctionne comme prévu. Sans débogage, les bugs peuvent entraîner des comportements inattendus, des plantages ou des résultats incorrects. Voici quelques raisons pour lesquelles le débogage est essentiel :

- **Assurer la fiabilité** : Un code sans bogues est plus fiable et offre une meilleure expérience utilisateur.
- **Améliorer la performance** : Le débogage permet d'identifier et de corriger les inefficacités dans le code.
- **Faciliter la maintenance** : Un code bien débogué est plus facile à comprendre et à maintenir.
- **Apprentissage et amélioration** : Le processus de débogage aide les développeurs à mieux comprendre le fonctionnement de leur code et à améliorer leurs compétences en programmation.

## Analyse du problème avant le code

Avant de déboguer un programme, il est crucial revoir les hypothèses faites pour prévoir les résultats. Des hypothèses incorrectes peuvent compliquer l’identification des problèmes. 

### Quelques conseils

- Il est important de repérer les fautes de frappe, et de considérer les modifications récentes du code. 

- Comprendre l’intention du code, surtout s’il a été écrit par quelqu’un d’autre, est également essentiel. 

- Commencer par un petit segment de code fonctionnel et tester progressivement peut faciliter la correction des erreurs. 

- Remettre en question ses hypothèses peut réduire le temps nécessaire pour identifier et corriger les problèmes.


## Suivre la trace à l'aide de la méthode print()

En utilisant la méthode `print()`, vous pouvez facilement suivre l'exécution de votre programme et identifier les erreurs. Cette technique est particulièrement utile pour les débutants en programmation, car elle permet de visualiser le comportement du code en temps réel.

En insérant des instructions `print()` à des endroits stratégiques du code, vous pouvez suivre l'évolution des variables et comprendre le flux d'exécution du programme. Voici comment appliquer cette technique pour résoudre des bugs courants.

### Exemple 1 : Boucles imbriquées

```python
def multiplication(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i} * {j} = {i * j}")
        print("Fin de la ligne", i)

# Test
multiplication(3)
```

Pour déboguer ce code, vous pouvez ajouter des instructions `print()` pour vérifier les valeurs de `i` et `j` à chaque itération :

```python
def multiplication(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"i = {i}, j = {j}")
            print(f"{i} * {j} = {i * j}")
        print("Fin de la ligne", i)

# Test
multiplication(3)
```

### Exemple 2 : Conditions imbriquées

```python
def pair_impair(num):
    if num > 0:
        if num % 2 == 0:
            print("Le nombre est positif et pair")
        else:
            print("Le nombre est positif et impair")
    elif num == 0:
        print("Le nombre est zéro")
    else:
        if num % 2 == 0:
            print("Le nombre est négatif et pair")
        else:
            print("Le nombre est négatif et impair")

# Test
pair_impair(4)
pair_impair(-3)
pair_impair(0)
```

Pour déboguer ce code, vous pouvez ajouter des instructions `print()` pour vérifier la valeur de `num` et les conditions visitées :

```python
def pair_impair(num):
    print(f"Vérification du nombre : {num}")
    if num > 0:
        print("Le nombre est positif")
        if num % 2 == 0:
            print("Le nombre est positif et pair")
        else:
            print("Le nombre est positif et impair")
    elif num == 0:
        print("Le nombre est zéro")
    else:
        print("Le nombre est négatif")
        if num % 2 == 0:
            print("Le nombre est négatif et pair")
        else:
            print("Le nombre est négatif et impair")

# Test
pair_impair(4)
pair_impair(-3)
pair_impair(0)
```

## Le débogueur intégré à Visual Studio Code

Visual Studio Code offre une gamme d'outils de débogage puissants et intégrés. Parmi ces outils, on trouve :
- le débogueur intégré qui permet de définir des **points d'arrêt** (*breakpoints*), de surveiller les variables, et de parcourir le code pas à pas. 
- des extensions spécifiques pour améliorer les capacités de débogage, telles que l'extension Python pour le débogage de scripts Python

Ces outils facilitent l'identification et la correction des erreurs dans le code, rendant le processus de développement plus efficace et moins stressant.

[Le Débogueur de VS Code en action](https://youtu.be/b4p-SBjHh28?si=C8bff51TX5xS6g-O)

[Bases de connaissances](https://420sn1re.github.io/A24/bases/outils/vs-code/deboggueur/index.html)


## Pause 5 minutes

![Pause](../pause.jpg?width=25vw)
