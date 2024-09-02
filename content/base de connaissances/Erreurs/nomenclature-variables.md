+++
title= "Erreurs avec les noms des variables"
weight= 1
+++

![Opérateurs](../erreur-variables.jpeg?width=20vw)

## Pourquoi bien nommer les choses ?

La raison est simple, **on passe plus de temps a lire du code qu'a l'écrire**, donc pour se simplifier la tâche de lecture du code, quel que soit le langage de programmation, il est important de bien nommer les différentes variables, méthodes etc.

## Conventions de nommage en python

En plus des règles liées au langage qui mèneront à un problème d'exécution (par exemple, un nom de variable ne doit pas commencer par des chiffres), il existe un nombre de convention concernant le nommage en python.

https://peps.python.org/pep-0008/#naming-conventions
| Type                         | Public               |
| ---------------------------- | -------------------- |
| Packages                     | `lower_with_under`   |
| Modules                      | `lower_with_under`   |
| Classes                      | `CapWords`           |
| Exceptions                   | `CapWords`           |
| Fonctions                    | `lower_with_under()` |
| Constantes Global / Class    | `CAPS_WITH_UNDER`    |
| Variables Global / Class     | `lower_with_under`   |
| Variables d'Instance         | `lower_with_under`   |
| Nom de Methode               | `lower_with_under()` |
| Paramètres Function / Method | `lower_with_under`   |
| Variables locales            | `lower_with_under`   |

## La logique de nommage

Bien nommer, va au dela des règles et convention du langage.
- Être le plus explicite possible, écrivez un nom complet. Préférez `minutes` à `min`.
- Si vous avez du mal à donner un nom à votre fonction, il y a probablement un problème de logique dans votre fonction.