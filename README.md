# Solveur de Scrabble

#### Un simple solveur du jeu de Scrabble en Python

## Mises à jour
### 15/05/2020
Changement de méthode pour touver les mots  
Ancienne méthode: vérifier pour chaque permutation des lettres entrées si elle se trouve dans le dictionnaire. O(n!)  
Nouvelle méthode: vérifie pour chaque mot si il peut être composé avec les lettres entrées par l'utilisateur.  

## Installation
- Si ce n'est pas déjà fait, il faut installer le module unidecode 
```bash
pip install unidecode
```
- Ensuite
```bash
./data_extract.py
```
Quatre fichier vont etre créés (peut prendre du temps)

## Fichier binaires créés
 - "data" continent une liste de tout les mots présents dans "lexique.txt"
 - "data_first" continent tout les mots de "data" classés selon leur première lettre.
 - "data_first_two" continent tout les mots de "data" classés selon leur deux première lettre (aa, ab, ..., zz).
 - "data_last" contient tout les mots de "data" classés selon leur dernière lettre.

## Utilisation
  - Lancez le fichier "scrabble.py"
  - Le premier champs est pour les lettres que le joueur possède
  - Le deuxième champ est pour pour les lettres disponible sur le plateau
  - Le troisième champs est pour mettre une contrainte sur le début des mots cherchés
  - Le quatrième champs est pour mettre une contrainte sur la fin des mots cherchés
  - Les résultats s'affichent en bas du mot le plus long au plus court
