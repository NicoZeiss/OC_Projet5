import mysql.connector
from database import create_db, create_tables, create_categories, fill_products



def update_database(mycursor, mydb):
    create_db(mycursor)
    create_tables(mycursor)
    create_categories(mycursor, mydb)
    fill_products(mycursor, mydb)