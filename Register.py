import sqlite3
from datetime import datetime
from passwords_manage import *
import tkinter
import os

cwd = os.getcwd()
path_db = os.path.join(cwd,'Data_Base\\Pass_Manager.db')
db = sqlite3.connect(path_db)
cursor = db.cursor()


def insert_user_to_db(username,passw):

    insert = ('INSERT INTO UserAccounts (UserName,MasterPass,DateSinged) VALUES(?,?,?)')
    cursor.execute(insert,(username,passw,datetime.now()))
    db.commit()
def register_check(username,pass1,pass2):
    msg_username = ''
    msg_pass1=''
    msg_pass2=''
    conf = True

    cursor.execute("SELECT UserName FROM UserAccounts WHERE UserName =?",[(username)])
    if username =='':
        msg_username = 'Pleaste type your username!'
        conf = False
    elif len(username) <4:
        msg_username = "Username to short!"
        conf = False
    elif cursor.fetchmany(1) :
        msg_username = 'User name already exists!'
        conf = False

    if strong_password(pass1) != 'PassOk':
        msg_pass1 = strong_password(pass1)
        conf = False
    else:
        msg_pass1 = 'Strong password!'

    if pass1 != pass2 :
        msg_pass2 = "Passwords don't match!"
        conf = False


    #Insert the user into the databse if the registration has succeed!!

    if conf == True :
        insert_user_to_db(username,hash_bcrypt(pass1))

    return [msg_username,msg_pass1,msg_pass2,conf]






if __name__ == '__main__':

    # u = 'usdsadasddd'
    # p1 = ''
    # p2 = 'laAla1'
    # print(register_check(u,p1,p2))

    #insert_user_to_db('onigarar','greagrea')
    pass
