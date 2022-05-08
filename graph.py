from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import webbrowser
from tkhtmlview import HTMLLabel
import sqlite3
from tkinter import messagebox 
import time
import os
from PIL import ImageTk,Image
class Student:
    
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

        title=Label(self.root,text="Placement details",font=("goudy old style",25),bg="#47476b",fg="black").place(x=0,y=130,relwidth=1)
        
        ######VARIABLES ++++++++++
        self.var_stud_id=StringVar()
        self.var_en=StringVar()
        self.var_stud_cp=StringVar()
    ######## Labels ++++++++++
        user_stud=Label(self.root,text="Company",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        user_stud.place(x=61,y=190,height=40,width=110)

        self.user_Estud=Entry(self.root,textvariable=self.var_stud_cp,font=("times new roman" ,15),bg="white",bd=4)
        self.user_Estud.place(x=271,y=190,height=40,width=210)

        
        
        btn_exit=Button(self.root,text="VIEW",command=self.plot1,font=("times new roman",20,"bold"),bg="brown",bd=3,cursor="hand2",anchor="w").place(x=501,y=190,height=40,width=210)

        btn_exit=Button(self.root,text="CLEAR",command=self.clear,font=("times new roman",20,"bold"),bg="brown",bd=3,cursor="hand2",anchor="w").place(x=781,y=190,height=40,width=210)


        u_stud=Label(self.root,text="User_id",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        u_stud.place(x=61,y=240,height=40,width=110)

        self.u_Estud=Entry(self.root,textvariable=self.var_stud_id,font=("times new roman" ,15),bg="white",bd=4)
        self.u_Estud.place(x=261,y=240,height=40,width=210)

        self.u_En=Entry(self.root,textvariable=self.var_en,font=("times new roman" ,15),bg="white",bd=4,state='disabled')
        self.u_En.place(x=481,y=240,height=40,width=210)


        
        
        btn_exit=Button(self.root,text="Result",command=self.result,font=("times new roman",20,"bold"),bg="brown",bd=3,cursor="hand2",anchor="w").place(x=771,y=240,height=40,width=210)


        leftmenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        leftmenu.place(x=0,y=302,width=300,height=1000)

        self.MenuLogo=Image.open("images/rv.jpeg")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenuLogo=Label(leftmenu,image=self.MenuLogo)
        LeftMenuLogo.pack(side=TOP,fill=X)
        self.btn_exit1=Button(leftmenu,text="Amazon",command=self.browser1,font=("times new roman",20,"bold"),bg="brown",bd=3,cursor="hand2",anchor="w").pack(side=TOP,fill=X)
        self.btn_exit2=Button(leftmenu,text="Wipro",command=self.browser2,font=("times new roman",20,"bold"),bg="brown",bd=3,cursor="hand2",anchor="w").pack(side=TOP,fill=X)
        self.btn_exit3=Button(leftmenu,text="Infosys",command=self.browser3,font=("times new roman",20,"bold"),bg="brown",bd=3,cursor="hand2",anchor="w").pack(side=TOP,fill=X)
        self.btn_exit4=Button(leftmenu,text="Flipcart",command=self.browser4,font=("times new roman",20,"bold"),bg="brown",bd=3,cursor="hand2",anchor="w").pack(side=TOP,fill=X)
        self.btn_exit5=Button(leftmenu,text="Google",command=self.browser5,font=("times new roman",20,"bold"),bg="brown",bd=3,cursor="hand2",anchor="w").pack(side=TOP,fill=X)
        self.btn_exit6=Button(leftmenu,text="Phone pay",command=self.browser6,font=("times new roman",20,"bold"),bg="brown",bd=3,cursor="hand2",anchor="w").pack(side=TOP,fill=X)
        self.btn_exit7=Button(leftmenu,text="Reliance",command=self.browser7,font=("times new roman",20,"bold"),bg="brown",bd=3,cursor="hand2",anchor="w").pack(side=TOP,fill=X)
        self.btn_exit8=Button(leftmenu,text="Tcs",command=self.browser8,font=("times new roman",20,"bold"),bg="brown",bd=3,cursor="hand2",anchor="w").pack(side=TOP,fill=X)

        my_label = HTMLLabel(leftmenu, html="""
    <a href='home1.html'>Basic info</a>""")
        my_label.pack(side=TOP,fill=X)

       
    def az(self,a,b):
        
        
        # the figure that will contain the plot
        self.fig = Figure(figsize = (5, 5),
                     dpi = 100)
      
        # list of squares
        x = a
        # corresponding y axis values
        y = b
 
      
        # adding the subplot
        plot1 = self.fig.add_subplot(111)
      
        # plotting the graph
        plot1.plot(x,y)
        plot1.set_xlabel('Year')
        plot1.set_ylabel('Students Selected')     
        # creating the Tkinter canvas
        # containing the Matplotlib figure
        self.canvas = FigureCanvasTkAgg(self.fig,
                                   master = self.root)
        
        self.canvas.draw()
        cn=self.canvas
        # placing the canvas on the Tkinter root
        self.canvas.get_tk_widget().pack(padx=500,pady=300)
      
        # creating the Matplotlib toolbar
        #self.toolbar = NavigationToolbar2Tk(self.canvas,
                                       
       

        #self.toolbar.update()
      
        # placing the toolbar on the Tkinter root
        self.canvas.get_tk_widget().pack()        
      
    def plot1(self):
        
        if self.user_Estud.get()=='Amazon':
            self.az([2016,2017,2018,2019,2020,2021,2022],[24,49,77,54,73,63,99])
        elif self.user_Estud.get()=='Reliance':
            self.az([2016,2017,2018,2019,2020,2021,2022],[20,49,77,34,83,53,89])
        elif self.user_Estud.get()=='Infosys':
            self.az([2016,2017,2018,2019,2020,2021,2022],[55,49,77,54,43,43,79])
        elif self.user_Estud.get()=='Wipro':
            self.az([2016,2017,2018,2019,2020,2021,2022],[31,49,77,54,23,23,69])
        elif self.user_Estud.get()=='Flipcart':
            self.az([2016,2017,2018,2019,2020,2021,2022],[17,49,77,54,93,83,59])
        elif self.user_Estud.get()=='Google':
            self.az([2016,2017,2018,2019,2020,2021,2022],[14,49,77,54,83,63,49])
        elif self.user_Estud.get()=='Phone pay':
            self.az([2016,2017,2018,2019,2020,2021,2022],[21,49,77,54,43,23,39])
        elif self.user_Estud.get()=='Tcs':
            self.az([2016,2017,2018,2019,2020,2021,2022],[29,49,77,54,63,33,29])
        
        else:
            print("no")
    def clear(self):
        self.var_stud_id.set("")
        self.var_stud_cp.set("")
        self.var_en.set("")
        self.u_En.config(state='disabled')
        self.canvas.get_tk_widget().pack_forget()

    def browser1(self):
        webbrowser.open_new("https://en.wikipedia.org/wiki/Amazon_(company)")
    def browser2(self):
        webbrowser.open_new("https://en.wikipedia.org/wiki/Wipro")
    def browser3(self):
        webbrowser.open_new("https://en.wikipedia.org/wiki/Infosys")
            
    def browser4(self):
        webbrowser.open_new("https://en.wikipedia.org/wiki/Flipcart")
            
    def browser5(self):
        webbrowser.open_new("https://en.wikipedia.org/wiki/Google")
            
    def browser6(self):
        webbrowser.open_new("https://en.wikipedia.org/wiki/Phone pay")
            
    def browser7(self):
        webbrowser.open_new("https://en.wikipedia.org/wiki/Reliance")
            
    def browser8(self):
        webbrowser.open_new("https://en.wikipedia.org/wiki/Tcs")

    def result(self):
        
        con=sqlite3.connect(database=r'student.db')
        cur=con.cursor()
        try:
            if self.var_stud_id.get() == "":
                
                messagebox.showerror("Error", "All fields are required",parent=self.root)
               
            else:
                print(100)
                cur.execute("select status from student where stud_id=? ",(self.var_stud_id.get(),))
                user=cur.fetchone()
                print(user)
                print(000)
                ss=user[0]
                self.u_En.config(state='normal')
                self.var_en.set(ss)
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)
    

        
    def  update_time(self):        
        tim=time.strftime("%I:%M:%S%p")
        dat=time.strftime("%d:%m:%Y")
        self.b_title.config(text=f"Welcome \t\tDate: {str(dat)}\t\t Time: {str(tim)}")
        self.b_title.after(200,self.update_time)


if  __name__=="__main__":
     root=Tk()
     obj=Student(root)
     root.mainloop()
