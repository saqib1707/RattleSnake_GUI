import json,os
import tkMessageBox
from Tkinter import *	
		
class Login:
	def __init__(self):		
		print ""

	def checkBatchEmpty(self,batch):
		with open('StudentRecords.txt') as readStudentFile:
			jsonData=json.load(readStudentFile)
			for i in range(len(jsonData)):
				if jsonData[i]['batch']==batch:
					return False
			tkMessageBox.showinfo('Error 404','Batch is empty')
			return True

	def getMarks(self):
		with open('StudentRecords.txt') as readStudentFile:
			jsonData=json.load(readStudentFile)
			for i  in range(len(jsonData)):
				if jsonData[i]['name']==self.name_entry.get() and self.marks_entry.get()!="" and jsonData[i]['batch']==self.batch:
					jsonData[i]['marks']=self.marks_entry.get()
					msg="Marks Modified for %s"%self.name_entry.get()
					tkMessageBox.showinfo('Cngos',msg)
					self.is_Modified=True
					break
			if self.is_Modified==False:
				tkMessageBox.showinfo('Error 404','Modification Failure!!!Student not found')
				self.name_entry.delete(0,'end')
				self.marks_entry.delete(0,'end')
				return
			open('StudentRecords.txt','w').write(json.dumps(jsonData,indent=4))
			count=0
			for widget in main.frame.winfo_children():
				count+=1
				if count>=11:
					widget.destroy()
	def modifyMarks(self):
		self.is_Modified=False
		if self.checkBatchEmpty(self.batch)==True:
			return
		self.label1=Label(main.frame,text='Student Name whose marks has to be modified:',bg='#58F0AB',padx='5px',pady='3px').place(x=40,y=310)
		self.name_entry=Entry(main.frame,width=15)
		self.name_entry.place(x=40,y=340)
		self.label2=Label(main.frame,text='Modified Marks:',bg='#58F0AB',padx='5px',pady='3px').place(x=350,y=310)
		self.marks_entry=Entry(main.frame)
		self.marks_entry.place(x=350,y=340)
		self.modify_btn=Button(main.frame,text='Modify>>',command=self.getMarks,bg='#58F0AB',padx='5px',pady='1px')
		self.modify_btn.place(x=480,y=340)

	def showListOfStudents(self):
		if self.checkBatchEmpty(self.batch)==True:
			return
		listOfStudent=[]
		with open('StudentRecords.txt') as readStudentFile:
			jsonData=json.load(readStudentFile)
			for i in range(len(jsonData)):
				if jsonData[i]['batch']==self.batch:
					data={jsonData[i]['name']:jsonData[i]['marks']}
					listOfStudent.append(data)
			with open('/home/saqib1707/Desktop/RattleSnake_GUI/temp.txt','w') as tempFile:
				json.dump(listOfStudent,tempFile,indent=4)
			os.system('xdg-open /home/saqib1707/Desktop/RattleSnake_GUI/temp.txt')

	def uploadMarks(self):
		if self.checkBatchEmpty(self.batch)==True:
			return
		with open('StudentRecords.txt') as readStudentFile:
			jsonData=json.load(readStudentFile)
			for i in range(len(jsonData2)):
				if jsonData[i]['batch']==self.batch:
					arg='Enter marks for '+jsonData[i]['name']+':'
					Label(frame,text=arg,bg='#58F0AB',padx='10px',pady='3px').place(x=80,y=50)
					marks_entry=Entry(frame)
					marks_entry.place()
					next_btn=Button(frame,text='Next')
					next_btn.pack()
			open('StudentRecords.txt','w').write(json.dumps(jsonData2,indent=4))
			tkMessageBox.showinfo('Congos','Marks updated successfully')
		with open('TeacherRecords.txt') as readTeacherFile:
			jsonData1=json.load(readTeacherFile)
			for i in range(len(jsonData1)):
				if jsonData1[i]['batch']==self.batch:
					jsonData1[i]['is_Marks_Updated']="True"
			open('TeacherRecords.txt','w').write(json.dumps(jsonData1,indent=4))

	def login(self):
		username=main.username_entry.get()
		pwd=main.password_entry.get()
		self.batch=None
		with open('TeacherRecords.txt') as readTeacherFile:
			jsonData1=json.load(readTeacherFile)
			for i in range(len(jsonData1)):
				if jsonData1[i]['username']==username and jsonData1[i]['password']==pwd :
					self.batch=jsonData1[i]['batch']
					msg=str(jsonData1[i]['name'])+' -Batch  '+str(self.batch)+'\nAccess Granted'
					msg_widget=Message(main.frame,text=msg,width=500,bg='#9FE4F3',padx='10px',pady='5px')
					msg_widget.place(x=220,y=190)
					if jsonData1[i]['is_Marks_Updated']=="False":
						tkMessageBox.showinfo('Warning','Reminder to upload the latest test marks')
					Button(main.frame,text='List students in ur Batch',command=self.showListOfStudents,activebackground='grey',activeforeground='#AB78F1',cursor='arrow',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px').place(x=40,y=260)
					Button(main.frame,text='Upload marks of latest test',command=self.uploadMarks,activebackground='grey',activeforeground='#AB78F1',cursor='arrow',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px').place(x=215,y=260)
					Button(main.frame,text='Modify marks of student',command=self.modifyMarks,activebackground='grey',activeforeground='#AB78F1',cursor='arrow',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px').place(x=400,y=260)
					break
			if self.batch==None:
				tkMessageBox.showinfo('Access Denied','Username or Password or both are incorrect!!! Try Again')
				main.username_entry.delete(0,'end')
				main.password_entry.delete(0,'end')

class TeacherInterface:			
	def __init__(self):
		self.frame=Tk()
		self.frame.title('Teacher Portal')
		self.frame.geometry('600x400+350+150')
		self.frame.config(bg='#ABADAC')
		self.frame.resizable(width=False,height=False)

	def exit(self):
		self.frame.destroy()

	def back(self):
		login_obj=Login()
		username_label=Label(self.frame,text="User Name",bg='#58F0AB',padx='10px',pady='3px').place(x=80,y=50)
		self.username_entry=Entry(self.frame,width=20)
		self.username_entry.place(x=170,y=50)
		password_label=Label(self.frame,text="Password",bg='#58F0AB',padx='10px',pady='3px').place(x=310,y=50)
		self.password_entry=Entry(self.frame,show="*",width=20)
		self.password_entry.place(x=390,y=50)
		Button(self.frame,text="Login",command=login_obj.login,activebackground='grey',activeforeground='#AB78F1',cursor='arrow',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px').place(x=250,y=100)
		Button(self.frame,text='Exit',command=self.exit,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px').place(relx=0.45,rely=0.35)
        
main=TeacherInterface()
main.back()
main.frame.mainloop()