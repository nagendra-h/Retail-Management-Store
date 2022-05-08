from tkinter import*
from tkinter import ttk
#from manageemp import MEMP
import sqlite3
from PIL import Image,ImageTk
from tkcalendar import  Calendar,DateEntry
from tkinter import ttk,messagebox
#from empview import VEMP



class EMP:
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1350x710+0+0")#1140x560+210+130")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="white")
            self.root.focus_force()
            self.my_canvas=Canvas(self.root,width=1350,height=80,bd=1)
            '''self.Lo=Image.open("images/bgg1.jpeg")
            self.Lo=self.Lo.resize((1350,40),Image.ANTIALIAS)
            self.Lo=ImageTk.PhotoImage(self.Lo)
            self.my_canvas.create_image(50,30,image=self.Lo)'''
                
            self.my_canvas.place(x=0,y=0)
            self.my_canvas.configure(bg="#622A0F")
            self.my_canvas.create_text(650,40,text="MANAGE EMPLOYEE",font=("times new roman",30,"bold"),fill="white")

            self.phone_im=Label(self.root,bd=3)#image=self.Lo)
            self.phone_im.place(x=0,y=90,width=1350,height=610)
            

            '''self.Lo=Image.open("images/bgg2.jpeg")
            self.Lo=self.Lo.resize((1340,710),Image.ANTIALIAS)
            self.Lo=ImageTk.PhotoImage(self.Lo)'''
            self.Logo1=Image.open("images/e11.jpg")
            self.Logo1=self.Logo1.resize((1340,610),Image.ANTIALIAS)
            self.Logo1=ImageTk.PhotoImage(self.Logo1)
            
            self.Logo2=Image.open("images/e12.jpg")
            self.Logo2=self.Logo2.resize((1340,710),Image.ANTIALIAS)
            self.Logo2=ImageTk.PhotoImage(self.Logo2)
            
            

            
           # my_canvas=Canvas(self.root,width=1140,height=560)
            #my_canvas.pack(fill="both",expand=True)
            '''my_canvas.create_image(0,0,image=self.Lo,anchor="nw")
            my_canvas.create_text(520,30,text="EMPLOYEE DETAILS",font=("times new roman",40,"bold"),fill="grey")'''

            

#-----------------------TITLE---------------------------------------------
            #emp_title=Label(self.root,text="EMPLOYEE DETAILS",font=("times new roman",40,"bold"),fg="#FF2800",bg="grey",bd=4,relief=RIDGE,padx=20).place(x=0,y=0,relwidth=1,height=60)

   #  button MANAGE AND VIEW
            btn_manage=Button(self.root,text="MANAGE EMPLOYEE",command=self.memployee,font=("times new roman",16,"italic"),fg="white",bg="#813F0B",cursor="hand2",bd=5)
            btn_manage.place(x=340,y=70,height=60,width=210)


            btn_view=Button(self.root,text="VIEW",command=self.vemployee,font=("times new roman",20,"italic"),fg="white",bg="#813F0B",cursor="hand2",bd=5)
            btn_view.place(x=640,y=70,height=60,width=210)

            self.ani()

            '''leftmenu=Frame(self.root,bd=0,relief=RIDGE,bg="grey")
            leftmenu.place(x=200,y=150,width=600,height=400)

            self.MenuLogo=Image.open("images/bg.png")
            self.MenuLogo=self.MenuLogo.resize((580,380),Image.ANTIALIAS)
            self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

            LeftMenuLogo=Label(leftmenu,image=self.MenuLogo,bg="grey")
            LeftMenuLogo.pack(side=TOP,fill=BOTH)'''
            




##----------MANAGE EMP DETAILS -------
        def  memployee(self):
           self.new_win=Toplevel(self.root)
           self.new_obj=MEMP(self.new_win)

  ##---------VIEW -------
        def  vemployee(self):
           self.new_win=Toplevel(self.root)
           self.new_obj=VEMP(self.new_win)
           

        def ani(self):
                self.im=self.Logo1
                self.Logo1=self.Logo2
                self.Logo2=self.im
                #self.Logo3=self.im
                self.phone_im.config(image=self.im)
                self.phone_im.after(1200,self.ani)
                
           
         


