+++
title = "Les Librairies systèmes"
weight = 71
+++

![Librairies systèmes](../librairies.png?width=25vw)


## Qu'est-ce qu'une librairie système ?

En Python, les librairies systèmes fournissent des interfaces pour intéragir avec le système d'exploitation et les ressources matérielles sous-jacentes.

Une librairie système est un ensemble de modules et de fonctions fournies par le système d'exploitation ou par des bibliothèques externes qui permettent aux programmes :

- De communiquer avec le système d'exploitation
- D'accéder aux ressources matérielles
- De gérer des processus
- De manipuler des fichiers
- D'effectuer d'autres opérations système de bas niveau.


### Exemple

```python
import os  # importation de la librairie os

print(os.listdir('.'))  # Liste les fichiers dans le répertoire courant
os.mkdir("foo")         # Crée le répertoire foo
```

## Librairie os

Ce module permet d'utiliser les fonctionnalités dépendantes du système d'exploitation telles que :
- La gestion des fichiers et des répertoires
- L'exécution de commandes système

Il faut d'abord importer la librairie :

```python
import os
```

### Fichiers et répertoires

#### Qu'est-ce qu'un fichier ?

Un fichier est une unité de stockage sur un ordinateur. Pensez à un fichier comme à une feuille de papier où vous pouvez écrire des informations. Les fichiers peuvent contenir différents types de données, comme du texte, des images, de la musique, des vidéos, ou des programmes.

#### Qu'est-ce qu'un répertoire ?

Un répertoire, aussi appelé dossier, est un conteneur qui peut contenir des fichiers et d'autres répertoires. Imaginez un répertoire comme un classeur où vous pouvez organiser vos feuilles de papier (fichiers) en différentes sections (sous-dossiers).


#### Organisation des fichiers et des répertoires

Les fichiers et les répertoires sont organisés dans une structure hiérarchique, souvent comparée à un arbre :

- **Répertoire racine** : Le répertoire principal qui contient tous les autres fichiers et répertoires. Sur Windows, il est souvent appelé `C:\`. Sur macOS et Linux, il est appelé `/`.
- **Sous-répertoires** : Répertoires à l'intérieur d'autres répertoires. Ils permettent d'organiser les fichiers de manière logique. Par exemple, un répertoire `Documents` peut contenir des sous-répertoires pour des `projets`, des `factures`, etc.
- **Chemin d'accès** : La manière dont on désigne l'emplacement d'un fichier ou d'un répertoire. Par exemple, le chemin d'accès à une vidéo peut être `C:\Vidéo\Archives\video_01.mkv` sur Windows.


![fichier 1](../fichier_01.png)

Dans cet exemple, `Image`, `Musique` et `Vidéo` sont des sous-répertoires de `Racine`.  
Le répertoire `Vidéo` contient un sous-répertoire `Archives` et un fichier `video_03.mkv`.  
Le répertoire `Musique` est vide.  

##### Chemins relatif vs absolu

Un **chemin absolu** part toujours de la racine.  
Exemple:
- `C:\Vidéo\Archives\video_01.mkv`

Un **chemin relatif** part d'où nous sommes. Par exemple, si un programme est exécuté dans le répertoire `Vidéo`, son point de départ sera `Vidéo`. Les `..` permettront de remonter au répertoire parent.  
Exemples (à partir de `Vidéo`):
- Pour accéder à `video_01.mkv`: `.\Archives\video_01.mkv`
- Pour accéder à `image_01.png`: `..\Image\image_01.png`


### Gestion de fichiers et répertoires


#### Lister les fichiers et les répertoires

```python
liste = os.listdir()   # liste des fichiers/répertoires du répertoire courant
liste = os.listdir('foo')   # liste des fichiers/répertoires du sous-répertoire "foo"
liste = os.listdir('..')   # liste des fichiers/répertoires du répertoire parent
liste = os.listdir('C:\Vidéo\Archives')   # liste des fichiers/répertoires du répertoire "Archives"
```

#### Créer un répertoire

```python
os.mkdir('nouveau_repertoire')  # Crée le répertoire "nouveau_repertoire" dans le répertoire courant
```


#### Combiner des composants de chemin

```python
chemin = os.path.join('repertoire', 'fichier.txt')  # Crée le chemin à partir des chaines "repertoire" et "fichier.txt"

```

`os.path.join` prend en compte le système d'exploitation pour combiner les composantes du chemin.  
Sous Windows, `chemin` sera `repertoire\fichier.txt`, tandis que sous Linux, il sera `repertoire/fichier.txt`.  
Ce qui permettra à ce programme s'exécuter peu importe le système d'exploitation.


#### Vérifier si un chemin est un fichier/répertoire

```python
est_fichier = os.path.isfile('repertoire/fichier.txt')   # Retourne Vrai si le fichier existe, sinon Faux
est_repertoire = os.path.isdir('repertoire')   # Retourne Vrai si le répertoire existe, sinon Faux
```

La fonction `os.path.exists()` est plus générale et indique si le chemin existe. Cette fonction est très utilise pour éviter les erreurs:

```python
if os.path.exists('repertoire/fichier.txt'):        # Si le fichier n'existe pas, la lecture n'aura pas lieu
    with open('repertoire/fichier.txt', 'r') as fichier:
        contenu = fichier.read()
    print(contenu)
