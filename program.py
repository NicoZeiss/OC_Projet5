import mysql.connector
from IDs import username, pw
from update_db import update_database

# We log-in to our database
mydb = mysql.connector.connect(
    host = "localhost",
    user = username,
    passwd = pw)
mycursor = mydb.cursor()
mycursor.execute("USE projet5")



def main():
    user_answer = input("\n----------\nPressez 1 : pour chercher un aliment\nPressez 2 : pour consulter vos favoris\nPressez 3 : pour mettre à jour la base de données\n----------\n")
    if user_answer == '1':
        print("à venir")
        main()
    elif user_answer == '2':
        print("à venir")
        main()
    elif user_answer == '3':
        update_database(mycursor, mydb)
    else:
        print("ERROR: Commande inconnue")
        main()
    


if __name__ == "__main__":
    main()