class   MEMP:
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1350x700+0+0")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="#B22222")
            self.root.focus_force()


        ####---------- ALL VARIABLES---
           
            self.var_user_id=StringVar()
            self.var_name=StringVar()
            self.var_doj=StringVar()
            self.var_mobileno=StringVar()
            self.var_password=StringVar()

            self.var_utype=StringVar()

            st=ttk.Style()
            st.theme_use("clam")
            
            
##-----------   USER_ID--------
            
            user_emp=Label(self.root,text="User_id",font=("times new roman" ,15, "bold"),fg="#D9DDDC",bg="#3A1F04",bd=3)
            user_emp.place(x=11,y=20,height=40,width=110)
            ##-----------   NAME--------
            name_emp=Label(self.root,text="Doj",font=("times new roman" ,15, "bold"),fg="#D9DDDC",bg="#3A1F04",bd=3)
            name_emp.place(x=611,y=20,height=40,width=110)
            ##-----------   DOJ--------
            doj_emp=Label(self.root,text="Name",font=("times new roman" ,15, "bold"),fg="#D9DDDC",bg="#3A1F04",bd=3)
            doj_emp.place(x=11,y=80,height=40,width=110)
            ##-----------   MOBILE_NO--------
            mob_emp=Label(self.root,text="Mobile no",font=("times new roman" ,15, "bold"),fg="#D9DDDC",bg="#3A1F04",bd=3)
            mob_emp.place(x=611,y=80,height=40,width=110)
            ##-----------   PASSWORD--------
            pass_emp=Label(self.root,text="Password",font=("times new roman" ,15, "bold"),fg="#D9DDDC",bg="#3A1F04",bd=3)
            pass_emp.place(x=11,y=130,height=40,width=110)
            ##-----------   USERTYPE--------
            utype_emp=Label(self.root,text="User type",font=("times new roman" ,15, "bold"),fg="#D9DDDC",bg="#3A1F04",bd=3)
            utype_emp.place(x=611,y=130,height=40,width=110)


            ###---------ENTRY -----------
            user_Eemp=Entry(self.root,textvariable=self.var_user_id,font=("times new roman" ,15),fg="black",bg="white",bd=4)
            user_Eemp.place(x=271,y=20,height=40,width=210)

            ###---------NAME -----------
            nam_Eemp=Entry(self.root,textvariable=self.var_name,font=("times new roman" ,15),fg="black",bg="white",bd=4)
            nam_Eemp.place(x=271,y=80,height=40,width=210)

            ###---------DOJ -----------
            self.doj_Eemp=Entry(self.root,textvariable=self.var_doj,font=("times new roman",2),fg="black",bg="white",bd=4)
            self.doj_Eemp.place(x=771,y=20,height=25,width=200)
            self.cal=DateEntry(self.doj_Eemp,width=200,fg="#FF2800",bg="grey",bd=3,textvariable=self.var_doj)
            self.cal.pack(fill=BOTH)
            
            

            ###---------MOBILE_NO -----------
            mob_Eemp=Entry(self.root,textvariable=self.var_mobileno,font=("times new roman" ,15),fg="black",bg="white",bd=4)
            mob_Eemp.place(x=771,y=80,height=40,width=210)


            ###---------PASSWORD -----------
            pass_Eemp=Entry(self.root,textvariable=self.var_password,font=("times new roman" ,15),fg="black",bg="white",bd=4)
            pass_Eemp.place(x=271,y=130,height=40,width=210)


            ###---------USERTYPE -----------
            utype_Eemp=Entry(self.root,textvariable=self.var_utype,font=("times new roman" ,15),fg="black",bg="white",bd=4)
            utype_Eemp.place(x=771,y=130,height=40,width=210)

            #####--------------BUTTONS--------------
            self.bns=False
            self.onimg=Image.open("images/switch on.png")
            self.onimg=self.onimg.resize((80,30),Image.ANTIALIAS)
            self.onimg=ImageTk.PhotoImage(self.onimg)
            
            self.offimg=Image.open("images/switch off.png")
            self.offimg=self.offimg.resize((80,30),Image.ANTIALIAS)
            self.offimg=ImageTk.PhotoImage(self.offimg)
            

            self.t=Label(self.root,text="Dark Mode: OFF",font=("times new roman",10,"bold"),fg="#FF2800",bg="grey")
            self.t.place(x=5,y=180,width=100,height=40)

            self.btn=Button(self.root,text="OFF",command=self.switchh,font=("times new roman",17),fg="#FF2800",bg="grey",image=self.offimg)
            self.btn.place(x=110,y=180,width=80,height=40)


            self.add_emp=Button(self.root,text="ADD",command=self.add,font=("times new roman" ,15),cursor="hand2",fg="#D9DDDC",bg="#3A1F04",bd=4)
            self.add_emp.place(x=271,y=180,height=40,width=110)

            self.delete_emp=Button(self.root,text="DELETE",command=self.delete,font=("times new roman" ,15),cursor="hand2",fg="#D9DDDC",bg="#3A1F04",bd=4)
            self.delete_emp.place(x=471,y=180,height=40,width=130)

            self.update_emp=Button(self.root,text="UPDATE",command=self.update,font=("times new roman" ,15),cursor="hand2",fg="#D9DDDC",bg="#3A1F04",bd=4)
            self.update_emp.place(x=671,y=180,height=40,width=130)


            self.clear_emp=Button(self.root,text="CLEAR",command=self.clear,font=("times new roman" ,15),cursor="hand2",fg="#D9DDDC",bg="#3A1F04",bd=4)
            self.clear_emp.place(x=871,y=180,height=40,width=130)

            self.ba_emp=Button(self.root,text="BACK",command=self.cl,font=("times new roman" ,15),cursor="hand2",fg="#D9DDDC",bg="#3A1F04",bd=4)
            self.ba_emp.place(x=1031,y=180,height=40,width=130)

            self.b_emp=Button(self.root,text="Login",font=("times new roman" ,15),command=self.log,cursor="hand2",fg="#D9DDDC",bg="#3A1F04",bd=4)
            self.b_emp.place(x=1181,y=180,height=40,width=130)


                
            
    ###############---------------------TREEVIEW-------------------
            
            view_emp=Frame(self.root,bd=3,relief=RIDGE)
            view_emp.place(x=0,y=230,relwidth=1,height=200)

            scrolly=Scrollbar(view_emp,orient=VERTICAL)
            scrollx=Scrollbar(view_emp,orient=HORIZONTAL)


            self.EmployeeTable=ttk.Treeview(view_emp,columns=("useri_id","name","doj","mobileno","password","utype"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            scrollx.pack(side=BOTTOM,fill=X)
            scrolly.pack(side=RIGHT,fill=Y)
            
            scrollx.config(command=self.EmployeeTable.xview)
            scrolly.config(command=self.EmployeeTable.yview)
            
            self.EmployeeTable.heading("useri_id",text=" USER_ID")
            self.EmployeeTable.heading("name",text=" NAME")
            self.EmployeeTable.heading("doj",text=" DOJ")
            self.EmployeeTable.heading("mobileno",text=" MOBILE NO")
            self.EmployeeTable.heading("password",text=" PASSWORD")
            self.EmployeeTable.heading("utype",text=" USER TYPE")

            self.EmployeeTable["show"]="headings"


            self.EmployeeTable.column("useri_id",width=70)
            self.EmployeeTable.column("name",width=100)
            self.EmployeeTable.column("doj",width=60)
            self.EmployeeTable.column("mobileno",width=70)
            self.EmployeeTable.column("password",width=40)
            self.EmployeeTable.column("utype",width=60)

            self.EmployeeTable.pack(fill=BOTH,expand=1)
            self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
            self.show()
            st.configure("Treeview",
                      background="grey",
                      foregroung="#622A0F",
                      rowheight=25,
                      fieldbackground="grey"
                      )
            st.map("Treeview",background=[("selected","navy")])

        
        def log(self):    
            self.new_win=Toplevel(self.root)
            self.new_obj=LOG(self.new_win)
           

            
#############--------------ADD--------------
       
        def switchh(self):
            #global bns
            #bns=False
            if self.bns:
                self.btn.config(image=self.offimg,bg="grey")
                self.root.config(bg="#B22222")
                self.t.config(text="Dark Mode: OFF",bg="grey")
                self.bns=False
            else:
                self.btn.config(image=self.onimg,bg="grey")
                self.root.config(bg="black")
                self.t.config(text="Dark Mode: ON",bg="black")
                self.bns=True
        def cl(self):
                self.root.destroy()
                
        

        def add(self):
            
            con=sqlite3.connect(database=r'coding.db')
            cur=con.cursor()
            try:
                if self.var_user_id.get()=="":
                    messagebox.showerror("Error","User_id must be required ",parent=self.root)
                else:
                    cur.execute("Select * from employee where user_id=?",(self.var_user_id.get(),))
                    row=cur.fetchone()
                    if row!=None:
                        messagebox.showerror("Error","This user_id already there ",parent=self.root)
                    else:
                        cur.execute("Insert into employee(user_id,name,doj,mobileno,password,utype) values(?,?,?,?,?,?)",(
                            self.var_user_id.get(),
                            self.var_name.get(),
                            self.var_doj.get(),
                            self.var_mobileno.get(),
                            self.var_password.get(),
                            self.var_utype.get()
                        ))
                        con.commit()
                        messagebox.showinfo("Success","Employee added successfully",parent=self.root)
                        self.show()
                        
                       
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)


        #############--------------UPDATE--------------
            
        def update(self):
            con=sqlite3.connect(database=r'coding.db')
            cur=con.cursor()
            try:
                if self.var_user_id.get()=="":
                    messagebox.showerror("Error","User_id must be required ",parent=self.root)
                else:
                    cur.execute("Select * from employee where user_id=?",(self.var_user_id.get(),))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error","INVALID  user_id  ",parent=self.root)
                    else:
                        cur.execute("Update  employee set name=?,doj=?,mobileno=?,password=?,utype=?  where user_id=?",(
                            self.var_name.get(),
                            self.var_doj.get(),
                            self.var_mobileno.get(),
                            self.var_password.get(),
                            self.var_utype.get(),
                            self.var_user_id.get()
                        ))

                        con.commit()
                        messagebox.showinfo("Success","Employee updated successfully",parent=self.root)
                        self.show()
                        
                       
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)


     #############--------------DELETE--------------
               
        def delete(self):
            con=sqlite3.connect(database=r'coding.db')
            cur=con.cursor()
            try:
                if self.var_user_id.get()=="":
                    messagebox.showerror("Error","User_id must be required ",parent=self.root)
                else:
                    cur.execute("Select * from employee where user_id=?",(self.var_user_id.get(),))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error","INVALID  user_id  ",parent=self.root)
                    else:
                        op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                        cur.execute("delete from employee where user_id=?",(self.var_user_id.get(),))
                        if op==True:
                                
                                con.commit()
                                messagebox.showinfo("Success","Employee deleted successfully",parent=self.root)
                                self.show()
                self.clear()
                                
             

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)

                
#############--------------CLEAR--------------
    
        def clear(self):
             self.var_user_id.set("")
             self.var_name.set("")
             self.var_doj.set("")
             self.var_mobileno.set("")
             self.var_password.set("")
             self.var_utype.set("")
             self.show()

        
        def  get_data(self,ev):
            f=self.EmployeeTable.focus()
            content=self.EmployeeTable.item(f)
            row=content['values']
            #print(row)
            self.var_user_id.set(row[0])
            self.var_name.set(row[1])
            self.var_doj.set(row[2])
            self.var_mobileno.set(row[3])
            self.var_password.set(row[4])
            self.var_utype.set(row[5])

            
        def grab_date(self):
                self.doj_Eemp.config(text=self.cal.get_date())

       
        def show(self):
         con=sqlite3.connect(database=r'coding.db')
         cur=con.cursor()
         try:
              global c
              c=1
              self.EmployeeTable.tag_configure('oddrow',background="#7C4700")
              self.EmployeeTable.tag_configure('evrow',background="#808588")
              cur.execute("select * from employee")
              rows=cur.fetchall()
              self.EmployeeTable.delete(*self.EmployeeTable.get_children())
              for row in rows:
                  if c % 2 == 0:
                          self.EmployeeTable.insert('',END,values=row,tags=('evrow',))
                  else:
                          self.EmployeeTable.insert('',END,values=row,tags=('oddrow',))
                  c +=1
               
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)

