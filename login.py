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
        self.my_canvas=Canvas(self.root,width=1350,height=700,bd=1)
        self.Lo=Image.open("images/n01.jpg")
        self.Lo=self.Lo.resize((1350,700),Image.ANTIALIAS)
        self.Lo=ImageTk.PhotoImage(self.Lo)
        self.my_canvas.create_image(0,0,image=self.Lo,anchor="nw")
        
        self.my_canvas.pack(fill="both",expand=True)
        self.my_canvas.create_text(720,60,text="RETAIL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),fill="PINK")

        #self.root.config(bg="white")
        #self.root.overrideredirect(1) # Remove shadow & drag bar. Note: Must be used before wm calls otherwise these will be removed.
        '''self.root.call("wm", "attributes", ".", "-topmost", "true") # Always keep window on top of others
        self.root.geometry("1350x700+0+0") # Set offset from top-left corner of screen as well as size
        self.root.call("wm", "attributes", ".", "-transparent",self.root['bg']) # Remove shadow from window'''
        
        #self.phone_i=Label(self.root,image=self.Lo)
        #self.phone_i.place(x=0,y=0,width=1350,height=700)

        
        '''self.root.call("wm", "attributes", ".", "-fullscreen", "true") # Fullscreen mode
        self.root.call("wm", "attributes", ".", "-alpha", "0.9") # Window Opacity 0.0-1.0
        self.root.call("wm", "attributes", ".", "-modified", "0.9") # Toggles modified state of the close-window icon.'''

        #self.root.wm_attributes("-transperncy","red")
        self.L=Image.open("images/n01.jpg")
        self.L=self.L.resize((625,400),Image.ANTIALIAS)
        self.L=ImageTk.PhotoImage(self.L)
        #self.my_canvas.create_image(0,0,image=self.L,anchor="nw")
        
        
        self.e11=Label(image=self.L,bd=0)
        self.e11.pack(fill=X,expand=1)
        wind=self.my_canvas.create_window(720,380,window=self.e11)
        
        '''self.MenuLogo=Image.open("images/im2.png")
        self.MenuLogo=self.MenuLogo.resize((170,70),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)#image=self.MenuLogo,compound=LEFT,

        #title=Label(self.root,text="Retail Management  System",font=("times new roman",40,"bold"),fg="red",bd=0).place(x=0,y=0,relwidth=1,height=170)'''


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
        
        '''self.Log=Image.open("images/p1.png")
        self.Log=self.Log.resize((350,510),Image.ANTIALIAS)
        self.Log=ImageTk.PhotoImage(self.Log)
        

        self.phone_im=Label(self.root,image=self.Log)
        self.phone_im.place(x=95, y=170,width=350,height=530)

        self.phone_im=Label(self.root)
        self.phone_im.place(x=195, y=269,width=177,height=351)'''

        
###########+++++++++++++++++++++++++++++++
        self.g3=Image.open("images/u1.png")
        self.g3=self.g3.resize((35,40),Image.ANTIALIAS)
        self.g3=ImageTk.PhotoImage(self.g3)

        self.g13=Image.open("images/pa1.png")
        self.g13=self.g13.resize((50,40),Image.ANTIALIAS)
        self.g13=ImageTk.PhotoImage(self.g13)

        self.g1=Image.open("images/pa2.png")
        self.g1=self.g1.resize((50,40),Image.ANTIALIAS)
        self.g1=ImageTk.PhotoImage(self.g1)
        
        
        self.use_l = Label(self.root,text="LOGIN",bd=6,font=("arial",20,"bold"), fg="BLACK")
        self.use_l.place(relx=0.50, rely=0.30, height=31, width=154)        
        #self.user_l.configure(font=("arial",10,"italic"), bg="pink", fg="black")
        #self.user_l.configure(text='''LOGIN''')


        self.user_l = Label(self.root,image=self.g3,compound=RIGHT)
        self.user_l.place(relx=0.35, rely=0.40, height=41, width=144)
        self.user_l.configure(font=("arial 18 bold",19,"bold"), fg="black",bd=5)
        self.user_l.configure(text='''User Id''')

        self.txtuser_e = Entry(self.root)
        self.txtuser_e.place(relx=0.5, rely=0.40, height=30, relwidth=0.15)
        self.txtuser_e.configure(background="white", borderwidth="3", disabledforeground="#a3a3a3", font='arial 18 bold', foreground="#000000", highlightbackground="#d9d9d9")
        self.txtuser_e.configure(highlightcolor="black", insertbackground="white", selectbackground="#c4c4c4", selectforeground="black")

        self.pass_l = Label(self.root)
        self.pass_l.place(relx=0.32, rely=0.50, height=41, width=158)
        self.pass_l.configure(font=("arial 18 bold",19,"bold"), fg="black",bd=5)
        self.pass_l.configure(text='''Password''')

        self.btn=True

        self.b1=Button(self.root,cursor="hand2",image=self.g13,command=self.p,font=("arial 18 bold",19,"bold"),bd=3)
        self.b1.place(relx=0.44, rely=0.50, height=40, width=70)
        #self.b1=Button(self.root,cursor="hand2",image=self.g1,command=self.pa,font=("arial 18 bold",19,"bold"),bd=3)
        #self.b1.place(relx=0.66, rely=0.50, height=37, width=70)

        self.txtpass_e = Entry(self.root, show='*')
        self.txtpass_e.place(relx=0.51, rely=0.50, height=30, relwidth=0.14)
        self.txtpass_e.configure(font=("arial 18 bold",19,"bold"), fg="black")
        
        self.BtnLogin = Button(self.root,cursor="hand2")
        self.BtnLogin.place(relx=0.5, rely=0.60, height=34, width=150)
        self.BtnLogin.configure(font=("arial 18 bold",19,"bold"), fg="black")#,bg="#4F7942")
        self.BtnLogin.configure(text='''Login''', command=self.login)

        self.BtnLogin = Button(self.root,text="Admin Login",command=self.alogin,font=("times new roman",20,"italic"),bg="white",bd=5,cursor="hand2",anchor="w").place(relx=0.5, rely=0.740, height=34, width=190)

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
            self.p=self.txtpass_e.get()
            self.txtpass_e.config(show=self.p)
            self.btn=False
        else:
            self.txtpass_e.config(show='*')
            self.b1.config(image=self.g13)
            self.btn=True
        #self.p=self.txtpass_e.get()
        
        

    '''def pa(self):
        self.p=self.txtpass_e.get()
        self.txtpass_e.config(show=self.p)'''
        

    def login(self): 
        con=sqlite3.connect(database=r'coding.db')
        cur=con.cursor()
        try:
            if self.txtuser_e.get() == "" or  self.txtpass_e.get()== "":
                messagebox.showerror("Error", "All fields are required",parent=self.root)
            else:
                cur.execute("select utype from employee where user_id=? and password=?",(self.txtuser_e.get(),self.txtpass_e.get()))
                user=cur.fetchone()
                if user==None:  #and  
                    messagebox.showerror('Invalid credentials', 'Try again with the correct credentials!!!!')
                print(user)
                if  user==('Employee',):
                  #  print(1)
                    self.root.destroy()
                    os.startfile("employee.py")
                    
                    
       
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)

    def  alogin(self):
        con=sqlite3.connect(database=r'coding.db')
        cur=con.cursor()
        try:
            if self.txtuser_e.get() == "" or  self.txtpass_e.get()== "":
                messagebox.showerror("Error", "All fields are required",parent=self.root)
            else:
                cur.execute("select name from admin where aid=? and password=?",(self.txtuser_e.get(),self.txtpass_e.get()))
                #print(1)
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
