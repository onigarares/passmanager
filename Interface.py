from tkinter import *
from Register import *
from Login_Page import *
from Add_Password import*
from PersonalVault import *
from Edit_Password import *
import tkinter.messagebox
from tkinter import ttk


window = Tk()

window.title("Password Manager")
windows_frame = '500x400'


def Main_Menu():
	try :
		for widget in window.winfo_children():
			widget.destroy()
	except :
		pass
	window.geometry(windows_frame)
	lbl0 = Label(window,text = "Sign In")
	lbl0.pack()

	lbl = Label(window,text = "Enter your user name :")
	lbl.pack()
	txt = Entry(window,width = 20)
	txt.pack()
	txt.focus()
	res_lbl= Label(window)
	res_lbl.pack()

	lbl1 = Label(window,text = "Enter your password:")
	lbl1.pack()
	txt1 = Entry(window,width = 20,show = "*")
	txt1.pack()
	res_lbl1= Label(window)
	res_lbl1.pack()

	def login_buton():
		global MasterPassword
		username = txt.get()
		MasterPassword = txt1.get()

		log_res = Login(username,MasterPassword)
		global user_id
		user_id =log_res[2]
		if log_res[1]:
			Password_Vault()
		try:
			res_lbl.config(text =log_res[0],fg='#f00')
			res_lbl1.config(text =log_res[3],fg='#f00')
			txt1.delete(0,END)
			txt.focus()
		except:
			pass


	log_btn = Button(window, text = 'Login',pady = 5,padx = 20,command = login_buton)
	log_btn.pack()
	reg_btn = Button(window, text = 'Register',pady = 5,padx = 14,command = Register_Menu)
	reg_btn.pack()




def Register_Menu():
	try:
		for widget in window.winfo_children():
			widget.destroy()
	except:
		pass
	window.geometry(windows_frame)
	lbl0 = Label(window,text = "Register")
	lbl0.pack()

	lbl1 = Label(window,text = "Choose your user name :")
	lbl1.pack()
	txt1 = Entry(window,width = 20)  #username entry
	txt1.pack()
	txt1.focus()
	res_lbl1= Label(window)           #username response
	res_lbl1.pack()

	lbl2 = Label(window,text = "Choose your password:")   #Pass 1 entry
	lbl2.pack()
	txt2 = Entry(window,width = 20,show = "*")
	txt2.pack()
	res_lbl2= Label(window)                              #
	res_lbl2.pack()

	lbl3 = Label(window,text = "Retype your password") #Pass 2 entry
	lbl3.pack()
	txt3 = Entry(window,width = 20,show = "*")
	txt3.pack()
	res_lbl3= Label(window)
	res_lbl3.pack()

	def Create_Account():
		username = txt1.get()
		pass1 = txt2.get()
		pass2 = txt3.get()
		reg_check = register_check(username,pass1,pass2)
		if reg_check[3] == True:
			txt1.delete(0,END)
			txt2.delete(0,END)
			txt3.delete(0,END)
			res_lbl1.config(text ='',fg='#f00')
			res_lbl2.config(text ='',fg='#f00')
			res_lbl3.config(text ='',fg='#f00')
			succed_mesg = f'Hello {username} wellcome to Passwords Manager!'
			tkinter.messagebox.showinfo('Registration succed!', succed_mesg)
			Main_Menu()
		try:

			res_lbl1.config(text =reg_check[0],fg='#f00')
			res_lbl2.config(text =reg_check[1],fg='#f00')
			res_lbl3.config(text =reg_check[2],fg='#f00')
		except:
			pass
	def back_button():
		Main_Menu()

	sub_btn = Button(window, text = 'Creeate account',pady = 5,padx = 20,command = Create_Account)
	sub_btn.pack()
	bk_btn = Button(window, text = '<< back to login',pady = 5,padx = 14,command = back_button)
	bk_btn.pack()

