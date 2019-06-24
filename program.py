import mysql.connector
from IDs import username, pw
from functions import update_database, cat_loop, favorite_loop
from constants import fonc_choice

# We log-in to our database
mydb = mysql.connector.connect(
    host = "localhost",
    user = username,
    passwd = pw)
mycursor = mydb.cursor(buffered=True)
mycursor.execute("CREATE DATABASE IF NOT EXISTS projet5")
mycursor.execute("USE projet5")



def main():
    # that's the main function, with the four main functionalities off our software
    while True:
        user_answer = input(fonc_choice)
        if user_answer == '1':
            cat_loop(mycursor, mydb)
        elif user_answer == '2':
            favorite_loop(mycursor)
        elif user_answer == '3':
            update_database(mycursor, mydb)
            print("\nBase de données à jour\n")
        elif user_answer == '4':
            break
        else:
            print("\nERREUR: Commande inconnue\n")
    


if __name__ == "__main__":
    main()