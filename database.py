import mysql.connector
from classes import Category
from constants import categories

# def create_db(mycursor):
#     '''We create our database, if it dosen't exist'''

#     mycursor.execute("CREATE DATABASE IF NOT EXISTS projet5")
#     mycursor.execute("USE projet5")

# def create_tables(mycursor):
#     '''We create 3 tables in our database, if they don't exist'''

#     # Table Categories
#     mycursor.execute("CREATE TABLE IF NOT EXISTS Categories (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, name VARCHAR(30) NOT NULL, PRIMARY KEY (id)) ENGINE=INNODB")
#     # Table Products
#     mycursor.execute("CREATE TABLE IF NOT EXISTS Products (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, code BIGINT UNSIGNED NOT NULL, name VARCHAR(40) NOT NULL, store VARCHAR(20), cat_id SMALLINT UNSIGNED NOT NULL, grade CHAR(1), product_url TEXT, PRIMARY KEY (id), CONSTRAINT fk_cat_id FOREIGN KEY (cat_id) REFERENCES Categories(id)) ENGINE=INNODB")
#     #Table Favorite
#     mycursor.execute("CREATE TABLE IF NOT EXISTS Favorite (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, code BIGINT UNSIGNED NOT NULL, name VARCHAR(40) NOT NULL, store VARCHAR(20) NOT NULL, cat_id SMALLINT UNSIGNED NOT NULL, grade CHAR(1), product_url TEXT, PRIMARY KEY (id)) ENGINE=INNODB")


def fill_categories():
    for category in categories:
        new_cat = Category(category)
        new_cat.create_product_list()
        print(new_cat.product_list)

fill_categories()