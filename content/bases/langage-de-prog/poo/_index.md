+++
title = "La programmation orientée objet (POO)"
weight = 9
+++

![POO](./poo.jpeg?width=25vw)

La programmation orientée objet (POO) est un concept clé en Python et dans de nombreux autres langages de programmation. Voici une introduction simple :

## Concepts de base de la POO en Python

### Classes et Objets

- **Classe** : Une classe est comme un plan ou un modèle pour créer des objets. Elle définit les attributs (données) et les méthodes (fonctions) que les objets créés à partir de cette classe auront.
- **Objet** : Un objet est une instance d'une classe. Par exemple, si `Chien` est une classe, alors `mon_chien` peut être un objet de cette classe.

```python
class Chien:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def aboyer(self):
        print("Woof!")

mon_chien = Chien("Rex", 5)
mon_chien.aboyer()  # Affiche "Woof!"
```

### Encapsulation

- L'encapsulation consiste à restreindre l'accès à certaines parties d'un objet. Cela se fait en utilisant des attributs privés (commençant par un underscore `_`) et des méthodes pour accéder et modifier ces attributs.

```python
class CompteBancaire:
    def __init__(self, solde):
        self._solde = solde

    def deposer(self, montant):
        self._solde += montant

    def retirer(self, montant):
        if montant <= self._solde:
            self._solde -= montant
        else:
            print("Fonds insuffisants")

    def afficher_solde(self):
        print(f"Solde: {self._solde}")

mon_compte = CompteBancaire(100)
mon_compte.deposer(50)
mon_compte.afficher_solde()  # Affiche "Solde: 150"
```

### Héritage

- L'héritage permet de créer une nouvelle classe à partir d'une classe existante. La nouvelle classe (classe dérivée) hérite des attributs et méthodes de la classe existante (classe de base).
```python
class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        pass

class Chien(Animal):
    def parler(self):
        print("Woof!")

class Chat(Animal):
    def parler(self):
        print("Meow!")

mon_chien = Chien("Rex")
mon_chat = Chat("Mimi")
mon_chien.parler()  # Affiche "Woof!"
mon_chat.parler()  # Affiche "Meow!"
```

### Polymorphisme

- Le polymorphisme permet d'utiliser une interface commune pour des objets de différentes classes. Par exemple, différentes classes peuvent avoir une méthode `parler`, mais chaque classe peut l'implémenter différemment.

```python
for animal in [mon_chien, mon_chat]:
    animal.parler()
```
