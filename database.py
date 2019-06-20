import mysql.connector
from classes import Category, Product
from constants import categories


def create_db(mycursor):
    '''We create our database, if it dosen't exist'''

    mycursor.execute("DROP DATABASE IF EXISTS projet5")
    mycursor.execute("CREATE DATABASE projet5")
    mycursor.execute("USE projet5")

def create_tables(mycursor):
    '''We create 3 tables in our database, if they don't exist'''

    # Table Categories
    mycursor.execute("CREATE TABLE IF NOT EXISTS Categories (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, name VARCHAR(45) NOT NULL, PRIMARY KEY (id)) ENGINE=INNODB")
    # Table Products
    mycursor.execute("CREATE TABLE IF NOT EXISTS Products (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, code BIGINT UNSIGNED NOT NULL, name VARCHAR(100) NOT NULL, store VARCHAR(100), cat_id SMALLINT UNSIGNED, grade CHAR(1) NOT NULL, product_url TEXT, PRIMARY KEY (id), CONSTRAINT fk_cat_id FOREIGN KEY (cat_id) REFERENCES Categories(id)) ENGINE=INNODB")
    #Table Favorite
    mycursor.execute("CREATE TABLE IF NOT EXISTS Favorite (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, code BIGINT UNSIGNED NOT NULL, name VARCHAR(100) NOT NULL, store VARCHAR(100) NOT NULL, cat_id SMALLINT UNSIGNED NOT NULL, grade CHAR(1), product_url TEXT, PRIMARY KEY (id)) ENGINE=INNODB")


def create_categories(mycursor, mydb):
    for category in categories:
        new_cat = Category(category)
        new_cat.insert_into_db(mycursor, mydb)

def fill_products(mycursor, mydb):
    for category in categories:
        new_cat = Category(category)
        new_cat.create_product_list()
        cat_list = new_cat.product_list
        for i in range(0, len(cat_list)):
            new_prod = Product(cat_list[i], category)
            new_prod.create_prod()
            new_prod.save_prod(mycursor, mydb)
        print(category + " updated: " + str(len(cat_list)) + " products")
