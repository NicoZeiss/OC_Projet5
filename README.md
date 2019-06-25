# OC_Projet5 : Utilisez les données publiques de l'OpenFoodFacts

Voici le repository concernant le projet 5 du parcours Développeur d'application - Python

Présentation du projet :

Réalisation d'un programme qui permettra à l'utilisateur de consulter une base de données de produits alimentaires de la grande distribution. Le programme proposera à l'utilisateur un substitut plus sain, aux produits sélectionnés. Il pourra alors les ajouter en favoris.
La base de données consultée provient du site OpenFoodFacts.

Le parcours utilisateur :

Lorsque l'utilisateur ouvre le programme, 4 choix s'offrent à lui :
- 1 : Rechercher un aliment
- 2 : Consulter les favoris
- 3 : Mettre à jour la base de données
- 4 : Quitter le programme

Si l'utilisateur choisi la première option :
- une liste de 10 catégories de produits s'affiche, il doit en sélectionner une (en renseignant le chiffre correspondant).
- Ainsi, une liste de 50 produits appartenants à la catégorie s'affiche, il doit sélectionner un produit (en renseignant le chiffre correspondant).
- Le produit choisi s'affiche dans la console, avec quelques informations (nom du produit, son nutriscore, un magasin où l'acheter, l'URL du produit sur le site OFF).
- En-dessous, un substitut est proposé, avec les mêmes informations. Un substitut est proposé dans le cas où il existe un produit de la même catégorie avec un meilleur nutriscrore.
- L'utilisateur a le choix d'enregistrer le substitut et le produit en favoris [o/n]

Si l'utilisateur choisi la seconde option :
- la liste des favoris enregistrés s'affiche, il doit en sélectionner un (en renseignant le chiffre correspondant).
- Le substitut, et le produit initialement recherché s'affichent dans la console, avec leurs informations relatives.
- L'utilisateur peut ensuite revenir au menu principal ou choisir de consulter un autre substitut.

Si l'utilisateur choisi la troisème option :
- La base de donnée est mise à jour.
- Par exemple, si l'utilisateur souhaite ajouter des catégories au programme, il doit ouvrir le fichier constants.py, rajouter le nom de la catégorie dans la liste 'categories', et sélectionner l'option 3 au lancement du programme.

Si l'utilisateur choisi la quatrième option :
- Le programme se ferme

Fonctionnalités :

- La recherche d'aliments est faite dans la base OpenFoodFacts
- L'utilisateur intéragit avec le program directement depuis la console
- Lorsque l'utilisateur entre un caractère qui n'est pas prévu dans les choix proposés, le programme affiche une erreur, et le choix est proposé à nouveau
- Les requêtes sur la BdD sont faites sur une base MySQL

Pré-requis :

Les logiciels/modules nécessaires (ainsi que leur version) sont renseignés dans le document requirements.txt

Il est nécessaire de créer un utilisateur et de renseigner les informations de connexion :
- Se connecter à MySQL : sudo mysql
- Créer un utilisateur : CREATE USER 'USERNAME'@'localhost' IDENTIFIED BY 'MOTDEPASSE';
- Donner les doits de modification à l'utilisateur : GRANT ALL PRIVILEGES ON projet5.* TO 'USERNAME'@'localhost';
(USERNAME et MOTDEPASSE sont les identifiants à choisir à la convenance de l'utilisateur)
- Ajouter un fichier IDs.py au dossier OC_Projet5
- Ecrire dans IDs.py : username = 'USERNAME'
pw = 'MOTDEPASSE'
- Au premier lancement du programme, choisir l'option 3 pour créer la base de donnée

Lancement de l'application :

Pour lancer le programme, il suffit d'exécuter le fichier program.py dans le dossier OC_Projet5 : python3 program.py

