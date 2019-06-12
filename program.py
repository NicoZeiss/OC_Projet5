import mysql.connector
from IDs import username, pw
from database import create_db, create_tables

# We log-in to our database
mydb = mysql.connector.connect(
    host = "localhost",
    user = username,
    passwd = pw)
mycursor = mydb.cursor()
create_db(mycursor)
create_tables(mycursor)

def main():
    

if __name__ == "__main__":
    main()