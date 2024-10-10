+++
title = "Manipulation de Séquences"
weight = 2
+++


## Lecture et écriture de séquences

Biopython facilite la lecture et l'écriture de séquences à partir de différents formats de fichiers biologiques comme FASTA, GenBank, etc.

**Exemple : Lecture d'un fichier FASTA**
```python
from Bio import SeqIO

# Lecture d'un fichier FASTA
for record in SeqIO.parse("example.fasta", "fasta"):
    print(f"ID: {record.id}")
    print(f"Séquence: {record.seq}")
    print(f"Description: {record.description}")
```

**Exemple : Écriture dans un fichier FASTA**
```python
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

# Création d'un objet SeqRecord
record = SeqRecord(
    Seq("AGTACACTGGT"),
    id="example",
    description="Exemple de séquence"
)

# Écriture dans un fichier FASTA
SeqIO.write(record, "output.fasta", "fasta")
```

## Opérations de base sur les séquences

Biopython permet d'effectuer diverses opérations sur les séquences, telles que la traduction, la transcription et la complémentarité.

**Exemple : Traduction d'une séquence d'ADN en protéine**
```python
from Bio.Seq import Seq

# Séquence d'ADN
dna_seq = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")

# Traduction en protéine
protein_seq = dna_seq.translate()
print(protein_seq)
```

**Exemple : Transcription d'une séquence d'ADN en ARN**
```python
# Transcription en ARN
rna_seq = dna_seq.transcribe()
print(rna_seq)
```

**Exemple : Obtention de la séquence complémentaire**
```python
# Séquence complémentaire
complement_seq = dna_seq.complement()
print(complement_seq)

# Séquence complémentaire inverse
reverse_complement_seq = dna_seq.reverse_complement()
print(reverse_complement_seq)
```

## Alignement de séquences

L'alignement de séquences est une technique utilisée pour identifier les régions de similarité entre des séquences biologiques. Biopython utilise des outils comme ClustalW et MUSCLE pour effectuer ces alignements.

**Exemple : Alignement de séquences avec ClustalW**
```python
from Bio.Align.Applications import ClustalwCommandline

# Chemin vers l'exécutable ClustalW et le fichier d'entrée
clustalw_exe = "/path/to/clustalw2"
in_file = "example.fasta"

# Commande ClustalW
clustalw_cline = ClustalwCommandline(clustalw_exe, infile=in_file)
stdout, stderr = clustalw_cline()
print(stdout)
```

**Exemple : Lecture d'un alignement**
```python
from Bio import AlignIO

# Lecture d'un fichier d'alignement
alignment = AlignIO.read("example.aln", "clustal")
print(alignment)
```

## Exercices

1. **Exercice 1 : Lecture et écriture de séquences**
   - Téléchargez un fichier FASTA contenant plusieurs séquences.
   - Écrivez un script pour lire et afficher chaque séquence avec son ID et sa description.
   - Créez une nouvelle séquence et écrivez-la dans un fichier FASTA.

2. **Exercice 2 : Opérations sur les séquences**
   - Écrivez un script pour traduire une séquence d'ADN en protéine.
   - Transcrivez une séquence d'ADN en ARN.
   - Obtenez la séquence complémentaire et la séquence complémentaire inverse d'une séquence d'ADN.

3. **Exercice 3 : Alignement de séquences**
   - Utilisez ClustalW pour aligner plusieurs séquences d'ADN.
   - Lisez et affichez l'alignement obtenu.
   - Analysez les régions de similarité entre les séquences alignées.
