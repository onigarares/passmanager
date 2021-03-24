import sqlite3
from datetime import datetime

db = sqlite3.connect('Pass_Manager.db')


cursor = db.cursor()

def create_UserAccounts():

    cursor.execute("""CREATE TABLE IF NOT EXISTS UserAccounts(
                UserID INTEGER PRIMARY KEY,
                UserName VARCHAR(50),
                FirstName Varchar(50),
                LastName Varchar(50),
                MasterPass VARCHAR (150),
                EmailAccount VARCHAR (100),
                DateSinged DATETIME

                )""")

def create_Passwords():

    cursor.execute("""CREATE TABLE IF NOT EXISTS Passwords(
                PasswordID INTEGER PRIMARY KEY,
                UserID INTEGER,
                Aplication VARCHAR (50),
                Username VARCHAR (50),
                Password VARCHAR (150),
                DateAded DATETIME
                ) """)




if __name__ == '__main__':
    #cursor.execute("DROP TABLE Passwords")
    parola_test ='gAAAAABgTAtfXlJ-YdDyL_9GMOSVR2lucaH7B0I0eVQy5AfLYZ3A-sSoH8SPmwZtRFKfUw0VrOR-E9nxyb9cAiXRAj8qYio4DQ=='
    create_UserAccounts()
    create_Passwords()

    #           INSERT in Password SELECT fom PASSWORDS


    # insert = ('INSERT INTO Passwords (UserID,Aplication,Username,Password,DateAded) VALUES(?,?,?,?,?)')
    # cursor.execute(insert,('8','aplicatie4','user4',parola_test,datetime.now()))
    # db.commit()
    # cursor.execute("DELETE FROM Passwords WHERE PasswordID = '1' ")
    # db.commit()
    cursor.execute("SELECT  * FROM Passwords ")


    #               SELECT FROM UserAccounts

    #cursor.execute("SELECT  * FROM UserAccounts ")
    
    for el in cursor:
        print(el)
        