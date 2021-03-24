import hashlib
import re
import bcrypt
import random

def generate_password(mxc=4,mxs=4) :
	password = ''
	lower = 'abcdefghijklmnopqrstuvwxyz'
	upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	spec = '!@#$%^&*+<>.-_?'
	l_up = random.randrange(1,mxc)
	l_sp =random.randrange(1,mxs)
	l_pas = random.randrange(12,16)
	l_low = l_pas-l_sp-l_up
	list_up = [upper[random.randrange(0,len(upper))] for i in range(l_up)]
	list_sp = [spec[random.randrange(0,len(spec))] for i in range(l_sp)]
	list_low = [lower[random.randrange(0,len(lower))] for i in range(l_low)]
	password_list=list_up+list_low+list_sp
	random.shuffle(password_list)
	password = ''.join(password_list)

	return password

def generate_random_password ():
	start = random.randrange(8, 11,1)
	end = random.randrange(23,27,1)

	pas = hash_bcrypt('greugreugreu')+hash_bcrypt('cocojambo')
	#print(len(pas[start:end].decode()))
	return(pas[start:end].decode())



def hash_bcrypt(password):
	to_hash = bytes(password, 'utf-8')
	hashed = bcrypt.hashpw(to_hash,bcrypt.gensalt())

	return hashed


def hash_bcrypt_match(pass_insert, hashed):
	pass_insert = bytes(pass_insert, 'utf-8')
	#hashed = bytes(hashed, 'utf-8')
	if bcrypt.checkpw(pass_insert,hashed):
		return True
	else:
		return False


def shapass(password):

	shapass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

	return shapass






def strong_password(pas) :
	#message = 'Strong Password'
	if pas == '':
		return 'Please type your password!'
	checks = [
				(len(pas)>=8,' 8 characters'),
				(re.search("\d", pas),' one number'),
				(re.search('[A-Z]',pas),' an uppercase character'),
				(re.search('[a-z]',pas),' an lowercase character'),
			]
	message = 'Your password must contain at least:'
	startlen = len(message)
	uncofirmities =''

	for check in checks :
		if not check[0] :

				uncofirmities = uncofirmities + check[1]+','

	if not uncofirmities:
		return 'PassOk'

	return message + uncofirmities[:-1] + '!'


if __name__ == '__main__' :

	pass