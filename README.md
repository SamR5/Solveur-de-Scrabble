# Solveur de Scrabble

#### Un simple solveur du jeu de Scrabble en Python

## Installation
Si ce n'est pas déjà fait, il faut installer le module unidecode
```bash
pip install unidecode
```

## Utilisation
  - Lancez le fichier "scrabble.py"
  - Le premier champs est pour les lettres que le joueur possède
  - Le deuxième champ est pour pour les lettres disponible sur le plateau
  - Le troisième champs est pour mettre une contrainte sur le début des mots cherchés
  - Le quatrième champs est pour mettre une contrainte sur la fin des mots cherchés
  - Les résultats s'affichent en bas du mot le plus long au plus court

## Mises à jour
### 16/05/2020
Optimisation de l'extraction des mots.  
Le chargement est fait à chaque démarrage, plus besoin de sauvegarde.  

### 15/05/2020
Changement de méthode pour touver les mots  
Ancienne méthode: vérifier pour chaque permutation des lettres entrées si elle se trouve dans le dictionnaire. O(n!)  
Nouvelle méthode: vérifie pour chaque mot si il peut être composé avec les lettres entrées par l'utilisateur.  
