import mysql.connector
from database import create_db, create_tables, create_categories, fill_products
from constants import cat_size, template


def update_database(mycursor, mydb):
    create_db(mycursor)
    create_tables(mycursor)
    create_categories(mycursor, mydb)
    fill_products(mycursor, mydb)

#_________________________________________________
#
#               CATEGORY CHOICE
#_________________________________________________


def cat_choice(mycursor):
	cat_choice = "\n"
	mycursor.execute("SELECT * FROM Categories")
	results = mycursor.fetchall()
	for result in results:
		cat_choice += (str(result[0]) + ": " + result[1] + "\n")
	cat_choice += '\nChose your category:\n'
	return cat_choice, results[-1][0]

def cat_loop(mycursor):
    choice, nb_cat = cat_choice(mycursor)
    while True:
        user_cat = input(choice)
        if user_cat.isdigit() and 1 <= int(user_cat) <= nb_cat:
            prod_loop(mycursor, user_cat)
            break
        else:
            print("\nERREUR: Commande inconnue\n")

#_________________________________________________
#
#               PRODUCT CHOICE
#_________________________________________________


def prod_choice(mycursor, user_answer):
    request = "SELECT name FROM Products WHERE cat_id = %s"
    user_cat = (user_answer,)
    mycursor.execute(request, user_cat)
    results = mycursor.fetchall()
    prod_choice = ""
    i = 1
    for result in results:
        prod_choice += (str(i) + ": " + result[0] + "\n")
        i += 1
    prod_choice += '\nChose your product:\n'
    return prod_choice, i - 1

def prod_loop(mycursor, user_cat):
    choice, nb_prod = prod_choice(mycursor, user_cat)
    while True:
        user_prod = input(choice)
        if user_prod.isdigit() and 1 <= int(user_prod) <= nb_prod:
            result = show_result(mycursor, user_cat, user_prod)
            print(result)
            save_sub_loop(mycursor)
            break
        else:
            print("\nERREUR: Commande inconnue\n")

#_________________________________________________
#
#           SHOW PRODUCT AND SUBSTITUTE
#_________________________________________________


def show_product(mycursor, user_cat, user_prod):
    prod_id = (int(user_cat) - 1) * cat_size + int(user_prod)
    request = "SELECT name, grade, store, product_url FROM Products WHERE id = %s"
    value = (prod_id,)
    mycursor.execute(request, value)
    result = mycursor.fetchone()
    prod_grade = result[1]
    product = formate_item(result)
    return product, prod_grade

def show_substitute(mycursor, user_cat, prod_grade):
    request = "SELECT name, grade, store, product_url FROM Products WHERE cat_id = %s ORDER BY grade ASC"
    value = (user_cat,)
    mycursor.execute(request, value)
    result = mycursor.fetchone()
    if result[1] != prod_grade:
        substitute = formate_item(result)
    else:
        substitute = "\nPas de meilleur produit à proposer\n"
    return substitute

def formate_item(result):
    text = "----------\nNom : {}\nNutriscore : {}\nMagasin : {}\nLien internet : {}\n----------\n"
    formated_text = text.format(result[0], result[1], result[2], result[3])
    return formated_text

def show_result(mycursor, user_cat, user_prod):
    request = "SELECT name FROM Categories WHERE id = %s"
    value = (user_cat,)
    mycursor.execute(request, value)
    category = mycursor.fetchone()
    show_cat = "\nCatégorie : {}\n".format(category[0])
    product, prod_grade = show_product(mycursor, user_cat, user_prod)
    substitute = show_substitute(mycursor, user_cat, prod_grade)
    result = show_cat + template.format(product, substitute)
    return result


#_________________________________________________
#
#               SAVE SUBSTITUTE
#_________________________________________________

def save_sub_loop(mycursor):
    while True:
        user_answer = input("Désirez-vous ajouter ce substitut à vos favoris ? [o/n]\n")
        if user_answer == "o":
            print("\nSubstitut enregistré\n")
            break
        elif user_answer == "n":
            break
        else:
            print("\nERREUR: Commande inconnue\n")