class VEMP:
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1350x700+0+0")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="white")
            self.root.focus_force()

            self.var_user_id=StringVar()
            self.var_name=StringVar()
            self.var_doj=StringVar()
            self.var_mobileno=StringVar()
            self.var_password=StringVar()

            self.var_utype=StringVar()

            st=ttk.Style()
            st.theme_use("clam")
            


           
            
            view_emp=Frame(self.root,bd=3,relief=RIDGE)
            view_emp.place(x=0,y=0,relwidth=1,height=400)

            scrolly=Scrollbar(view_emp,orient=VERTICAL)
            scrollx=Scrollbar(view_emp,orient=HORIZONTAL)


            self.EmployeeTable=ttk.Treeview(view_emp,columns=("useri_id","name","doj","mobileno","password","utype"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            scrollx.pack(side=BOTTOM,fill=X)
            scrolly.pack(side=RIGHT,fill=Y)
            
            scrollx.config(command=self.EmployeeTable.xview)
            scrolly.config(command=self.EmployeeTable.yview)
            
            
            
            self.EmployeeTable.heading("useri_id",text="USER_ID")
            self.EmployeeTable.heading("name",text="NAME")
            self.EmployeeTable.heading("doj",text="DOJ")
            self.EmployeeTable.heading("mobileno",text="MOBILE NO")
            self.EmployeeTable.heading("password",text="PASSWORD")
            self.EmployeeTable.heading("utype",text="USER TYPE")



            self.EmployeeTable["show"]="headings"


            self.EmployeeTable.column("useri_id",width=90)
            self.EmployeeTable.column("name",width=100)
            self.EmployeeTable.column("doj",width=100)
            self.EmployeeTable.column("mobileno",width=100)
            self.EmployeeTable.column("password",width=100)
            self.EmployeeTable.column("utype",width=100)

            self.EmployeeTable.pack(fill=BOTH,expand=1)
            self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
            self.show()
            st.configure("Treeview",
                      background="grey",
                      foregroung="#FF2800",
                      rowheight=25,
                      fieldbackground="#997950"
                      )
            st.map("Treeview",background=[("selected","navy")])
            
            

        def show(self):
            con=sqlite3.connect(database=r'coding.db')
            cur=con.cursor()
            try:
                    
              global c
              c=0
              self.EmployeeTable.tag_configure('oddrow',background="#7C4700")
              self.EmployeeTable.tag_configure('evrow',background="#808588")
              cur.execute("select * from employee")
              rows=cur.fetchall()
              self.EmployeeTable.delete(*self.EmployeeTable.get_children())
              for row in rows:
                  if c % 2 == 0:
                          self.EmployeeTable.insert('',END,values=row,tags=('oddrow',))
                  else:
                          self.EmployeeTable.insert('',END,values=row,tags=('evrow',))
                  c +=1
              
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)


        def  get_data(self,ev):
            f=self.EmployeeTable.focus()
            content=self.EmployeeTable.item(f)
            row=content['values']
            #print(row)
            self.var_user_id.set(row[0])
            self.var_name.set(row[1])
            self.var_doj.set(row[2])
            self.var_mobileno.set(row[3])
            self.var_password.set(row[4])
            self.var_utype.set(row[5])

            
class LOG:#x=0,y=230,relwidth=1,height=200)
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1350x500+0+260")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="#B22222")
            self.root.focus_force()

            scrolly=Scrollbar(self.root,orient=VERTICAL)
            scrollx=Scrollbar(self.root,orient=HORIZONTAL)


            self.EmployeTable=ttk.Treeview(self.root,columns=("id","name","time","date","tim"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            scrollx.pack(side=BOTTOM,fill=X)
            scrolly.pack(side=RIGHT,fill=Y)
            
            scrollx.config(command=self.EmployeTable.xview)
            scrolly.config(command=self.EmployeTable.yview)
            
            
            
            self.EmployeTable.heading("id",text="USER_ID")
            self.EmployeTable.heading("name",text="NAME")
            self.EmployeTable.heading("time",text="LOGIN TIME")
            self.EmployeTable.heading("date",text="DATE")
            self.EmployeTable.heading("tim",text="LOGOUT TIME")


            self.EmployeTable["show"]="headings"


            self.EmployeTable.column("id",width=50)
            self.EmployeTable.column("name",width=60)
            self.EmployeTable.column("time",width=60)
            self.EmployeTable.column("date",width=60)
            self.EmployeTable.column("tim",width=60)
           
            self.EmployeTable.pack(fill=BOTH,expand=1)
           # self.EmployeTable.bind("<ButtonRelease-1>",self.get_data)
            self.show()

        def show(self):
            con=sqlite3.connect(database=r'coding.db')
            cur=con.cursor()
            try:
                    cur.execute("select * from login")
                    rows=cur.fetchall()
                    self.EmployeTable.delete(*self.EmployeTable.get_children())
                    for row in rows:
                          self.EmployeTable.insert('',END,values=row)#,tags=('evrow',))
                  #c +=1
              
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)

        

        

if  __name__=="__main__":
     root=Tk()
     obj=EMP(root)
     root.mainloop()
