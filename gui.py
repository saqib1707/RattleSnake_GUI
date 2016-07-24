from Tkinter import *
import StudentLogin
import TeacherInterface
import administrator

class gui:
	def __init__(self):
		global frame
		frame=Tk()
		frame.title('Authentication')
		frame.config(bg='#ABADAC')
		frame.geometry('600x400+350+150')
		frame.resizable(width=False,height=False)
		studentbtn=Button(frame,text="Student Interface",command=lambda:StudentLogin.studentInterface(frame),activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='5px',pady='5px')
		teacherbtn=Button(frame,text="Teacher Interface",command=TeacherInterface.teacherInterface,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='5px',pady='5px')
		adminbtn=Button(frame,text="Admin Interface",command=administrator.adminInterface,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='5px',pady='5px')
		studentbtn.place(x=90,y=80)
		teacherbtn.place(x=240,y=80)
		adminbtn.place(x=390,y=80)
		frame.mainloop()

mainobj=gui()
