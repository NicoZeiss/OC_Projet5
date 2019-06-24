import mysql.connector
from database import create_db, create_tables, create_categories, fill_products
from constants import cat_size, template, no_subs
from sql_requests import show_cat, show_prod, select_prod, find_substitute, cat_name, show_subs_list, show_favorite, show_original_prod
from classes import Substitute

'''
Here are all the main functions used into our software
'''

def update_database(mycursor, mydb):
    '''We update the database'''

    create_db(mycursor)
    create_tables(mycursor)
    create_categories(mycursor, mydb)
    fill_products(mycursor, mydb)

#_________________________________________________
#
#               CATEGORY CHOICE
#_________________________________________________


def cat_choice(mycursor):
    '''Display category list'''

	cat_choice = "\n"
    #sql request
	results = show_cat(mycursor)
	for result in results:
		cat_choice += (str(result[0]) + ": " + result[1] + "\n")
	cat_choice += '\nChoisissez votre catégorie :\n'
	return cat_choice, results[-1][0]

def cat_loop(mycursor, mydb):
    '''While user has not chose a category with a valid input, the loop is true'''

    choice, nb_cat = cat_choice(mycursor)
    while True:
        user_cat = input(choice)
        if user_cat.isdigit() and 1 <= int(user_cat) <= nb_cat:
            prod_loop(mycursor, user_cat, mydb)
            break
        else:
            print("\nERREUR: Commande inconnue\n")

#_________________________________________________
#
#               PRODUCT CHOICE
#_________________________________________________


def prod_choice(mycursor, user_answer):
    '''Display product list from the category chosen'''

    #sql request
    results = show_prod(mycursor, user_answer)
    prod_choice = ""
    i = 1
    for result in results:
        prod_choice += (str(i) + ": " + result[0] + "\n")
        i += 1
    prod_choice += '\nChoisissez votre produit:\n'
    return prod_choice, i - 1

def prod_loop(mycursor, user_cat, mydb):
    '''While user has not chose a product with a valid input, the loop is true'''

    choice, nb_prod = prod_choice(mycursor, user_cat)
    while True:
        user_prod = input(choice)
        if user_prod.isdigit() and 1 <= int(user_prod) <= nb_prod:
            result, subs, subs_id, prod_id = show_result(mycursor, user_cat, user_prod)
            print(result)
            save_subs_loop(mycursor, subs, subs_id, prod_id, mydb)
            break
        else:
            print("\nERREUR: Commande inconnue\n")

#_________________________________________________
#
#           SHOW PRODUCT AND SUBSTITUTE
#_________________________________________________


def show_product(mycursor, user_cat, user_prod):
    '''We formate the chosen product, and return the result'''

    prod_id = (int(user_cat) - 1) * cat_size + int(user_prod)
    #sql request
    result = select_prod(mycursor, prod_id)
    prod_grade = result[1]
    product = formate_item(result)
    return product, prod_grade, prod_id

def show_substitute(mycursor, user_cat):
    '''We formate the chosen substitute, and return the result'''

    #sql request
    result = find_substitute(mycursor, user_cat)
    subs_grade = result[1]
    subs_id = result[4]
    substitute = formate_item(result)
    return substitute, subs_grade, subs_id

def formate_item(result):
    '''Allows us to formate chosen products'''

    text = "----------\nNom : {}\nNutriscore : {}\nMagasin : {}\nLien internet : {}\n----------\n"
    formated_text = text.format(result[0], result[1], result[2], result[3])
    return formated_text

def show_result(mycursor, user_cat, user_prod):
    '''We display chosen product and substitute in the console'''

    category = cat_name(mycursor, user_cat)
    show_cat = "\nCatégorie : {}\n".format(category[0])
    product, prod_grade, prod_id = show_product(mycursor, user_cat, user_prod)
    substitute, subs_grade, subs_id = show_substitute(mycursor, user_cat)
    #Text is different if chosen product has not better substitute
    if prod_grade != subs_grade:
        result = show_cat + template.format(product, substitute)
        subs = True
    else:
        result = show_cat + template.format(product, no_subs)
        subs_id = prod_id
        subs = False
    return result, subs, subs_id, prod_id


#_________________________________________________
#
#               SAVE SUBSTITUTE
#_________________________________________________


def save_subs_loop(mycursor, subs, subs_id, prod_id, mydb):
    '''User has to chose if he wants to saved the result as favorite'''

    while True:
        user_answer = input("Désirez-vous ajouter ce produit à vos favoris ? [o/n]\n")

        if user_answer == "o":
            new_subs = Substitute(subs_id, prod_id)
            new_subs.add_to_db(mycursor, mydb)
            print("\nProduit enregistré\n")
            break
        elif user_answer == "n":
            break
        else:
            print("\nERREUR: Commande inconnue\n")


#_________________________________________________
#
#               SAVE SUBSTITUTE
#_________________________________________________

def favorite_list(mycursor):
    '''We display the favorite list'''

    #sql request
    results = show_subs_list(mycursor)
    subs_list = "\n"
    i = 1
    for result in results:
        subs_list += (str(i) + ": " + result[0] + "\n")
        i += 1
    subs_list += '\n\nChoisissez un produit à consulter :\n'
    return subs_list, i - 1

def display_result(favorite, original_prod):
    '''We formate chosen favorite and display the result in our console'''

    formated_fav = formate_item(favorite)
    formated_prod = formate_item(original_prod)
    print(("\nNotre suggestion :\n{}\nVotre choix initial :\n{}\n").format(formated_fav, formated_prod))


def favorite_loop(mycursor):
    '''User has to which favorite he wants to read'''

    subs_list, nb_subs = favorite_list(mycursor)
    while True:
        user_answer = input(subs_list)
        if user_answer.isdigit() and 1 <= int(user_answer) <= nb_subs:
            favorite = show_favorite(mycursor, user_answer)
            original_prod = show_original_prod(mycursor, user_answer)
            display_result(favorite, original_prod)
            go_back = input("\nPressez \'1\' pour consulter un autre favori, \'2\' pour revenir au menu principal\n")
            if go_back == '2':
                break
        else:
            print("\nERREUR: Commande inconnue\n")
