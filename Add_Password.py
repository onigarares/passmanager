import sqlite3
from passwords_manage import *
from datetime import datetime
import os
from password_encryption import *

cwd = os.getcwd()
path_db = os.path.join(cwd,'Data_Base\\Pass_Manager.db')
db = sqlite3.connect(path_db)
cursor = db.cursor()

def gen_password():

	return generate_password()


def Add_Password_db(user_id,username,site,added_password,MasterPassword):
	added_password_en = encrypt(MasterPassword,added_password)
	insert = ('INSERT INTO Passwords (UserID,Aplication,Username,Password,DateAded) VALUES(?,?,?,?,?)')
	cursor.execute(insert,(user_id,site,username,added_password_en,datetime.now()))
	db.commit()




if __name__ == '__main__':

	user_id = '8'
	username = 'UserGreu'
	site = 'sitedemanelisti.com'
	added_password = 'PArolaMEaSecreta'
	MasterPassword = 'Test1234'
	print(gen_password())
	#Add_Password_db(user_id,username,site,added_password,MasterPassword)