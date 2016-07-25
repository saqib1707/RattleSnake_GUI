import json
import os
from Tkinter import *
import tkMessageBox

def checkFileEmpty():
    if os.stat("StudentRecords.txt").st_size == 0:
        tkMessageBox.showinfo('Error 404','Empty File!!!Please add members to perform these operations')
        return True
    else:
        return False

class AddStudent:
    def __init__(self):
        self.nametoadd=""
        self.phone_no=""
        self.marks=0
        self.batch=None
        self.username=""
        self.password=""

    def addStudent_getData(self):
        listobj=[]
        count=0
        string=""
        myModifiedList=""
        self.nametoadd=self.name_entry.get()
        self.phone_no=self.phone_entry.get()
        with open("StudentRecords.txt") as readStudentFile:
            if checkFileEmpty()==False:
                jsonData=json.load(readStudentFile)
                if len(jsonData) in range(1,4):
                    self.batch=1
                elif len(jsonData) in range(4,8):
                    self.batch=2
                elif len(jsonData) in range(8,12):
                    self.batch=3
                elif len(jsonData) in range(11,15):
                    self.batch=4
            else:
                self.batch=1

        data= {"name":self.nametoadd,"phoneno":self.phone_no,"marks":self.marks,"batch":self.batch,"username":self.username,"password":self.password}
        listobj.append(data)
        
        with open('StudentRecords.txt','a') as appendStudentFile:
            json.dump(listobj,appendStudentFile)
        with open('StudentRecords.txt') as readStudentFile:
            textdata=readStudentFile.read()
            for char in textdata:
                if count==1:
                    string+=char
                    if string=="][":
                        count=2
                        char=','
                if char==']':
                    count+=1
                    string+=char
                else:
                    myModifiedList+=char
                if count==2:
                    continue
            if count==1 or count==3:
                myModifiedList+=']'
        with open('StudentRecords.txt','w') as file:
            file.write(myModifiedList)
        jsonData=json.load(open("StudentRecords.txt"))
        open("StudentRecords.txt",'w').write(json.dumps(jsonData,indent=4))
        tkMessageBox.showinfo('Attention','Student Added to Database')
        count=0
        for widget in main.frame.winfo_children():
            count+=1
            if count>=6:
                widget.destroy()

    def addStudent(self):
        Label(main.frame,text='Enter Name:',bg='#58F0AB',padx='5px',pady='3px').place(relx=0.2,rely=0.4)
        self.name_entry=Entry(main.frame)
        self.name_entry.place(relx=0.4,rely=0.4)
        Label(main.frame,text='Enter Phone No:',bg='#58F0AB',padx='5px',pady='3px').place(relx=0.2,rely=0.5)
        self.phone_entry=Entry(main.frame)
        self.phone_entry.place(relx=0.4,rely=0.5)
        continue_btn=Button(main.frame,text='Continue',command=self.addStudent_getData,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px')
        continue_btn.place(relx=0.4,rely=0.6)

class RemoveStudent:
    def __init__(self):
        print " "

    def removeStudent_getData(self):
        with open('StudentRecords.txt') as readStudentFile:
            jsonData1=json.load(readStudentFile)
            found=False
            if jsonData1==[]:
                tkMessageBox.showinfo('Warning','Student Database already empty!!!No more members to delete')
            self.nameToRemove=self.name_entry.get()
            for i in range(len(jsonData1)):
                if jsonData1[i]["name"]==self.nameToRemove :
                    jsonData1.pop(i)
                    msg='%s deleted from database' %self.nameToRemove
                    found=True
                    break
            if found==False:
                msg='%s not in the database'%self.nameToRemove
            tkMessageBox.showinfo('Warning',msg)
            open('StudentRecords.txt','w').write(json.dumps(jsonData1,indent=4))
            count=0
            for widget in main.frame.winfo_children():
                count+=1
                if count>=6:
                    widget.destroy()
            
    def removeStudent(self):
        if checkFileEmpty()==True:
            return
        Label(main.frame,text='Enter Name to be removed:',bg='#58F0AB',padx='5px',pady='3px').place(relx=0.2,rely=0.4)
        self.name_entry=Entry(main.frame)
        self.name_entry.place(relx=0.5,rely=0.4)
        continue_btn=Button(main.frame,text='Remove',command=self.removeStudent_getData,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px')
        continue_btn.place(relx=0.4,rely=0.5)

class ShowListAndModify:       
    def showListOfStudents(self):
        listObj=[]
        with open('StudentRecords.txt') as infile:
            if checkFileEmpty()==False:
                data=json.load(infile)
                for i in range(len(data)):
                    dictionary={"name":data[i]['name'],"phoneno":data[i]['phoneno'],"marks":data[i]['marks'],"batch":data[i]['batch']}
                    listObj.append(dictionary)
                with open('/home/saqib1707/Desktop/Extra_RattleSnake_copy/Info.txt','w') as readFile:
                    json.dump(listObj,readFile,indent=4)
                os.system('xdg-open /home/saqib1707/Desktop/Extra_RattleSnake_copy/Info.txt')     
        infile.close()
    def finalModify(self):
        self.jsonData[flag]['name']=self.name_entry1.get()
        self.jsonData[flag]['phoneno']=self.name_phone.get()
        msg="Data Modified for %s"%self.name_entry1.get()
        tkMessageBox.showinfo('Attention',msg)
        open("StudentRecords.txt",'w').write(json.dumps(self.jsonData,indent=4))
        count=0
        for widgets in main.frame.winfo_children():
        	count+=1
        	if count>=6:
        		widgets.destroy()

    def getName(self):
        modification=True
        for i in range(len(self.jsonData)):
            if self.jsonData[i]["name"]==self.name_entry.get() :
                global flag
                flag=i
                Label(main.frame,text='Modified Name:',bg='#58F0AB',padx='5px',pady='3px').place(relx=0.2,rely=0.6)
                self.name_entry1=Entry(main.frame)
                self.name_entry1.place(relx=0.3,rely=0.6)
                Label(main.frame,text='Modified Phone no',bg='#58F0AB',padx='5px',pady='3px').place(relx=0.6,rely=0.6)
                self.name_phone=Entry(main.frame)
                self.name_phone.place(relx=0.8,rely=0.6)
                continue_btn=Button(main.frame,text='Modify',command=self.finalModify,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px')
                continue_btn.place(relx=0.4,rely=0.8)
                    
    def modifyData(self):
        with open('StudentRecords.txt') as infile:
            if checkFileEmpty()==False:
                self.jsonData=json.load(infile)
                Label(main.frame,text='Student whose data has to be modified',bg='#58F0AB',padx='5px',pady='3px').place(relx=0.1,rely=0.4)
                self.name_entry=Entry(main.frame)
                self.name_entry.place(relx=0.5,rely=0.4)
                next_btn=Button(main.frame,text='Next>>',command=self.getName,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px')
                next_btn.place(relx=0.4,rely=0.5)

class Administrator:
	def __init__(self):
		print " "

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
		#------------------showing the shuffled data----------------------------#
		for i in range(len(jsonDataSorted)):
			datadict={'name':jsonDataSorted[i]['name'],'marks':jsonDataSorted[i]['marks'],"batch":jsonDataSorted[i]['batch']}
			listObj.append(datadict)
		json.dump(listObj,open('/home/saqib1707/Desktop/RattleSnake_GUI/MarkSheet.txt','w'))
		jsonDataSorted=json.load(open('MarkSheet.txt'))
		open('MarkSheet.txt','w').write(json.dumps(jsonDataSorted,indent=4))
		os.system('xdg-open /home/saqib1707/Desktop/RattleSnake_GUI/MarkSheet.txt')

class CoachingTemp:
    def __init__(self):
    	print ""

    def back(self):
    	for widget in main.frame.winfo_children():
    		widget.destroy()
        addStudent_obj=AddStudent()
        remStudent_obj=RemoveStudent()
        show_obj=ShowListAndModify()
        addStudent_btn=Button(main.frame,text='Add Student',command=addStudent_obj.addStudent,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px')
        addStudent_btn.place(relx=0.07,rely=0.2)
        removeStudent_btn=Button(main.frame,text='Remove Student',command=remStudent_obj.removeStudent,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px')
        removeStudent_btn.place(relx=0.25,rely=0.2)
        showAllStudent_btn=Button(main.frame,text='Show All Students',command=show_obj.showListOfStudents,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px')
        showAllStudent_btn.place(relx=0.45,rely=0.2)
        modify_btn=Button(main.frame,text='Modify Info of Students',command=show_obj.modifyData,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px')
        modify_btn.place(relx=0.65,rely=0.2)
        back_btn=Button(main.frame,text='Back',command=main.back,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px')
        back_btn.place(relx=0.45,rely=0.35)

class AdminInterface:
	def __init__(self):
		self.frame=Tk()
		self.frame.title('Administrator Portal')
		self.frame.geometry('600x400+350+150')
		self.frame.config(bg='#ABADAC')
		self.frame.resizable(width=False,height=False)
	
	def exit(self):
		main.frame.destroy()

	def back(self):
		for widget in main.frame.winfo_children():
			widget.destroy()
		admin_obj=Administrator()
		coachingtemp_obj=CoachingTemp()
		accessDatabase_btn=Button(self.frame,text='Access Students Database',command=coachingtemp_obj.back,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px')
		accessDatabase_btn.place(relx=0.1,rely=0.2)
		startTest_btn=Button(self.frame,text='Start a New Test',command=admin_obj.startNewTest,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px')
		startTest_btn.place(relx=0.4,rely=0.2)
		batchAllotment_btn=Button(self.frame,text='Batch Allotment',command=admin_obj.reMapping,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px')
		batchAllotment_btn.place(relx=0.65,rely=0.2)
		Button(main.frame,text='Exit',command=self.exit,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px').place(relx=0.45,rely=0.35)


main=AdminInterface()
main.back()
main.frame.mainloop()