import sqlite3
from passwords_manage import *
from datetime import datetime
import os
from password_encryption import *

cwd = os.getcwd()
path_db = os.path.join(cwd,'Data_Base\\Pass_Manager.db')
db = sqlite3.connect(path_db)
cursor = db.cursor()



def Select_user_data(user_id,MasterPassword):

	cursor.execute("SELECT * FROM  Passwords WHERE UserID = ?",[(user_id)] )
	rezults = cursor.fetchall()

	try:
		for i in range(0,len(rezults)):
			rezults[i] = list(rezults[i])
			rezults[i][4] = decrypt(MasterPassword,rezults[i][4])

	except :
		pass

	return rezults


def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)



if __name__ == '__main__':


	ps = 'Test1234'
	data = Select_user_data(8,ps)
	for el in data:
		print(el)

