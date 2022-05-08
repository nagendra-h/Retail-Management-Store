from tkinter import*
import os
import time
from emp import  EMP
from sup  import  SUP
from prod  import  PRODUCT
from bill  import  bill
import time
class IMS:
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1350x700+0+0")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="white")


            #  title
            
            title=Label(self.root,text="Retail Management  ",font=("times new roman",40,"bold"),bg="blue",fg="green",padx=20).place(x=0,y=0,relwidth=1,height=70)

             #  button log out
            #btn_log=Button(self.root,text="LOGOUT",command=self.logout,font=("times new roman",10,"italic"),bg="yellow",fg="orange",cursor="hand2",anchor="w",padx=30).place(x=1150,y=20,height=30,width=110)
                
            self.b_title=Label(self.root,text="Welcome  to Retail Management ",font=("times new roman",15,"bold"),bg="grey",fg="white").place(x=0,y=70,relwidth=1,height=30)
            '''
            tim=time.strftime("%I%M%S")
            dat=time.strftime("%d%m%Y")
            self.b_title.config(text=f'Welcome  to Retail Management \t\tTime: {str(tim)}\t\t Date: {str(dat)}')
            '''


            #            left menu
            leftmenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
            leftmenu.place(x=0,y=102,width=200,height=565)


            lbl_menulogo=Label(leftmenu,text="image",font=(10)).pack(side=TOP,fill=X)
            
            
            lab_menu=Label(leftmenu,text="MENU",font=("times new roman",10),bg="#009688").pack(side=TOP,fill=X)

            btn_emp=Button(leftmenu,text="EMPLOYEE",command=self.employee,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

            btn_pro=Button(leftmenu,text="PRODUCTS",command=self.product,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

            btn_sup=Button(leftmenu,text="SUPPLIER",command=self.supplier,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

            btn_bill=Button(leftmenu,text="BILL",command=self.bill,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

            btn_exit=Button(leftmenu,text="EXIT",command=self.logout,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

            


        def employee(self):
           self.new_win=Toplevel(self.root)
           self.new_obj=EMP(self.new_win)
           
          # self.b_title.after(200,self.employee)



        def supplier(self):
           self.new_win=Toplevel(self.root)
           self.new_obj=SUP(self.new_win)
           
        def bill(self):
           self.new_win=Toplevel(self.root)
           self.new_obj=bill(self.new_win)
           
        def logout(self):
                self.root.destroy()
                os.startfile("login.py")



        def product(self):
           self.new_win=Toplevel(self.root)
           self.new_obj=PRODUCT(self.new_win)

        
                 

if  __name__=="__main__":
     root=Tk()
     obj=IMS(root)
     root.mainloop()

