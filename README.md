# Mc LetsGuy
**Projet 3 de la formation OpenClassrooms DA Python**

Réalisation du jeu qui va changer votre relation avec le video gaming. Comme pas mal de bonne chose, n'en abusez pas, mais amusez vous.

####Objectif
Réaliser un jeu de labyrinthe en Python ou le but sera de sortir du labyrinthe en ayant récuperé tous les objets nécessaires.
 
####Contraintes :
- Il n'y a qu'un seul niveau. La structure (départ, emplacement des murs, arrivée), devra être enregistrée dans un fichier pour la modifier facilement au besoin.
- MacGyver sera contrôlé par les touches directionnelles du clavier.
- Les objets seront répartis aléatoirement dans le labyrinthe et changeront d’emplacement si l'utilisateur ferme le jeu et le relance.
- La fenêtre du jeu sera un carré pouvant afficher 15 sprites sur la longueur.
- MacGyver devra donc se déplacer de case en case, avec 15 cases sur la longueur de la fenêtre !
- Il récupèrera un objet simplement en se déplaçant dessus.
- Le programme s'arrête uniquement si MacGyver a bien récupéré tous les objets et trouvé la sortie du labyrinthe. S'il n'a pas tous les objets et qu'il se présente devant le garde, il meurt (la vie est cruelle pour les héros).

####Installation :
- Clonez ou téléchargez le dépôt
- `pip3 install pipenv` installera `pipenv` si vous ne l'avez pas
- Depuis le dépôt créer l'environnement virtuel et installe les paquets requis `pipenv install`
- Activer l'environnement virtuel `pipenv shell`
- Lancez le jeu `python game.py`


###Remerciements
Ressources graphiques: Jesse Freeman - licence WTFPL - http://jessefreeman.com/

OpenClassrooms et leur équipe de mentor pour leur aide et soutien.