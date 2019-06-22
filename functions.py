import mysql.connector
from database import create_db, create_tables, create_categories, fill_products



def update_database(mycursor, mydb):
    create_db(mycursor)
    create_tables(mycursor)
    create_categories(mycursor, mydb)
    fill_products(mycursor, mydb)

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
        user_answer = input(choice)
        if user_answer.isdigit() and 1 <= int(user_answer) <= nb_cat:
            prod_loop(mycursor, user_answer)
            break
        else:
            print("\nERROR: Invalid Input\n")

def product_choice(mycursor, user_answer):
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

def prod_loop(mycursor, user_answer):
    choice, nb_prod = product_choice(mycursor, user_answer)
    while True:
        user_prod = input(choice)
        if user_prod.isdigit() and 1 <= int(user_prod) <= nb_prod:
            print("GG")
            break
        else:
            print("\nERROR: Invalid Input\n")

