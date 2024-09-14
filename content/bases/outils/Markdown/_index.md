+++
title = "MarkDown"
weight = 187
+++

![Markdown](markdown.png)

## Introduction au Markdown dans Jupyter Notebook

Markdown est un langage de balisage léger qui vous permet de formater du texte en utilisant une syntaxe simple. Dans Jupyter Notebook, vous pouvez utiliser des **cellules Markdown** pour ajouter des titres, des listes, des liens, des images, et bien plus encore.

## Comment créer une cellule Markdown

1. **Créer une nouvelle cellule** : Cliquez sur le bouton "+" dans la barre d'outils pour ajouter une nouvelle cellule.
2. **Changer le type de cellule** : Cliquez sur le menu déroulant "Code" dans la barre d'outils et sélectionnez "Markdown". Vous pouvez également utiliser le raccourci clavier `Esc` puis `M`.
3. **Écrire du texte en Markdown** : Tapez votre texte en utilisant la syntaxe Markdown.
4. **Exécuter la cellule** : Appuyez sur `Shift + Enter` pour exécuter la cellule et afficher le texte formaté.


## Les bases du Markdown

1. **Titres et sous-titres**:

   Utilisez les dièses `#` pour créer des titres. Le nombre de dièses indique le niveau du titre.

   ```markdown
   # Titre de niveau 1
   ## Titre de niveau 2
   ### Titre de niveau 3
   ```

2. **Texte en gras et en italique**:

   Pour mettre du texte en **gras**, encadrez-le avec deux astérisques `**` ou deux tirets bas `__`.

   ```markdown
   **texte en gras**
   __texte en gras__
   ```

   Pour mettre du texte en *italique*, encadrez-le avec un astérisque `*` ou un tiret bas `_`.

   ```markdown
   *texte en italique*
   _texte en italique_
   ```

   Pour mettre du texte en **gras** et en *italique*, encadrez-le avec trois astérisques `***` ou trois tirets bas `___`.

   ```markdown
   ***Gras et italique*** 
   ___Gras et italique___

3. **Texte souligné**

   En Markdown, il n'y a pas de syntaxe native pour souligner du texte. Cependant, vous pouvez utiliser des balises HTML pour obtenir cet effet. Voici comment faire :

   ```markdown
   <u>Texte souligné</u>
   ```

4. **Listes**:

   **Listes à puces**:

     Utilisez des tirets `-`, des astérisques `*` ou des signes plus `+` pour créer des listes à puces.

     ```markdown
     - Élément 1
     - Élément 2
     - Élément 3
     ```

   **Listes numérotées**:

     Utilisez des chiffres suivis d'un point pour créer des listes numérotées.

     ```markdown
     1. Premier élément
     2. Deuxième élément
     3. Troisième élément
     ```

5. **Liens et images**:

   Pour insérer un lien, utilisez la syntaxe suivante :

   ```markdown
   [Texte du lien](URL_du_lien)
   ```

   Pour insérer une image, utilisez la syntaxe suivante :

   ```markdown
   ![Texte alternatif](URL_de_l'image)
   ```

6. **Blocs de code**:

   Utilisez des accents graves ` (backticks) pour insérer du code en ligne :

   ```markdown
   `print("Hello, World!")`
   ```

7. **Tableaux**:

   Créez des tableaux en utilisant des barres verticales `|` et des traits d'union `-` pour délimiter les en-têtes et les colonnes :

   ```markdown
   | En-tête 1 | En-tête 2 |
   |-----------|-----------|
   | Cellule 1 | Cellule 2 |
   | Cellule 3 | Cellule 4 |
   ```

8. **Citations**:

   Utilisez le symbole `>` pour créer des citations.

   ```markdown
   > Ceci est une citation.
   ```

9. **Formules mathématiques**:

   Utilisez LaTeX pour écrire des formules mathématiques. Encadrez vos formules avec des signes dollar `$`.
   
```markdown
   $E = mc^2$
   ```

10. **Texte barré**:

   Utilisez deux tildes `~~` pour barrer du texte.
  
   ```markdown
   ~~texte barré~~
   ```

11. **Blocs de texte surligné**:

   Utilisez trois accents graves `^^^` pour surligner des blocs de texte.

   ```markdown
   ^^^markdown
   ```

## Exemples pratiques

### Exemple de titre et de paragraphe

```markdown
# Mon chapitre sur le Markdown

Bienvenue dans ce chapitre sur le Markdown dans Jupyter Notebook. Vous apprendrez à formater du texte facilement.
```

### Exemple de liste et de lien

```markdown
## Liste des sujets abordés

- Introduction au Markdown
- Syntaxe de base
	- Les titres
	- Texte en gras et en italique
	- Les listes
- Exemples pratiques
- [Documentation officielle](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html)
```

### Exemple d'image et de bloc de code

```markdown
## Exemple d'image

![Logo Jupyter](https://jupyter.org/assets/main-logo.svg)

## Exemple de code Python

```python
def salut(nom):
    return f"Hello, {nom}!"

print(salut("world"))
```

## Vidéo YouTube

[Créer des cellules Markdowns dans Jupyter Notebook](https://youtu.be/jyVnqr44mtE?si=jFdhyUAzv5VQ6OCz)