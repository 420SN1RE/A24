+++
title = "Installation des bibliothèques Python"
weight = 1.3
+++

![Installation Python](install-lib.png?width=25vw)


## Installation des bibliothèques Python sur Windows 10/11

Python est un langage de programmation puissant et polyvalent, largement utilisé pour l'analyse de données, la visualisation et les calculs scientifiques. Les bibliothèques `pandas`, `matplotlib`, `numpy` et `scipy` sont parmi les plus populaires pour ces tâches. Ce chapitre vous guidera à travers les étapes nécessaires pour installer ces bibliothèques sur un système Windows 10 ou 11.

### Prérequis

Avant de commencer, assurez vous d'avoir installé Python sur votre système. Vous pouvez télécharger la dernière version de Python depuis le site officiel [python.org](https://www.python.org/). Pendant l'installation, assurez vous de cocher l'option **"Add Python to PATH"**.

### Étape 1 : Ouvrir l'invite de commande (Windows)

Ouvrir l'invite de commande sur Windows 10 et Windows 11 est assez simple. Voici les étapes pour chaque version :

#### Windows 10

1. **Utiliser le menu Démarrer** :
   - Cliquez sur le bouton **Démarrer** (icône Windows en bas à gauche de l'écran).
   - Tapez **cmd** ou **invite de commande** dans la barre de recherche.
   - Cliquez sur **Invite de commandes** dans les résultats de recherche.

2. **Utiliser le raccourci clavier** :
   - Appuyez sur les touches **Windows + R** pour ouvrir la boîte de dialogue **Exécuter**.
   - Tapez **cmd** et appuyez sur **Entrée**.

3. **Utiliser le menu contextuel** :
   - Faites un clic droit sur le bouton **Démarrer**.
   - Sélectionnez **Invite de commandes** ou **Windows PowerShell** (selon la version de Windows 10).

#### Windows 11

1. **Utiliser le menu Démarrer** :
   - Cliquez sur le bouton **Démarrer** (icône Windows au centre de la barre des tâches).
   - Tapez **cmd** ou **invite de commande** dans la barre de recherche.
   - Cliquez sur **Invite de commandes** dans les résultats de recherche.

2. **Utiliser le raccourci clavier** :
   - Appuyez sur les touches **Windows + R** pour ouvrir la boîte de dialogue **Exécuter**.
   - Tapez **cmd** et appuyez sur **Entrée**.

3. **Utiliser le menu contextuel** :
   - Faites un clic droit sur le bouton **Démarrer**.
   - Sélectionnez **Terminal Windows** ou **Windows PowerShell** (selon la version de Windows 11).

#### Astuce supplémentaire

Pour ouvrir l'invite de commande en tant qu'administrateur, faites un clic droit sur **Invite de commandes** ou **Terminal Windows** et sélectionnez **Exécuter en tant qu'administrateur**.


### Étape 2 : Installation de pip

`pip` est le gestionnaire de paquets de Python, utilisé pour installer et gérer les bibliothèques Python. Si vous avez installé Python 3.4 ou une version ultérieure, `pip` est déjà inclus. Pour vérifier si `pip` est installé, dans l'invite de commande (CMD) tapez :

```sh
pip --version
```

Si `pip` n'est pas installé, vous pouvez l'installer en téléchargeant le script `get-pip.py` depuis [ce lien](https://bootstrap.pypa.io/get-pip.py) et en l'exécutant avec Python :

```sh
python get-pip.py
```

## Installation des bibliothèques Python sur Visual Studio Code sur Windows

**Étape 1** : Ouvrir votre dossier de projet dans Visual Studio Code

![Dossier](ouvrir_dossier.png?width=25vw)

**Étape 2** : Ouvrir le **Terminal**

Dans Visual Studio Code, cliquer sur l'onglet `Terminal` en haut de l'écran, puis sur `Nouveau terminal`. 

![Nouveau Terminal](terminal.png?width=25vw)

Cela ouvrira une nouvelle fenêtre de terminal en bas de l'écran.

![Terminal](new_terminal.png?width=25vw)

**Étape 3** : Installer les bibliothèques

Dans la fenêtre du Terminal (en bas de l'écran), taper la commande suivante pour installer les trois bibliothèques :

![Commande pip](pip.png?width=25vw)

```bash
pip install pandas matplotlib numpy
```

Cela téléchargera et installera les dernières versions des bibliothèques.


## Installation des bibliothèques Python sur Visual Studio Code sur Mac

La seule différence est dans la commande `pip`. Au lieu de `pip`, il faut écrire `pip3`.

```bash
pip3 install pandas matplotlib numpy
```

## Vérification de l'installation

Pour vérifier que les bibliothèques ont été correctement installées, vous pouvez importer les bibliothèques dans votre code, puis vérifier les versions installées :

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.__version__
plt.__version__
np.__version__
```
Si aucune erreur n'est affichée, cela signifie que les bibliothèques ont été installées avec succès.

## Résolution des problèmes courants

- **Problème : `pip` n'est pas reconnu comme une commande interne ou externe.**
  - Solution : Assurez vous que le chemin vers le dossier `Scripts` de Python est ajouté à la variable d'environnement PATH.

- **Problème : Erreur d'installation due à des permissions.**
  - Solution : Exécutez l'invite de commande en tant qu'administrateur.

- **Problème : Conflits de versions.**
  - Solution : Utilisez des environnements virtuels pour isoler les dépendances de votre projet. Vous pouvez créer un environnement virtuel avec `venv` :
    ```sh
    python -m venv myenv
    myenv\Scripts\activate
    ```