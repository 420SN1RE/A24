+++
title = "Installation des extensions dans VS Code"
weight = 1.4
+++

![Installation librairies sur VS code](install-lib-vsc.jpeg?width=25vw)

Pour installer les extensions comme Python, Pandas, Numpy, Matplotlib et SciPy dans Visual Studio Code, suivez ces étapes :

1. **Ouvrir Visual Studio Code**

2. **Installer l'extension Python** :
    - Cliquez sur l'icône des extensions dans la barre d'activité à gauche (elle ressemble à quatre carrés) ou utilisez le raccourci `Ctrl+Shift+X`.
    - Recherchez **Python** et installez l'extension officielle développée par Microsoft.

3. **Ouvrir un terminal intégré** :
    - Allez dans le menu `Terminal` et sélectionnez `Nouveau terminal` (ou utilisez le raccourci `Ctrl+`).

4. **Installer les bibliothèques Python** :
    - Dans le terminal, utilisez les commandes `pip` pour installer les bibliothèques nécessaires. Voici les commandes pour chaque bibliothèque :
        ```sh
        pip install numpy
        pip install pandas
        pip install matplotlib
        pip install scipy
        ```

5. **Vérifier l'installation** :
    - Vous pouvez vérifier que les bibliothèques sont correctement installées en créant un nouveau fichier Python et en essayant d'importer les bibliothèques :
        ```python
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        import scipy
        ```

6. **Installer d'autres extensions utiles** : Vous pouvez également installer d'autres extensions utiles pour le développement Python, comme `Jupyter` pour travailler avec des notebooks Jupyter, et `Python Docstring Generator` pour générer des docstrings.


**Référence** : [How to install Python Libraries in Visual Studio Code](https://dev.to/emminex/how-to-install-python-libraries-in-visual-studio-code-38i1)

