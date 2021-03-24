import sqlite3
from passwords_manage import *
import os

cwd = os.getcwd()
path_db = os.path.join(cwd,'Data_Base\\Pass_Manager.db')
db = sqlite3.connect(path_db)


cursor = db.cursor()

def Login(username,pasword):
	pas_msg=''
	msg =''
	conf = True
	userID=''
	if username =='':
		msg ='Please type your username!'
		conf = False
		return [msg,conf,userID,pas_msg]
	if pasword == '':
		pas_msg = 'Please type your password!'
		conf = False
		return [msg,conf,userID,pas_msg]

	cursor.execute("SELECT UserID,MasterPass,UserName FROM UserAccounts WHERE UserName =?",[(username)])
	result  = cursor.fetchall()
	try:
		hashed = result[0][1]
		userID = result[0][0]
		if hash_bcrypt_match(pasword,hashed) == False :
			msg = 'Invalid username or password!'
			conf = False

	except (IndexError,TypeError):
		msg = 'Invalid username or password!'
		conf = False

	return [msg,conf,userID,pas_msg]


if __name__ == '__main__':

	pass

