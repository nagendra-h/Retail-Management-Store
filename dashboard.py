from tkinter import*
import os
import time
from tkinter import ttk,messagebox
from tkinter.ttk import  Progressbar
from PIL import Image,ImageTk
from emp import  EMP
from sup  import  SUP
from prod  import  PROD
from bill  import  BILLS
import time
import sqlite3
import threading
class IMS:
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1350x700+0+0")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="brown")

            

            #  title
            self.icon_title=PhotoImage(file="images/logo1.png")
            
            
            title=Label(self.root,text="Retail Management  System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="black",fg="red").place(x=0,y=0,relwidth=1,height=70)

            bt_exit=Button(self.root,text="VIEW",command=self.log,compound=LEFT,font=("times new roman",20,"bold"),bg="black",fg="red",bd=3,cursor="hand2",anchor="w").place(x=1100,y=0,width=90,height=60)

                
            self.b_title=Label(self.root,text="Welcome to Retail Management  Store \t\tDate=DD:MM:YYYY\t\tTime=II:MM:SS:P",font=("times new roman",10,"bold"),bg="brown",fg="red")
            self.b_title.place(x=0,y=70,relwidth=1,height=30)
            self.update_time()
            
            
        #            left menu
            leftmenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
            leftmenu.place(x=0,y=102,width=200,height=500)

            self.MenuLogo=Image.open("images/menu_im.png")
            self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
            self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

            LeftMenuLogo=Label(leftmenu,image=self.MenuLogo)
            LeftMenuLogo.pack(side=TOP,fill=X)

            self.Logo=Image.open("images/side.png")
            self.Logo=self.Logo.resize((20,20),Image.ANTIALIAS)
            self.Logo=ImageTk.PhotoImage(self.Logo)
                

            
            lab_menu=Label(leftmenu,text="MENU",font=("times new roman",10),bg="#009688").pack(side=TOP,fill=X)

            btn_emp=Button(leftmenu,text="EMPLOYEE",command=self.employee,image=self.Logo,compound=LEFT,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",anchor="w")
            btn_emp.pack(side=TOP,fill=X)

            btn_pro=Button(leftmenu,text="SUPPLIER",command=self.supplier,image=self.Logo,compound=LEFT,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",anchor="w").pack(side=TOP,fill=X)

            btn_sup=Button(leftmenu,text="PRODUCTS",command=self.product,image=self.Logo,compound=LEFT,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",anchor="w").pack(side=TOP,fill=X)

            btn_bill=Button(leftmenu,text="BILL",command=self.bill,image=self.Logo,compound=LEFT,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",anchor="w").pack(side=TOP,fill=X)

            btn_exit=Button(leftmenu,text="EXIT",command=self.logout,image=self.Logo,compound=LEFT,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",anchor="w").pack(side=TOP,fill=X)
            
            self.bns=False
            self.onimg=Image.open("images/switch on.png")
            self.onimg=self.onimg.resize((80,30),Image.ANTIALIAS)
            self.onimg=ImageTk.PhotoImage(self.onimg)
            
            self.offimg=Image.open("images/switch off.png")
            self.offimg=self.offimg.resize((80,30),Image.ANTIALIAS)
            self.offimg=ImageTk.PhotoImage(self.offimg)
            

            self.t=Label(self.root,text="Dark Mode: OFF",font=("times new roman",10,"bold"),fg="#FF2800",bg="#4B3619")
            self.t.place(x=5,y=630,width=130,height=40)

            self.btn=Button(self.root,text="OFF",command=self.switchh,font=("times new roman",17),fg="#FF2800",bg="white",image=self.offimg)
            self.btn.place(x=140,y=630,width=80,height=40)


        def switchh(self):
            #global bns
            #bns=False
            if self.bns:
                self.btn.config(image=self.offimg,bg="white")
                self.root.config(bg="brown")
                self.t.config(text="Dark Mode: OFF",bg="brown")
                self.bns=False
            else:
                self.btn.config(image=self.onimg,bg="white")
                self.root.config(bg="black")
                self.t.config(text="Dark Mode: ON",bg="black")
                self.bns=True
        def log(self):
                #self.root.destroy()
                os.startfile("employee.py")
                    

            
        def employee(self):
           style=ttk.Style()
           style.theme_use('alt')
           style.configure("orange.Horizontal.TProgressbar",fg="orange",bg="black")
           l1=Label(self.root,text="Loading..",bg="black",fg="red",bd=0)
           l1.place(x=230,y=102)
           pp=Progressbar(self.root,style="orange.Horizontal.TProgressbar",orient="horizontal",length=600,mode="determinate",value=1)
           pp.place(x=220,y=120,width=1000)
           r=0
           for i in range(100):
                   pp['value']=r
                   root.update_idletasks()
                   time.sleep(0.001)
                   r +=1
           self.new_win=Toplevel(self.root)
           self.new_obj=EMP(self.new_win)
           l1.destroy()
           pp.destroy()
           

        def  update_time(self):
                tim=time.strftime("%I:%M:%S%p")
                dat=time.strftime("%d:%m:%Y")
                self.b_title.config(text=f"Welcome to Retail Management  Store\t\tDate: {str(dat)}\t\t Time: {str(tim)}")
                self.b_title.after(100,self.update_time)
                
                
        
        def supplier(self):
           style=ttk.Style()
           style.theme_use('alt')
           style.configure("orange.Horizontal.TProgressbar",fg="orange",bg="black")
           l1=Label(self.root,text="Loading..",bg="black",fg="red",bd=0)
           l1.place(x=230,y=102)
           pp=Progressbar(self.root,style="orange.Horizontal.TProgressbar",orient="horizontal",length=600,mode="determinate",value=1)
           pp.place(x=220,y=120,width=1000)
           r=0
           for i in range(100):
                   pp['value']=r
                   root.update_idletasks()
                   time.sleep(0.001)
                   r +=1
           
           self.new_win=Toplevel(self.root)
           self.new_obj=SUP(self.new_win)
           l1.destroy()
           pp.destroy()
           
           
           
        def bill(self):
           style=ttk.Style()
           style.theme_use('alt')
           style.configure("orange.Horizontal.TProgressbar",fg="orange",bg="black")
           l1=Label(self.root,text="Loading..",bg="black",fg="red",bd=0)
           l1.place(x=230,y=102)
           pp=Progressbar(self.root,style="orange.Horizontal.TProgressbar",orient="horizontal",length=600,mode="determinate",value=1)
           pp.place(x=220,y=120,width=1000)
           r=0
           for i in range(100):
                   pp['value']=r
                   root.update_idletasks()
                   time.sleep(0.001)
                   r +=1
           
           self.new_win=Toplevel(self.root)
           self.new_obj=BILLS(self.new_win)
           l1.destroy()
           pp.destroy()
           
           
           
        def logout(self):
                self.root.destroy()
                os.startfile("login.py")



        def product(self):
           style=ttk.Style()
           style.theme_use('alt')
           style.configure("orange.Horizontal.TProgressbar",fg="orange",bg="black")
           l1=Label(self.root,text="Loading..",bg="black",fg="red",bd=0)
           l1.place(x=230,y=102)
           pp=Progressbar(self.root,style="orange.Horizontal.TProgressbar",orient="horizontal",length=600,mode="determinate",value=1)
           pp.place(x=220,y=120,width=1000)
           r=0
           for i in range(100):
                   pp['value']=r
                   root.update_idletasks()
                   time.sleep(0.001)
                   r +=1
           
           self.new_win=Toplevel(self.root)
           self.new_obj=PROD(self.new_win)
           l1.destroy()
           pp.destroy()
           
           
if  __name__=="__main__":
     root=Tk()
     obj=IMS(root)
     root.mainloop()