def Password_Vault():
	#============= #TestData ==============
	# user_id ='8'
	# MasterPassword = 'Test1234'
	#======================================
	def settings_page():
		window.destroy()
		Settings_page()

	def copy_user():
		try:
		
			data_selected = data_display_tree.selection()[0]
			user = data_to_display[int(data_selected)][3]
			addToClipBoard(user)
		except IndexError:

			t = 'Select site row!'
			msg = ' Please select the row with the user you want to copy to clipboard! '
			tkinter.messagebox.askretrycancel(title =t,message = msg)

	def copy_pass():
		try:
			data_selected = data_display_tree.selection()[0]
			password = data_to_display[int(data_selected)][4]
			addToClipBoard(password)

		except IndexError:
			t = 'Select site row!'
			msg = ' Please select the row with the pasword you want to copy to clipboard! '
			tkinter.messagebox.askretrycancel(title =t,message = msg)

	def log_out():
		Main_Menu()

	def addpassword():

		Add_Password()


	def edit_Password():
		try:
			data_selected = data_display_tree.selection()[0]
			global data_to_edit
			data_to_edit = data_to_display[int(data_selected)]
			global password_id
			password_id = data_to_display[int(data_selected)][0]
			Edit_Password(data_to_edit)
		except IndexError:
			t = 'Select Password!'
			msg = ' Please select the row with the information you want to edit! '
			tkinter.messagebox.askretrycancel(title =t,message = msg)

		pass

	try:
		for widget in window.winfo_children():
			widget.destroy()
	except:
		pass

	window.geometry(windows_frame)

	my_menu = Menu(window)
	window.config(menu=my_menu)
	#Profile menu
	Profile = Menu(my_menu,tearoff=0)
	my_menu.add_cascade(label='Pofile',menu =Profile)
	Profile.add_command(label ='Edit Profile',command = log_out)
	Profile.add_command(label ='Settings',command = settings_page)


	#passwords menu
	Passwords = Menu(my_menu,tearoff=0)
	my_menu.add_cascade(label='Passwords',menu =Passwords)
	Passwords.add_command(label ='Add Password',command = Add_Password)
	Passwords.add_command(label ='Edit Password',command = edit_Password)



	#Log out menu
	Log_out = Menu(my_menu,tearoff=0)
	my_menu.add_cascade(label='Log Out',menu =Log_out)
	Log_out.add_command(label ='Log Out',command = log_out)

	#==== Define columns ===
	data_display_tree = ttk.Treeview(window)
	data_display_tree['columns'] = ('Aplication','Username','Passwords')

#==== Formate the coulmns ====
	lenght = 152
	data_display_tree.column('#0',width = 0,stretch = NO)
	data_display_tree.column('Aplication',anchor = W, width = lenght)
	data_display_tree.column('Username',anchor = CENTER, width = lenght)
	data_display_tree.column('Passwords',anchor = W, width = lenght)
#==== Create headings ====
	data_display_tree.heading('#0', text ='',anchor = W)
	data_display_tree.heading('Aplication',text = 'Aplication',anchor = W)
	data_display_tree.heading('Username',text = 'Username',anchor = CENTER)
	data_display_tree.heading('Passwords',text = 'Passwords',anchor = W)

#==== Add data to the columns ====
	#========== #TestData ===============================
	user_id ='8'
	MasterPassword = 'Test1234'
#===============================================================
	global data_to_display
	data_to_display = Select_user_data(user_id,MasterPassword)
	option = False
	#data = [('sitebun.com','celmaiusername','parola_grea')]
	
	i = 0
	for record in data_to_display :
		if option :
			show_password = record[4]
		else:
			show_password = '************'

		data_display_tree.insert(parent = '',index = 'end',iid=i,values = [record[2],record[3],show_password])
		i=+1
		data_display_tree.pack(pady= 10)

#=== Adding a frame for copy user and copy password button
	bottom = Frame(window)
	bottom.pack(pady=10)
	copyuser = Button(bottom, text = 'Username copy',pady = 10,padx = 10,command = copy_user)
	copyuser.grid(row = 1,column = 2,padx= 10,pady=50)
	copypas = Button(bottom, text = 'Password copy',pady = 10,padx = 10,command = copy_pass)
	copypas.grid(row = 1,column = 3,pady= 50)

	# Select a specific row in treeview 




# Main_Menu()

