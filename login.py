from tkinter import*
from tkinter import messagebox
import sqlite3
import os
from PIL import Image,ImageTk




class Login:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Login System")
        self.root.config(bg="white")
        self.Frame1 = Frame(self.root)
        self.Frame1.place(relx=-0.02, rely=-0.02, relheight=0.21, relwidth=1.04)
        self.Frame1.configure(relief=FLAT, borderwidth="2",background="red", width=625)

        self.MenuLogo=Image.open("images/im2.png")
        self.MenuLogo=self.MenuLogo.resize((170,70),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        title=Label(self.Frame1,text="Retail Management  System",image=self.MenuLogo,compound=LEFT,font=("times new roman",40,"bold"),bg="black",fg="red").place(x=0,y=0,relwidth=1,height=170)


          #####IMAGE##############
        

        self.Logo1=ImageTk.PhotoImage(file="images/im1.png")
        self.Logo2=ImageTk.PhotoImage(file="images/im2.png")
        self.Logo3=ImageTk.PhotoImage(file="images/im3.png")
        
        self.Log=Image.open("images/phone.png")
        self.Log=self.Log.resize((350,510),Image.ANTIALIAS)
        self.Log=ImageTk.PhotoImage(self.Log)
        

        self.phone_im=Label(self.root,image=self.Log)
        self.phone_im.place(x=50, y=170,width=350,height=530)

        self.phone_im=Label(self.root,bg="white")
        self.phone_im.place(x=185, y=269,width=184,height=351)

        
###########+++++++++++++++++++++++++++++++    

        self.loginLabel = Label(self.root)
        self.loginLabel.place(relx=0.50, rely=0.30, height=31, width=94)
        self.loginLabel.configure(background="#d9d9d9", disabledforeground="#a3a3a3", font='arial 18 bold', foreground="#000000", width=94)
        self.loginLabel.configure(text='''Log In''')

        self.user_l = Label(self.root)
        self.user_l.place(relx=0.35, rely=0.40, height=31, width=144)
        self.user_l.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9", disabledforeground="#a3a3a3", font='arial 18 bold')
        self.user_l.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black")
        self.user_l.configure(text='''Username''')

        self.txtuser_e = Entry(self.root)
        self.txtuser_e.place(relx=0.5, rely=0.40, height=30, relwidth=0.15)
        self.txtuser_e.configure(background="white", borderwidth="3", disabledforeground="#a3a3a3", font='arial 18 bold', foreground="#000000", highlightbackground="#d9d9d9")
        self.txtuser_e.configure(highlightcolor="black", insertbackground="black", selectbackground="#c4c4c4", selectforeground="black")

        self.pass_l = Label(self.root)
        self.pass_l.place(relx=0.35, rely=0.50, height=31, width=144)
        self.pass_l.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9", disabledforeground="#a3a3a3", font='arial 18 bold')
        self.pass_l.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black")
        self.pass_l.configure(text='''Password''')

        self.txtpass_e = Entry(self.root, show='*')
        self.txtpass_e.place(relx=0.5, rely=0.50, height=30, relwidth=0.15)
        self.txtpass_e.configure(background="white", borderwidth="3", disabledforeground="#a3a3a3", font='arial 18 bold', foreground="#000000", highlightbackground="#d9d9d9")
        self.txtpass_e.configure(highlightcolor="black", insertbackground="black", selectbackground="#c4c4c4", selectforeground="black")

        self.BtnLogin = Button(self.root)
        self.BtnLogin.place(relx=0.5, rely=0.60, height=34, width=150)
        self.BtnLogin.configure(activebackground="#d9d9d9", activeforeground="#000000", font='arial 10 bold', background="#d9d9d9", cursor="hand2", disabledforeground="#a3a3a3")
        self.BtnLogin.configure(foreground="black", highlightbackground="#d9d9d9", highlightcolor="black", pady="0", width=100)
        self.BtnLogin.configure(text='''Login''', command=self.login)

        self.BtnLogin = Button(self.root,text="Admin Login",command=self.alogin,font=("times new roman",20,"italic"),bg="brown",bd=3,cursor="hand2",anchor="w").place(relx=0.5, rely=0.740, height=34, width=190)

        self.ani()

    def ani(self):
        self.im=self.Logo1
        self.Logo1=self.Logo2
        self.Logo2=self.Logo3
        self.Logo3=self.im
        self.phone_im.config(image=self.im)
        self.phone_im.after(1200,self.ani)
        
        

    def login(self): 
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.txtuser_e.get() == "" and  self.txtpass_e.get()== "":
                messagebox.showerror("Error", "All fields are required",parent=self.root)
            else:
                cur.execute("select utype from employee where user_id=? and password=?",(self.txtuser_e.get(),self.txtpass_e.get()))
                user=cur.fetchone()
                if user==None:  #and  
                    messagebox.showerror('Invalid credentials', 'Try again with the correct credentials!!!!')
                print(user)
                if  user==('employee',):
                    print(1)
                    self.root.destroy()
                    os.startfile("employee.py")
       
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)

    def  alogin(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.txtuser_e.get() == "" and  self.txtpass_e.get()== "":
                messagebox.showerror("Error", "All fields are required",parent=self.root)
            else:
                cur.execute("select name from admin where aid=? and password=?",(self.txtuser_e.get(),self.txtpass_e.get()))
                print(1)
                admi=cur.fetchone()
                if admi==None:
                    messagebox.showerror('Invalid credentials', 'Try again with the correct credentials!!!!') 
                if admi==('rama',):
                        self.root.destroy()
                        os.startfile("dashboard.py")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)                
        

if  __name__=="__main__":
     root=Tk()
     obj=Login(root)
     root.mainloop()
