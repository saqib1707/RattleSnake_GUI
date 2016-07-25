import json
import os
from Tkinter import *
import tkMessageBox

#-----------check for empty database-------------------------
def checkFileEmpty():
        if os.stat("/home/saqib1707/Desktop/RattleSnake_GUI/StudentRecords.txt").st_size  ==  0:
            tkMessageBox.showinfo('Warning','Empty File!!!Please add members to perform these operations')
            return True
        else:
            return False
def destroyInterface(obj):
	for widget in obj.winfo_children():
		widget.destroy()

class Login:
	def __init__(self):
		print 

	def login(self):
		found = False
		#----------checks whether the file is empty or not--------------
		if checkFileEmpty() == True:              
			return
		destroyInterface(main.frame)
		main.frame.title('Student Portal --Login Interface')
		usernamelabel  =  Label(main.frame,text = "User Name",bg = '#58F0AB',padx = '10px',pady = '3px').place(x = 50,y = 60)
		self.usernameentry1 = Entry(main.frame,width = 25)
		self.usernameentry1.place(x = 145,y = 60)
		passwordlabel = Label(main.frame,text = "Password",bg = '#58F0AB',padx = '10px',pady = '3px').place(x = 330,y = 60)
		self.passwordentry1 = Entry(main.frame,show = "*",width = 25)
		self.passwordentry1.place(x = 415,y = 60)
		Button(main.frame,text = "Login",command = self.getLogin,activebackground = 'grey',activeforeground = '#AB78F1',cursor = 'arrow',bg = '#58F0AB',highlightcolor = 'red',padx = '10px',pady = '3px').place(x = 250,y = 120)
		Button(main.frame,text= "Back",command=main.back,activebackground = 'grey',activeforeground = '#AB78F1',cursor = 'arrow',bg = '#58F0AB',highlightcolor = 'red',padx = '10px',pady = '3px').place(x = 250,y = 160)
	
	def getLogin(self):
		found = False
		username = self.usernameentry1.get()
		pwd = self.passwordentry1.get()
		with open('StudentRecords.txt') as readFile:
			jsonData = json.load(readFile)
	        for i in range(len(jsonData)):
	        	if jsonData[i]['username'] == username and jsonData[i]['password'] == pwd:
	        		#-----------------show his username,marks,rank and current batch-----------------------#
	        		found = True
	        		msg = 'Name:'+str(jsonData[i]['name'])+'\nMarks:'+str(jsonData[i]['marks'])+'\nCurrent Batch:'+str(jsonData[i]['batch'])
	        		msg_widget = Message(main.frame,text = msg,width = 500,bg = '#9FE4F3',padx = '10px',pady = '5px')
	        		msg_widget.place(x = 220,y = 200)
	        if found == False:
	        	tkMessageBox.showinfo('Warning','Not registered or Wrong Username or Password!!!If Registered ,then Sign Up!!!')
	        	self.usernameentry1.delete(0,'end')
	        	self.passwordentry1.delete(0,'end')

#--------------for students who have been admitted -----------------#
class SignUp:
	def __init__(self):
		print
	def getSignUp(self):
		username = self.username_entry.get()
		pwd = self.password_entry.get()
		with open('StudentRecords.txt') as readFile:
			jsonData = json.load(readFile)
		jsonData[self.flag]['username'] = username
		jsonData[self.flag]['password'] = pwd
		tkMessageBox.showinfo('Congratulations','Registration complete!!! Now Login to view your Current Status')
		open('StudentRecords.txt','w').write(json.dumps(jsonData,indent = 4))
		main.back()	

	def getConfirmation(self):
		countOfTry = 0
		found = False
		name = self.name_entry.get()
		phone = self.phone_entry.get()
		with open('StudentRecords.txt') as readStudentFile:
			jsonData = json.load(readStudentFile)
			for i in range(len(jsonData)):
				if jsonData[i]['name'] == name and jsonData[i]['phoneno'] == phone and jsonData[i]['username'] == "" and jsonData[i]['password'] == "":
					found = True
					usernamelabel = Label(main.frame,text = "User Name",bg = '#58F0AB',padx = '10px',pady = '3px').place(x = 80,y = 210)
					self.username_entry = Entry(main.frame)
					self.username_entry.place(x = 175,y = 210)
					passwordlabel = Label(main.frame,text = "Password",bg = '#58F0AB',padx = '10px',pady = '3px').place(x = 330,y = 210)
					self.password_entry = Entry(main.frame,show = "*")
					self.password_entry.place(x = 415,y = 210)
					Button(main.frame,text = "SignUp",command = self.getSignUp,activebackground = 'grey',activeforeground = '#AB78F1',cursor = 'arrow',bg = '#58F0AB',highlightcolor = 'red',padx = '10px',pady = '3px').place(x = 260,y = 280)
					self.flag = i
					break
			if found == False:
				tkMessageBox.showinfo('Error 404','Not admitted yet or data filled incorrectly or already registered')
				self.name_entry.delete(0,'end')
				self.phone_entry.delete(0,'end')

	def signUp(self):
		if checkFileEmpty() == True:              
			return
		destroyInterface(main.frame)
		main.frame.title('Student Portal -Sign Up')
		Label(main.frame,text = "Name",bg = '#58F0AB',padx = '10px',pady = '3px').place(x = 90,y = 80)
		self.name_entry = Entry(main.frame)
		self.name_entry.place(x = 160,y = 80)
		Label(main.frame,text = "Phone No",bg = '#58F0AB',padx = '10px',pady = '3px').place(x = 330,y = 80)
		self.phone_entry = Entry(main.frame)
		self.phone_entry.place(x = 420,y = 80)
		submit = Button(main.frame,text = 'Confirmation',command = self.getConfirmation,bg = '#58F0AB',padx = '10px',pady = '3px').place(x = 240,y = 140)
		Button(main.frame,text = 'Back',command = main.back,bg = '#58F0AB',padx = '10px',pady = '3px').place(x = 240,y = 190)

class stuInterface():
	def __init__(self):
		self.frame = Tk()
		self.frame.title('Student Portal')
		self.frame.geometry('600x400+350+150')
		self.frame.config(bg = '#ABADAC')
		self.frame.resizable(width = False,height = False)
		global Login_obj,SignUp_obj
		Login_obj=Login()
		SignUp_obj=SignUp()

	def exit(self):
		self.frame.destroy()

	def back(self):
		destroyInterface(self.frame)
		login_btn = Button(self.frame,text = "Login",command = Login_obj.login,activebackground = 'grey',activeforeground = '#AB78F1',bg = '#58F0AB',highlightcolor = 'red',padx = '10px',pady = '3px')
		signup_btn = Button(self.frame,text = "Sign Up",command = SignUp_obj.signUp,activebackground = 'grey',activeforeground = '#AB78F1',bg = '#58F0AB',highlightcolor = 'red',padx = '10px',pady = '3px')
		exit_btn = Button(self.frame,text = "Exit",command=self.exit,activebackground = 'grey',activeforeground = '#AB78F1',bg = '#58F0AB',highlightcolor = 'red',padx = '10px',pady = '3px')
		login_btn.place(x = 200,y = 100)
		signup_btn.place(x = 350,y = 100)
		exit_btn.place(x=260,y=160)

main = stuInterface()
main.back()
main.frame.mainloop()
