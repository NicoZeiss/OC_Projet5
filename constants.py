# -*- coding: Utf-8 -*-
# Here are all the constants we'll use in our project


# URLs
api_url = 'https://fr.openfoodfacts.org/api/v0/product/'
product_url = 'https://fr.openfoodfacts.org/produit/'
cat_url = 'https://fr.openfoodfacts.org/categorie/'


# Categories
categories = ['boissons-energisantes', 'beignets-sucres', 'taboules', 
'pates-a-tartiner', 'flocons-de-cereales-', 'fromages-rapes', 'jambons-blancs', 
'chocolats-noirs', 'rillettes-de-viande', 'mayonnaises']

cat_size = 50

# Text
template = "\nVotre sélection :\n{}\nNotre suggestion :\n{}\n"
no_subs = "\nPas de meilleur produit à proposer\n"
fonc_choice = "\n----------\nPressez 1 : pour chercher un aliment\nPressez 2 : pour consulter vos favoris\nPressez 3 : pour mettre à jour la base de données\nPressez 4 : pour quitter le programme\n----------\n"
