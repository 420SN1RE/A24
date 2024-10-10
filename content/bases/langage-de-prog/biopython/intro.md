+++
title = "Introduction à Biopython"
weight = 2
+++

## Présentation de Biopython

Biopython est une collection de bibliothèques Python conçues pour faciliter le travail en bioinformatique. Il offre des outils pour manipuler des séquences biologiques, accéder à des bases de données biologiques, effectuer des analyses de séquences, et bien plus encore. Biopython est largement utilisé par les bioinformaticiens pour automatiser et simplifier les tâches courantes en biologie computationnelle.

## Installation et configuration

Pour commencer à utiliser Biopython, vous devez d'abord l'installer. Voici comment procéder :

1. **Installation via pip** :
   ```bash
   pip install biopython
   ```

2. **Vérification de l'installation** :
   Après l'installation, vous pouvez vérifier que Biopython est correctement installé en important le module dans un script Python :
   ```python
   import Bio
   print(Bio.__version__)
   ```

3. **Configuration de l'environnement** :
   Assurez-vous que votre environnement de développement est configuré pour utiliser Biopython. Vous pouvez utiliser des environnements virtuels pour isoler vos projets :
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # Sur Windows, utilisez `myenv\Scripts\activate`
   pip install biopython
   ```

### Aperçu des fonctionnalités principales

Biopython offre une multitude de fonctionnalités. Voici un aperçu des plus courantes :

1. **Manipulation de séquences** :
   Biopython permet de lire, écrire et manipuler des séquences biologiques. Voici un exemple simple de lecture d'un fichier FASTA :
   ```python
   from Bio import SeqIO

   for record in SeqIO.parse("example.fasta", "fasta"):
       print(record.id)
       print(record.seq)
   ```

2. **Accès aux bases de données** :
   Vous pouvez accéder à des bases de données biologiques en ligne, comme NCBI, pour télécharger des séquences et des informations. Par exemple, pour télécharger une séquence à partir de NCBI :
   ```python
   from Bio import Entrez

   Entrez.email = "your.email@example.com"
   handle = Entrez.efetch(db="nucleotide", id="NM_001301717", rettype="gb", retmode="text")
   record = handle.read()
   print(record)
   ```

3. **Analyse de séquences** :
   Biopython offre des outils pour analyser des séquences, comme le calcul du contenu en GC :
   ```python
   from Bio.SeqUtils import gc_fraction

   seq = "AGCTATAG"
   print(gc_fraction(seq))
   ```

## Exercices

1. **Exercice 1 : Installation de Biopython**
   - Installez Biopython sur votre machine.
   - Vérifiez l'installation en imprimant la version de Biopython.

2. **Exercice 2 : Lecture de séquences**
   - Téléchargez un fichier FASTA d'exemple.
   - Écrivez un script Python pour lire et afficher les séquences du fichier.

3. **Exercice 3 : Accès à NCBI**
   - Utilisez Biopython pour télécharger une séquence génomique à partir de NCBI.
   - Affichez les informations de la séquence téléchargée.

4. **Exercice 4 : Analyse de séquences**
   - Écrivez un script pour calculer le contenu en GC d'une séquence donnée.
   - Testez votre script avec différentes séquences.
