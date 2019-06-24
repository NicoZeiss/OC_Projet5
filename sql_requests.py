import mysql.connector

'''
Here are all the requests we'll use to interact with the DB
'''

def show_cat(mycursor):
    mycursor.execute("SELECT * FROM Categories")
    results = mycursor.fetchall()
    return results

def show_prod(mycursor, user_answer):
    request = "SELECT name FROM Products WHERE cat_id = %s"
    user_cat = (user_answer,)
    mycursor.execute(request, user_cat)
    results = mycursor.fetchall()
    return results

def select_prod(mycursor, prod_id):
    request = "SELECT name, grade, store, product_url FROM Products WHERE id = %s"
    value = (prod_id,)
    mycursor.execute(request, value)
    result = mycursor.fetchone()
    return result

def find_substitute(mycursor, user_cat):
    request = "SELECT name, grade, store, product_url, id FROM Products WHERE cat_id = %s ORDER BY grade ASC"
    value = (user_cat,)
    mycursor.execute(request, value)
    result = mycursor.fetchone()
    return result

def cat_name(mycursor, user_cat):
    request = "SELECT name FROM Categories WHERE id = %s"
    value = (user_cat,)
    mycursor.execute(request, value)
    category = mycursor.fetchone()
    return category

def show_subs_list(mycursor):
    mycursor.execute("SELECT name FROM Products INNER JOIN Favorite ON Products.id = Favorite.subs_id")
    results = mycursor.fetchall()
    return results

def show_favorite(mycursor, subs_id):
    request = ("SELECT name, grade, store, product_url FROM Products INNER JOIN Favorite ON Products.id = Favorite.subs_id WHERE Favorite.id = %s")
    value = (subs_id,)
    mycursor.execute(request, value)
    result = mycursor.fetchone()
    return result

def show_original_prod(mycursor, prod_id):
    request = ("SELECT name, grade, store, product_url FROM Products INNER JOIN Favorite ON Products.id = Favorite.prod_id WHERE Favorite.id = %s")
    value = (prod_id,)
    mycursor.execute(request, value)
    result = mycursor.fetchone()
    return result
