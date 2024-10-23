+++
title = 'Google Colab'
weight =  193
+++

![Google Colab](./colab.png?width=25vw)

**Google Colab**, ou ***Colaboratory***, est un service cloud gratuit proposé par Google, basé sur Jupyter Notebook. Colab permet d'exécuter du code Python directement dans le navigateur sans nécessiter de configuration préalable, tout en offrant un accès gratuit aux processeurs graphiques (**GPU** ou _Graphics Processing_), pour accélérer les calculs.

## Accéder à Google Colab

Pour commencer à utiliser Google Colab, suivez ces étapes simples :

### Via le site de Google Colab

1. Allez sur le site: [Google Colab](https://colab.research.google.com/).
2. Cliquez sur le bouton **Open Colab**.
3. Si la fenêtre **Ouvrir le notebook** s'ouvre, cliquez sur le bouton **+ Nouveau notebook** pour créer un nouveau notebook. Sinon, une fois sur l'interface de Colab, vous pouvez créer un nouveau notebook en utilisant le menu **Fichier** et en sélectionnant **Nouveau notebook**.

![Nouveau notebook](./nouveau-notebook.png?width=40vw)

![Menu Fichier](./menu-fichier.png?width=40vw)

Les notebooks Colab permettent d'écrire et d'exécuter du code Python. Par exemple, pour exécuter une cellule de code, cliquez dessus et appuyez sur le bouton de lecture ou utilisez le raccourci clavier `Ctrl+Entrée`.

### Via votre compte Google Drive

1. Ouvrez votre compte **Google Drive**, cliquez sur **Nouveau**, puis sur **Plus** et sélectionnez ***Google Colaboratory***.

![Ouvrir Colab via Google Drive](./drive-colab.png?width=40vw)

## Utilisation des bibliothèques Python

Colab permet d'utiliser des bibliothèques populaires pour l'analyse et la visualisation des données. Par exemple, pour générer des données aléatoires avec `NumPy` et les visualiser avec `Matplotlib` :

```python
import numpy as np
import matplotlib.pyplot as plt

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]
plt.figure(figsize=(10, 6))
plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)
plt.show()
```

## Collaboration et partage

Les notebooks Colab sont enregistrés dans votre compte Google Drive, ce qui facilite le partage et la collaboration. Vous pouvez partager vos notebooks avec d'autres utilisateurs, qui peuvent les commenter ou les modifier.

## Utiliser Colab

[Lire ce notebook](https://colab.research.google.com/notebooks/intro.ipynb)

