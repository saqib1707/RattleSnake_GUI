import json
import coachingtemp
import os
from Tkinter import *
import tkMessageBox

class Administrator:
	def __init__(self):
		print

	def startNewTest(self):
		flag=True
		with open('TeacherRecords.txt','r') as readTeacherFile:
			jsonData=json.load(readTeacherFile)
			for i in range(len(jsonData)):
				if jsonData[i]['is_Marks_Updated']=="None":
					flag=False
					jsonData[i]['is_Marks_Updated']="False"
			if flag==False:
				tkMessageBox.showinfo('Error 404','New Test could not be started now.Reminders to teachers who have not submitted marksheet')
				return
		tkMessageBox.showinfo('Attention','New Test Started')
		with open('TeacherRecords.txt') as readTeacherFile:
			jsonData=json.load(readTeacherFile)
			for i in range(len(jsonData)):
					jsonData[i]['is_Marks_Updated']="None"
			open('TeacherRecords.txt','w').write(json.dumps(jsonData,indent=4))

	def reMapping(self):
		count=0
		listObj=[]
		with open('TeacherRecords.txt','r') as readTeacherFile:
			jsonData=json.load(readTeacherFile)
			for i in range(len(jsonData)):
				if jsonData[i]['is_Marks_Updated']!="True":
					tkMessageBox.showinfo('Error 404','All students marks has not be uploaded!! ReMapping could not be done now')
					return
		tkMessageBox.showinfo('Attention','Remapping of Students')
		i=1
		with open('StudentRecords.txt','r') as readStudentFile:
			jsonData=json.load(readStudentFile)
			jsonDataSorted=sorted(jsonData,key=lambda k:k['marks'],reverse=True)
			for j in range(len(jsonDataSorted)):
				count+=1
				if count%5==0:
					i+=1
					count+=1
				jsonDataSorted[j]['batch']=i
		open('StudentRecords.txt','w').write(json.dumps(jsonDataSorted,indent=4))
		#showing the shuffled data
		for i in range(len(jsonDataSorted)):
			datadict={'name':jsonDataSorted[i]['name'],'marks':jsonDataSorted[i]['marks'],"batch":jsonDataSorted[i]['batch']}
			listObj.append(datadict)
		json.dump(listObj,open('MarkSheet.txt','w'))
		jsonDataSorted=json.load(open('MarkSheet.txt'))
		open('MarkSheet.txt','w').write(json.dumps(jsonDataSorted,indent=4))
		os.system('MarkSheet.txt')


class AdminInterface:
	def __init__(self):
		self.frame=Tk()
		self.frame.title('Administrator Portal')
		self.frame.geometry('600x400+350+150')
		self.frame.config(bg='#ABADAC')
		self.frame.resizable(width=False,height=False)
	def back(self):
		admin_obj=Administrator()
		accessDatabase_btn=Button(self.frame,text='Access Students Database',command=coachingtemp.myfunc,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px')
		accessDatabase_btn.place(relx=0.1,rely=0.2)
		startTest_btn=Button(self.frame,text='Start a New Test',command=admin_obj.startNewTest,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px')
		startTest_btn.place(relx=0.4,rely=0.2)
		batchAllotment_btn=Button(self.frame,text='Batch Allotment',command=admin_obj.reMapping,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px')
		batchAllotment_btn.place(relx=0.65,rely=0.2)
main=AdminInterface()
main.back()
main.frame.mainloop()
