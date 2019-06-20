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
	return cat_choice
		
def nb_cat(mycursor):
	mycursor.execute("SELECT * FROM Categories")
	result = mycursor.fetchall()
	return result[-1][0]

def cat_loop(mycursor):
    choice = cat_choice(mycursor)
    while True:
        user_answer = input(choice)
        if user_answer.isdigit() and 1 <= int(user_answer) <= nb_cat(mycursor):
            prod = product_choice(mycursor, user_answer)
            print(prod)
            break
        else:
            print("\nERROR: Invalid Input")

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

    return prod_choice

