from tkinter import*
from tkinter import ttk
from graph import Student
import sqlite3
from PIL import Image,ImageTk
from tkcalendar import  Calendar,DateEntry
from tkinter import ttk,messagebox
import time
import subprocess
class Studinfo:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1750x900+0+0")
        self.root.title("PLACEMENT MANAGEMENT SYSTEM | MCA STUDENTS")
        self.root.config(bg="white")
        self.my_canvas=Canvas(self.root,width=1750,height=900,bd=1)

        title=Label(self.root,text="Placement Management  System",compound=LEFT,font=("times new roman",40,"bold"),bg="#47476b",fg="orange").place(x=0,y=0,relwidth=1,height=70)
#############  time
        self.b_title=Label(self.root,text="Welcome   \t\tDate=DD:MM:YYYY\t\tTime=II:MM:SS:P",font=("times new roman",10,"bold"),bg="#8a8a5c",fg="black")
        self.b_title.place(x=0,y=70,relwidth=1,height=30)
        self.update_time()

        self.phone_im=Label(self.root,bd=3,text="hey")#image=self.Lo)
        self.phone_im.place(x=0,y=110,width=1840,height=870)

        self.Logo1=Image.open("images/e11.jpg")
        self.Logo1=self.Logo1.resize((1840,870),Image.ANTIALIAS)
        self.Logo1=ImageTk.PhotoImage(self.Logo1)
        
        self.Logo2=Image.open("images/e12.jpg")
        self.Logo2=self.Logo2.resize((1840,870),Image.ANTIALIAS)
        self.Logo2=ImageTk.PhotoImage(self.Logo2)

        self.Logo3=Image.open("images/n03.jpg")
        self.Logo3=self.Logo3.resize((1840,870),Image.ANTIALIAS)
        self.Logo3=ImageTk.PhotoImage(self.Logo3)
        
        self.Logo4=Image.open("images/n04.jpg")
        self.Logo4=self.Logo4.resize((1840,870),Image.ANTIALIAS)
        self.Logo4=ImageTk.PhotoImage(self.Logo4)

        self.ani()

        
        


        btn_emp=Button(title,text="GRAPH",command=self.graph,compound=LEFT,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",anchor="w").place(x=1400,y=3,width=200,height=40)
        btn_emp1=Button(title,text="LOGOUT",command=self.logout,compound=LEFT,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",anchor="w").place(x=1640,y=3,width=200,height=40)



    def ani(self):
        self.im=self.Logo1
        self.Logo1=self.Logo2
        self.Logo2=self.Logo3
        self.Logo3=self.Logo4
        self.Logo4=self.im
        self.phone_im.config(image=self.im)
        self.phone_im.after(1200,self.ani)
        

    def graph(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=Student(self.new_win)


    def  update_time(self):        
        tim=time.strftime("%I:%M:%S%p")
        dat=time.strftime("%d:%m:%Y")
        self.b_title.config(text=f"Welcome \t\tDate: {str(dat)}\t\t Time: {str(tim)}")
        self.b_title.after(200,self.update_time)

    def logout(self):
        self.root.destroy()
        subprocess.run(['python3','check.py'])

if  __name__=="__main__":
     root=Tk()
     obj=Studinfo(root)
     root.mainloop()
