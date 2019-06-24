import mysql.connector

'''
Here are all the requests we'll use to interact with the DB
'''

def show_cat(mycursor):
    '''We select all items from Categories'''

    mycursor.execute("SELECT * FROM Categories")
    results = mycursor.fetchall()
    return results

def show_prod(mycursor, user_answer):
    '''We select all items countain in one category and display their name'''

    request = "SELECT name FROM Products WHERE cat_id = %s"
    user_cat = (user_answer,)
    mycursor.execute(request, user_cat)
    results = mycursor.fetchall()
    return results

def select_prod(mycursor, prod_id):
    '''We select all items from countain in one category, and display their informations'''

    request = "SELECT name, grade, store, product_url FROM Products WHERE id = %s"
    value = (prod_id,)
    mycursor.execute(request, value)
    result = mycursor.fetchone()
    return result

def find_substitute(mycursor, user_cat):
    '''We order all items from one category by grade ASC'''

    request = "SELECT name, grade, store, product_url, id FROM Products WHERE cat_id = %s ORDER BY grade ASC"
    value = (user_cat,)
    mycursor.execute(request, value)
    result = mycursor.fetchone()
    return result

def cat_name(mycursor, user_cat):
    '''We select the name of one category'''

    request = "SELECT name FROM Categories WHERE id = %s"
    value = (user_cat,)
    mycursor.execute(request, value)
    category = mycursor.fetchone()
    return category

def show_subs_list(mycursor):
    '''We select the name of all products saved in Favorite table'''

    mycursor.execute("SELECT name FROM Products INNER JOIN Favorite ON Products.id = Favorites.subs_id")
    results = mycursor.fetchall()
    return results

def show_favorite(mycursor, subs_id):
    '''We display of informations about one substitute saved as favorite'''

    request = ("SELECT name, grade, store, product_url FROM Products INNER JOIN Favorite ON Products.id = Favorites.subs_id WHERE Favorites.id = %s")
    value = (subs_id,)
    mycursor.execute(request, value)
    result = mycursor.fetchone()
    return result

def show_original_prod(mycursor, prod_id):
    '''We display of informations about one product saved as favorite'''

    request = ("SELECT name, grade, store, product_url FROM Products INNER JOIN Favorite ON Products.id = Favorites.prod_id WHERE Favorites.id = %s")
    value = (prod_id,)
    mycursor.execute(request, value)
    result = mycursor.fetchone()
    return result
