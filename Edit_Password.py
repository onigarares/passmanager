import sqlite3
from passwords_manage import *
from datetime import datetime
import os
from password_encryption import *

cwd = os.getcwd()
path_db = os.path.join(cwd,'Data_Base\\Pass_Manager.db')
db = sqlite3.connect(path_db)
cursor = db.cursor()

def edit_data(password_id,edited_site,edited_username,edited_password,MasterPassword):

	edited_password = encrypt(MasterPassword,edited_password)
	edit = ('UPDATE Passwords SET Aplication = ?, Username = ?,Password = ?, DateAded = ? WHERE PasswordID = ?')
	cursor.execute(edit,(edited_site,edited_username,edited_password,datetime.now(),password_id))
	db.commit()
	#print('done')

def delete_password(password_id):
	delete = ("DELETE FROM Passwords WHERE PasswordID = ? ")
	cursor.execute(delete,[password_id])
	db.commit()


if __name__ == '__main__':

	delete_password(9)