```

#### Supprimer un fichier/répertoire

```python
os.remove('fichier.txt')    # Supprime le fichier "fichier.txt"
os.rmdir('repertoire')   # Supprime le répertoire "repertoire" et tout ce qui se trouve à l'intérieur
```

### Gestion de processus

#### Exécuter une commande système

La fonction `os.system()` permet d'exécuter des commandes système.
Les commandes système sont dépendantes de votre système d'exploitation (ex: Windows vs Linux).
Donc, les commandes devront être ajustées en conséquence.

Par exemple, sous Windows, la commande `dir` permet d'obtenir la liste des fichiers et répertoires. Tandis que sous Linux, la commande est `ls`.

```python
os.system('ls')      # Liste des fichiers et répertoire sous Linux
os.system('dir')     # Liste des fichiers et répertoire sous Windows
```

Cet exemple est seulement pour illustrer la différence entre les systèmes d'exploitation.
Il aurait été préférable d'utiliser la commande `os.listdir()` qui a la même fonctionnalité que `ls` ou `dir`, mais fonctionne sur toutes les plateformes.

Il est possible d'exécuter d'autres programmes à l'aide la de commande `os.system()`. Par exemple, il est possible d'exécuter un autre script `Python`:


```python
# premierProgramme.py
print('Bonjour')
```

```python
# deuxiemeProgramme.py
os.system('python premierProgramme.py')
```

Si on exécute `deuxiemeProgramme.py`, celui-ci appellera à son tour le programme `premierProgramme.py` qui lui affichera `Bonjour`.


## Librairie sys

Ce module fournit des fonctions et des variables utilisées pour manipuler différentes parties de l'environnement d'exécution Python, telles que les arguments de la ligne de commande, les variables d'environnement, le chemin de recherche de modules, etc.

### Les arguments

Il est possible de lancer un programme python avec des arguments. On utilise `sys.argv` pour accéder à ceux-ci. `sys.argv` est une liste contenant les arguments sous forme de chaîne de caractères (`string`). La première valeur est le nom du programme.  
Exemple:

```python
# addition.py
# Programme utilisant des arguments

import sys

print("Programme:", sys.argv[0])    # Affichera le nom du programme, soit "addition.py"

nombre_1 = int(sys.argv[1])         # "nombre_1" devient la valeur numérique du 1er argument
nombre_2 = int(sys.argv[2])         # "nombre_2" devient la valeur numérique du 2e argument
reponse = nombre_1 + nombre_2

print("Réponse:", reponse)
```

[addition.py](../addition.py)

Pour lancer le programme à la ligne de commande:

```
## Windows
python addition.py 2 3      # Devrait donner la réponse 5

## Linux
python3 addition.py 2 3      
```

Essayez de lancer le programme sans argument.  
Modifiez le programme pour éviter cette erreur.


## Sortir du programme

Si tout ce passe bien, les programmes terminent normalement lorsqu'il n'y a plus de code à exécuter.  
Dans ce cas, le programme retournera la valeur `0`.  
Si une erreur se produit en cours d'exécution et que le programme s'arrête anormalement, une valeur différente de `0` sera retournée.  
L'utilisateur du programme pourra utiliser la documentation pour connaître la signification de ce code d'erreur.

La fonction `sys.exit()` permet de sortir du programme immédiatement en retournant un code.


```python
# addition_2.py
# Programme utilisant des arguments

import sys

print("Programme:", sys.argv[0])    # Affichera le nom du programme, soit "addition.py"

if len(sys.argv) != 3:
    print("Vous devez fournir 2 arguments pour l'addition")
    sys.exit(1)

if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    print("Vous devez fournir des arguments numériques pour l'addition")
    sys.exit(2)

nombre_1 = int(sys.argv[1])         # "nombre_1" devient la valeur numérique du 1er argument
nombre_2 = int(sys.argv[2])         # "nombre_2" devient la valeur numérique du 2e argument
reponse = nombre_1 + nombre_2

print("Réponse:", reponse)
```

[addition_2.py](../addition_2.py)


Exemple :

```
# Windows
python addition_2.py 2 3        # Devrait donner la réponse 5
echo %ERRORLEVEL%               # Devrait donner 0

python addition_2.py 2          # Erreur
echo %ERRORLEVEL%               # Devrait donner 1

python addition_2.py 2 a        # Erreur
echo %ERRORLEVEL%               # Devrait donner 2


# Linux
python3 addition_2.py 2         # Erreur
echo $?                         # Devrait donner 1
```

## Valeur maximale

En python, la valeur maximale d'un `int` est de 9223372036854775807.
Il est possible d'utiliser cette valeur à l'aide de `sys.maxsize`.


```python
import sys

print('Maximum :', sys.maxsize)   # Affiche 9223372036854775807
```

Exemple d'utilisation pour trouver la valeur minimale dans une liste:

```python
import sys

ma_liste = [7,5,3,4,5,7,6,1,2,6]
minimum_trouve = sys.maxsize       # On initialise minimum_trouve avec une très grande valeur

for val in ma_liste:
    if val < minimum_trouve:
        minimum_trouve = val

print("La valeur minimale est :", minimumTrouve)
```

## Atelier

[Les librairies](../atelier_librairies.ipynb)


## Exemples

[Exemples en .ipynb](../atelier_librairies.ipynb)
