from tkinter import*
import os
import time
from tkinter import ttk,messagebox
#from PIL import Image,ImageTk
from emp import  EMP
#import time
#import sqlite3
class random:
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1350x700+0+0")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="black")
            
            #  title
            self.icon_title=PhotoImage(file="images/logo1.png")
            
            
            title=Label(self.root,text="Retail Management  System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="black",fg="red").place(x=0,y=0,relwidth=1,height=70)

             #  button log out
            #btn_log=Button(self.root,text="LOGOUT",command=self.logout,font=("times new roman",10,"italic"),bg="yellow",fg="orange",cursor="hand2",anchor="w",padx=30).place(x=1150,y=20,height=30,width=110)
                
            self.b_title=Label(self.root,text="Welcome to Retail Management  Store \t\tDate=DD:MM:YYYY\t\tTime=II:MM:SS:P",font=("times new roman",10,"bold"),bg="brown",fg="red")
            self.b_title.place(x=0,y=70,relwidth=1,height=30)
            self.update_time()
            
            

        
                
            


           ''' #            left menu
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
                

            self.empp=Label(self.root,text="Total Employee\n[0]",bd=5,font=("times new roman",15),bg="#808588",fg="#FFFDD0")
            self.empp.place(x=375,y=102,width=170,height=100)

            self.pr=Label(self.root,text="Total Product\n[0]",bd=5,font=("times new roman",15),bg="#808588",fg="#FFFDD0")
            self.pr.place(x=655,y=102,width=170,height=100)

            self.sal=Label(self.root,text="Total Supplier\n[0]",bd=5,font=("times new roman",15),bg="#808588",fg="#FFFDD0")
            self.sal.place(x=935,y=102,width=170,height=100)
            '''
            
            lab_menu=Label(leftmenu,text="MENU",font=("times new roman",10),bg="#009688").pack(side=TOP,fill=X)

            btn_emp=Button(leftmenu,text="EMPLOYEE",command=self.employee,image=self.Logo,compound=LEFT,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",anchor="w").pack(side=TOP,fill=X)



            #self.update_content()

            

        def employee(self):
           self.new_win=Toplevel(self.root)
           self.new_obj=EMP(self.new_win)
           

     '''   def  update_time(self):
                
                tim=time.strftime("%I:%M:%S%p")
                dat=time.strftime("%d:%m:%Y")
                self.b_title.config(text=f"Welcome to Retail Management  Store\t\tDate: {str(dat)}\t\t Time: {str(tim)}")
                self.b_title.after(200,self.update_time)
'''
if  __name__=="__main__":
     root=Tk()
     obj=random(root)
     root.mainloop()
                
                
