from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import sqlite3
from tkinter import messagebox 
from student import Student
import os
import subprocess
class Login:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1750x900+0+0")
        self.root.title("Login System")
        self.my_canvas=Canvas(self.root,width=1750,height=900,bd=1)
        self.Lo=Image.open("images/n01.jpg")
        self.Lo=self.Lo.resize((1850,1060),Image.ANTIALIAS)
        self.Lo=ImageTk.PhotoImage(self.Lo)
        self.my_canvas.create_image(0,0,image=self.Lo,anchor="nw")
        
        self.my_canvas.pack(fill="both",expand=True)
        self.my_canvas.create_text(850,80,text="PLACEMENT MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),fill="brown")

        self.L=Image.open("images/n01.jpg")
        self.L=self.L.resize((625,400),Image.ANTIALIAS)
        self.L=ImageTk.PhotoImage(self.L)


        self.e11=Label(image=self.L,bd=0)
        self.e11.pack(fill=X,expand=1)
        wind=self.my_canvas.create_window(870,530,window=self.e11)

    ######## variables +++++++
        self.stud_id=StringVar()
        self.password=StringVar()

           #####IMAGE##############
        

        #self.Logo1=ImageTk.PhotoImage(file="images/n02.jpg")
        self.Log1=Image.open("images/n02.jpg")
        self.Log1=self.Log1.resize((625,400),Image.ANTIALIAS)
        self.Log1=ImageTk.PhotoImage(self.Log1)
        
        #self.Logo2=ImageTk.PhotoImage(file="images/n2.jpg")
        self.Log2=Image.open("images/n01.jpg")
        self.Log2=self.Log2.resize((625,400),Image.ANTIALIAS)
        self.Log2=ImageTk.PhotoImage(self.Log2)
        
        #self.Logo3=ImageTk.PhotoImage(file="images/n03.jpg")
        self.Log3=Image.open("images/n03.jpg")
        self.Log3=self.Log3.resize((625,400),Image.ANTIALIAS)
        self.Log3=ImageTk.PhotoImage(self.Log3)


        self.g3=Image.open("images/u1.png")
        self.g3=self.g3.resize((35,40),Image.ANTIALIAS)
        self.g3=ImageTk.PhotoImage(self.g3)

        self.g13=Image.open("images/pa1.png")
        self.g13=self.g13.resize((50,40),Image.ANTIALIAS)
        self.g13=ImageTk.PhotoImage(self.g13)

        
        
        self.g1=Image.open("images/pa2.png")
        self.g1=self.g1.resize((50,40),Image.ANTIALIAS)
        self.g1=ImageTk.PhotoImage(self.g1)
        

    ######## LOGIN ++++++++++++
        self.use_l = Label(self.root,text="LOGIN",bd=6,font=("arial",20,"bold"), fg="BLACK")
        self.use_l.place(x=830, y=280, height=31, width=154)


         ########### ++++++ LABEL ++++++++++++++++
        user_stud=Label(self.root,text="User_id",image=self.g3,compound=RIGHT,font=("times new roman" ,15, "bold"),bg="white",bd=3)
        user_stud.place(x=580,y=350,height=40,width=130)

        doj_stud=Label(self.root,text="Password",font=("times new roman" ,15, "bold"),bg="white",bd=3)
        doj_stud.place(x=580,y=440,height=40,width=110)
        


          ####### + ENTRY +++++++++
        self.user_stud=Entry(self.root,textvariable=self.stud_id,font=("times new roman" ,15),bg="white",bd=2)
        self.user_stud.place(x=750,y=350,height=40,width=210)

        self.pwd=Entry(self.root,textvariable=self.password,show='*',font=("times new roman",15),bg="white",bd=2)
        self.pwd.place(x=790,y=440,height=40,width=200)


        self.b1=Button(self.root,cursor="hand2",image=self.g13,command=self.p,font=("arial 18 bold",19,"bold"),bd=3)
        self.b1.place(x=700,y=440, height=40, width=70)
        self.btn=True

        self.BtnLogin = Button(self.root,text="Admin Login",command=self.login1,font=("times new roman",20,"italic"),bg="white",bd=5,cursor="hand2",anchor="w")
        self.BtnLogin.place(x=750,y=600, height=34, width=240)
       


        self.ani()

    def ani(self):
        self.im=self.Log1
        self.Log1=self.Log2
        self.Log2=self.Log3
        self.Log3=self.im
        self.e11.config(image=self.im)
        self.e11.after(1200,self.ani)
        
    def p(self):
        if self.btn:
            self.b1.config(image=self.g1)
            self.p1=self.pwd.get()
            self.pwd.config(show=self.p1)
            self.btn=False
        else:
            self.pwd.config(show='*')
            self.b1.config(image=self.g13)
            self.btn=True
    def login1(self): 
        con=sqlite3.connect(database=r'student.db')
        cur=con.cursor()
        try:
            
            if self.user_stud.get() == "" and  self.pwd_stud.get()== "":
                messagebox.showerror("Error", "All fields are required",parent=self.root)
            else:
                
                    cur.execute("select name from admin where user_id=? and password=?",(self.user_stud.get(),self.pwd.get()))
                    user=cur.fetchone()
                    if  user==('admin',):
                        try:
                            subprocess.run(['python3','student1.py']) 
                        finally:
                           self.root.destroy() 
                    else:
                    
                        cur.execute("select stud_id from student where stud_id=? and password=?",(self.user_stud.get(),self.pwd.get()))
                        user=cur.fetchone()
                        print(user)
                        ss=user[0]
                        print(ss,11)
                        if user==None:
                            messagebox.showerror('Invalid credentials', 'Try again with the correct credentials!!!!')
                        
                        p1=int(self.user_stud.get())
                       
                        if (ss==p1):
                            print(00)
                            try:
                                self.root.destroy()
                                
                                
                            finally:
                                subprocess.run(['python3','studentinfo.py'])
                        else:
                            print(100)

                    if user==None:
                        messagebox.showerror('Invalid credentials', 'Try again with the correct credentials!!!!')
                

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)



if  __name__=="__main__":
     root=Tk()
     obj=Login(root)
     root.mainloop()
