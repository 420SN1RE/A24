+++
title = "Installation des bibliothèques Python"
weight = 1.3
+++

![Installation Python](install-lib.png?width=25vw)


## Installation des librairies Python sur Windows 10/11

Python est un langage de programmation puissant et polyvalent, largement utilisé pour l'analyse de données, la visualisation et les calculs scientifiques. Les librairies `pandas`, `matplotlib`, `numpy` et `scipy` sont parmi les plus populaires pour ces tâches. Ce chapitre vous guidera à travers les étapes nécessaires pour installer ces librairies sur un système Windows 10 ou 11.

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

`pip` est le gestionnaire de paquets de Python, utilisé pour installer et gérer les librairies Python. Si vous avez installé Python 3.4 ou une version ultérieure, `pip` est déjà inclus. Pour vérifier si `pip` est installé, dans l'invite de commande (CMD) tapez :

```sh
pip --version
```

Si `pip` n'est pas installé, vous pouvez l'installer en téléchargeant le script `get-pip.py` depuis [ce lien](https://bootstrap.pypa.io/get-pip.py) et en l'exécutant avec Python :

```sh
python get-pip.py
```

### Étape 3 : Installation des librairies

Une fois `pip` installé, vous pouvez installer les librairies `pandas`, `matplotlib`, `numpy` et `scipy` en utilisant les commandes suivantes dans l'invite de commande :

```sh
pip install pandas
pip install matplotlib
pip install numpy
pip install scipy
```

### Étape 4 : Vérification de l'installation

Pour vérifier que les librairies ont été correctement installées, vous pouvez ouvrir une session Python interactive en tapant `python` dans l'invite de commande, puis essayer d'importer chaque librairie :

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy
```
Si aucune erreur n'est affichée, cela signifie que les librairies ont été installées avec succès.

## Résolution des problèmes courants

- **Problème : `pip` n'est pas reconnu comme une commande interne ou externe.**
  - Solution : Assurez-vous que le chemin vers le dossier `Scripts` de Python est ajouté à la variable d'environnement PATH.

- **Problème : Erreur d'installation due à des permissions.**
  - Solution : Exécutez l'invite de commande en tant qu'administrateur.

- **Problème : Conflits de versions.**
  - Solution : Utilisez des environnements virtuels pour isoler les dépendances de votre projet. Vous pouvez créer un environnement virtuel avec `venv` :
    ```sh
    python -m venv myenv
    myenv\Scripts\activate
    ```