def Add_Password():
	try:
		for widget in window.winfo_children():
			widget.destroy()
	except:
		pass

	window.geometry(windows_frame)
	def generate_password():

		password = gen_password()
		try:
			txt3.delete(0,END)
		except:
			pass

		txt3.insert(0,password)

	def register_password():
		# MasterPassword = 'test22'
		# user_id = '5'
		passed = True
		site = txt1.get()
		username = txt2.get()
		added_password =txt3.get()

		if site == '' or username == '' or added_password == '':
			tkinter.messagebox.showerror(title='Insert password error!', message='No filed must be empty!')
			passed = False

		if passed == True:
			Add_Password_db(user_id,username,site,added_password,MasterPassword)
			title = ''
			msg = '    Password added successfully!\nDo you want to add another password?'
			add_another = tkinter.messagebox.askquestion(title=title, message=msg)
			if add_another == 'yes':
				txt1.focus()
				txt1.delete(0,END)
				txt2.delete(0,END)
				txt3.delete(0,END)
			else:

				Password_Vault()
		passed = True
	def back_btn():
		Password_Vault()


	lbl1 = Label(window,text = "Site/Aplication * ")
	lbl1.pack()
	txt1 = Entry(window,width = 40)
	txt1.pack()
	txt1.focus()

	lbl2 = Label(window,text = "Username *")
	lbl2.pack()
	txt2 = Entry(window,width = 40)
	txt2.pack()

	lbl3 = Label(window,text = "Password *")
	lbl3.pack()
	txt3 = Entry(window,width = 40)
	txt3.pack()

	genBtn = Button(window, text ='Generate strong password',width = 15,pady = 15,padx = 20,command = generate_password)
	genBtn.pack()
	lbl4 = Label(window,text = "")
	lbl4.pack()
	regBtn = Button(window, text ='Register Password',width = 20,pady = 15,padx = 20,command = register_password)
	regBtn.pack()
	bkBtn = Button(window, text ='Personal Vault',width = 20,pady = 15,padx = 20,command = back_btn)
	bkBtn.pack()

def Edit_Password(data_selected):
	try:
		for widget in window.winfo_children():
			widget.destroy()
	except:
			pass

	window.geometry(windows_frame)

	def back_btn():
		title ='Unsaved will be lost!'
		msg = 'Every unsaved modification will be deleted are you want to proceed?'
		ask_ok = tkinter.messagebox.askquestion(title=title, message=msg)
		if ask_ok == 'yes':
			Password_Vault()

	def generate_password():
		password = gen_password()
		try:
			txt3.delete(0,END)
		except:
			pass

		txt3.insert(0,password)

	def save_update():
		edited_site = txt1.get()
		edited_username = txt2.get()
		edited_password =txt3.get()

		if edited_site != ''and edited_username!='' and edited_password!= '':
		#================== #TestData  =================
		# password_id ='3'
		# MassterPassword = 'Test1234'

		#==============================================
			edit_data(password_id,edited_site,edited_username,edited_password,MasterPassword)
			title = 'Password data modified!'
			msg = f'Your data for the site  {edited_site} and username {edited_username} have been successfully modified! Take care!'
			tkinter.messagebox.showinfo(title=title, message=msg)
			Password_Vault()

		else:
			tkinter.messagebox.showerror(title='Insert password error!', message='No filed must be empty!')

		pass

	def del_password():
		
		title = 'Password Delete!'
		msg = 'Password will be deleted ! This action is ireversible!\nAre you sure you want to continue?'
		del_pass = tkinter.messagebox.askquestion(title=title, message=msg)
		if del_pass == 'yes':
			delete_password(password_id)
			Password_Vault()

		pass
	lbl1 = Label(window,text = "Site/Aplication * ")
	lbl1.pack()
	txt1 = Entry(window,width = 40)
	txt1.pack()
	txt1.focus()

	lbl2 = Label(window,text = "Username *")
	lbl2.pack()
	txt2 = Entry(window,width = 40)
	txt2.pack()

	lbl3 = Label(window,text = "Password *")
	lbl3.pack()
	txt3 = Entry(window,width = 40)
	txt3.pack()

	genBtn = Button(window, text ='Generate strong password',width = 15,pady = 15,padx = 20,command = generate_password)
	genBtn.pack()
	lbl4 = Label(window,text = "")
	lbl4.pack()
	regBtn = Button(window, text ='Save Update',width = 20,pady = 15,padx = 20,command = save_update)
	regBtn.pack()
	deltn = Button(window, text ='Delete Password',width = 20,pady = 15,padx = 20,command = del_password)
	deltn.pack()
	bkBtn = Button(window, text ='Personal Vault',width = 20,pady = 15,padx = 20,command = back_btn)
	bkBtn.pack()

	txt1.insert(0,data_to_edit[2])
	txt2.insert(0,data_selected[3])
	txt3.insert(0,data_selected[4])

if __name__ == '__main__':
	Main_Menu()


window.mainloop()
