## petit programme de scrapping

### Description du programme
C’est un programme qui va scraper une [boutique de livre en ligne](http://books.toscrape.com/).
Il va récolter plusieurs infos telles que le titre du livre,
sa description, ... et mettre ces infos dans un fichier csv qui a le nom de la category.
Il va aussi produire un dossier qui a le nom de la category
et y mettre toutes les images de couverture des livres de la category.

### Étape 1 : installation de python3
Si vous avez python3 installé, sautez cette étape.  
Pour lancer le programme, vous devez avoir python3 installé.  
Visitez ce [lien](https://www.python.org/downloads/) et suivez les étapes d’installation

### Étape 2 : Création d’un environnement virtuel en python
Télécharger tous les fichiers du dépôt git et mettez dans un dossier spécifique.
Dans ce même dossier, il va falloir créer un environnement virtuel dans lequel
on va installer les modules nécessaires. 
La liste de ces modules se trouve dans le requirement.txt.  
Pour créer cet environnement, cliquez sur ce [lien](https://docs.python.org/fr/3/library/venv.html) et suivez les 
étapes.

### Étape 3 : installer les modules nécessaires
À l’aide d’un terminal, installez pip. 
* Pour macOS, tapez : 
  - sudo easy_install pip
  - sudo pip install --upgrade pip
* Pour windows et Linux : pip est déjà installé

Ensuite, naviguez jusqu’au dossier où se trouve 
les fichiers téléchargés .py ainsi que votre environnement virtuel.  
Enfin, installez les modules avec pip comme suit :  
Tapez 'pip install [nom module]'

### Étape 4 : lancer le programme
Il faut lancer main.py uniquement.
Vous pouvez le faire dans le terminal.  
Si vous êtes situé dans le repertoire où se trouve les fichiers 
Tapez : 'Python main.py'  
Vous pouvez aussi lancer le programme dans votre éditeur
de code préféré.

Les fichiers csv et les dossiers images vont être
créés dans le repertoire courant.

Pour consulter idéalement ces fichiers, ouvrez
Excel→Données→Obtenir des données→À partir d’un fichier→À partir d’un fichier texte csv→sélectionner le fichier
que vous voulez consulter

Vous devrez sélectionner le(s) fichier(s) en question en naviguant
jusqu’à leur emplacement. 