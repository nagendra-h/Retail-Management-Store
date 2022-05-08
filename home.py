from tkinter import*
from tkinter import messagebox
import sqlite3
import os
from PIL import Image,ImageTk
import time

class home:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Login System")
        self.my_canvas=Canvas(self.root,width=1350,height=700,bd=1)
        self.Lo=Image.open("images/n01.jpg")
        self.Lo=self.Lo.resize((1350,700),Image.ANTIALIAS)
        self.Lo=ImageTk.PhotoImage(self.Lo)
        self.my_canvas.create_image(0,0,image=self.Lo,anchor="nw")

        #self.my_canvas.create_image(0,0,image=self.L,anchor="nw")
        
        
        #self.e11=Label(self.root,image=self.L,bd=0)
        ##self.e11.pack(fill=X,expand=1)
        
        
        self.my_canvas.pack(fill="both",expand=True)
        self.my_canvas.create_text(720,60,text="RETAIL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),fill="PINK")

        btn_manage=Button(self.root,text="EMPLOYEE LOGIN",command=self.log,font=("times new roman",16,"italic"),fg="white",bg="#813F0B",cursor="hand2",bd=5)
        btn_manage.place(x=340,y=100,height=60,width=210)


        btn_view=Button(self.root,text="LOGOUT",command=self.logout,font=("times new roman",20,"italic"),fg="#D9DDDC",bg="#813F0B",cursor="hand2",bd=5)
        btn_view.place(x=640,y=100,height=60,width=210)
        
        btn_vview=Button(self.root,text="HOME PAGE",command=self.login,font=("times new roman",20,"italic"),fg="white",bg="#813F0B",cursor="hand2",bd=5)
        btn_vview.place(x=880,y=100,height=60,width=210)


    def log(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=loginn(self.new_win)
    def logout(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=logout(self.new_win)

    def login(self):
        self.root.destroy()
        os.startfile("login.py")
    
    

class loginn:
    def    __init__(self,root):
            self.root=root
            self.root.geometry("1200x450+100+190")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="white")
            self.root.focus_force()

            self.var_user_id=StringVar()
            self.var_name=StringVar()

            self.var_time=StringVar()

            self.var_dat=StringVar()

            self.var_tim=StringVar()

            self.Time=time.strftime("%I:%M:%S%p")

            self.dat=time.strftime("%d:%m:%Y")

            user_emp=Label(self.root,text="User_id",font=("times new roman" ,15, "bold"),fg="#D9DDDC",bg="#3A1F04",bd=3)
            user_emp.place(x=11,y=20,height=40,width=110)

            name_emp=Label(self.root,text="Name",font=("times new roman" ,15, "bold"),fg="#D9DDDC",bg="#3A1F04",bd=3)
            name_emp.place(x=611,y=20,height=40,width=110)

            doj_emp=Label(self.root,text="Login time",font=("times new roman" ,15, "bold"),fg="#D9DDDC",bg="#3A1F04",bd=3)
            doj_emp.place(x=11,y=80,height=40,width=110)

            doj_em=Label(self.root,text="Logout time",font=("times new roman" ,15, "bold"),fg="#D9DDDC",bg="#3A1F04",bd=3)
            doj_em.place(x=611,y=80,height=40,width=110)
            

            doj_emp=Label(self.root,text="Date",font=("times new roman" ,15, "bold"),fg="#D9DDDC",bg="#3A1F04",bd=3)
            doj_emp.place(x=11,y=160,height=40,width=110)
            
            

            user_Eemp=Entry(self.root,textvariable=self.var_user_id,font=("times new roman" ,15),fg="black",bg="white",bd=4)
            user_Eemp.place(x=271,y=23,height=40,width=210)

            ###---------NAME -----------
            nam_Eemp=Entry(self.root,textvariable=self.var_name,font=("times new roman" ,15),fg="black",bg="white",bd=4)
            nam_Eemp.place(x=871,y=20,height=40,width=210)

            user_emp=Label(self.root,text="User_id",font=("times new roman" ,15, "bold"),fg="#D9DDDC",bg="#3A1F04",bd=3)
            user_emp.place(x=11,y=20,height=40,width=110)

            nam_Eemp=Entry(self.root,textvariable=self.var_time,font=("times new roman" ,15),fg="black",bg="white",bd=4)
            nam_Eemp.place(x=271,y=80,height=40,width=210)
            nam_Eemp.insert(0,self.Time)

            nam_Eemp=Entry(self.root,textvariable=self.var_tim,font=("times new roman" ,15),fg="black",bg="white",bd=4)
            nam_Eemp.place(x=871,y=80,height=40,width=210)
            nam_Eemp.insert(0,"null")


            user_emp=Entry(self.root,textvariable=self.var_dat,font=("times new roman" ,15),fg="black",bg="white",bd=4)
            user_emp.place(x=271,y=160,height=40,width=210)
            user_emp.insert(0,self.dat)


            self.add_emp=Button(self.root,text="LOGIN",command=self.login,font=("times new roman" ,15),cursor="hand2",fg="#D9DDDC",bg="#3A1F04",bd=4)
            self.add_emp.place(x=271,y=250,height=40,width=110)

    def login(self):
            con=sqlite3.connect(database=r'coding.db')
            cur=con.cursor()
            try:
                if self.var_user_id.get()=="":
                    messagebox.showerror("Error","id must be required ",parent=self.root)
                else:
                    cur.execute("Select * from employee where user_id=?",(self.var_user_id.get(),))
                    row=cur.fetchone()
                    if row ==None:
                        messagebox.showerror("Error","This user_id is invalid",parent=self.root)
                    else:
                        cur.execute("Insert into login(id,name,time,date) values(?,?,?,?)",(
                            self.var_user_id.get(),
                            self.var_name.get(),
                            self.var_time.get(),
                            self.var_dat.get()
                        ))
                        con.commit()
                        messagebox.showinfo("Success","Employee login successfully",parent=self.root)
                        
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)


class logout:
    def    __init__(self,root):
            self.root=root
            self.root.geometry("1200x450+100+190")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="white")
            self.root.focus_force()

            self.L1=Image.open("images/tq.jpg")
            self.L1=self.L1.resize((1200,450),Image.ANTIALIAS)
            self.L1=ImageTk.PhotoImage(self.L1)
            #self.my_canvas.create_image(0,0,image=self.L,anchor="nw")
            
            
            self.e11=Label(self.root,image=self.L1,bd=0)
            self.e11.pack(fill=X,expand=1)

            
            #wind=self.my_canvas.create_window(720,380,window=self.e11)

            
            

            self.var_user_id=StringVar()

            self.var_name=StringVar()


            self.var_dat=StringVar()

            self.var_tim=StringVar()

            self.Time=time.strftime("%I:%M:%S%p")

            self.dat=time.strftime("%d:%m:%Y")

            user_emp=Label(self.root,text="User_id",font=("times new roman" ,15, "bold"),fg="#D9DDDC",bg="#3A1F04",bd=3)
            user_emp.place(x=11,y=20,height=40,width=110)

            '''name_emp=Label(self.root,text="Name",font=("times new roman" ,15, "bold"),fg="#D9DDDC",bg="#3A1F04",bd=3)
            name_emp.place(x=611,y=20,height=40,width=110)

            doj_emp=Label(self.root,text="Login time",font=("times new roman" ,15, "bold"),fg="#D9DDDC",bg="#3A1F04",bd=3)
            doj_emp.place(x=11,y=80,height=40,width=110)'''

            doj_em=Label(self.root,text="Logout time",font=("times new roman" ,15, "bold"),fg="#D9DDDC",bg="#3A1F04",bd=3)
            doj_em.place(x=611,y=20,height=40,width=110)
            

            
            user_Eemp=Entry(self.root,textvariable=self.var_user_id,font=("times new roman" ,15),fg="black",bg="white",bd=4)
            user_Eemp.place(x=271,y=20,height=40,width=210)

            ###---------NAME -----------
            
            
            
            nam_Eemp=Entry(self.root,textvariable=self.var_tim,font=("times new roman" ,15),fg="black",bg="white",bd=4)
            nam_Eemp.place(x=871,y=20,height=40,width=210)
            nam_Eemp.insert(0,self.Time)


            self.L=Image.open("images/exit.jpeg")
            self.L=self.L.resize((210,60),Image.ANTIALIAS)
            self.L=ImageTk.PhotoImage(self.L)
            
            self.add_emp=Button(self.root,image=self.L,command=self.login,font=("times new roman" ,15),cursor="hand2",bg="#3A1F04",bd=4)
            self.add_emp.place(x=271,y=160,height=60,width=210)

            
    def login(self):
            con=sqlite3.connect(database=r'coding.db')
            cur=con.cursor()
            try:
                if self.var_user_id.get()=="":
                    messagebox.showerror("Error","id must be required ",parent=self.root)
                else:
                    cur.execute("Select * from employee where user_id=?",(self.var_user_id.get(),))
                    row=cur.fetchone()
                    if row ==None:
                        messagebox.showerror("Error","This user_id is invalid",parent=self.root)
                    else:
                        cur.execute("Update login set tim=?  where id=?",(
                            self.var_tim.get(),
                            self.var_user_id.get()
                        ))
                        con.commit()
                        messagebox.showinfo("Success","Employee logout successfully",parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)

                    
            
            


            
          
            

    

if  __name__=="__main__":
     root=Tk()
     obj=home(root)
     root.mainloop()
