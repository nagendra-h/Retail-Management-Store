from tkinter import*
from tkinter import ttk,messagebox
import  sqlite3
from tkcalendar import  Calendar,DateEntry
class MEMP:
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1140x400+214+298")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="white")
            self.root.focus_force()


        ####---------- ALL VARIABLES---
           
            self.var_user_id=StringVar()
            self.var_name=StringVar()
            self.var_doj=StringVar()
            self.var_mobileno=StringVar()
            self.var_password=StringVar()

            self.var_utype=StringVar()
            
    ##--------EMP ENTERIES-----------
##-----------   USER_ID--------
            user_emp=Label(self.root,text="User_id",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
            user_emp.place(x=11,y=20,height=40,width=110)
            ##-----------   NAME--------
            name_emp=Label(self.root,text="Doj",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
            name_emp.place(x=611,y=20,height=40,width=110)
            ##-----------   DOJ--------
            doj_emp=Label(self.root,text="Name",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
            doj_emp.place(x=11,y=80,height=40,width=110)
            ##-----------   MOBILE_NO--------
            mob_emp=Label(self.root,text="Mobile no",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
            mob_emp.place(x=611,y=80,height=40,width=110)
            ##-----------   PASSWORD--------
            pass_emp=Label(self.root,text="Password",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
            pass_emp.place(x=11,y=130,height=40,width=110)
            ##-----------   USERTYPE--------
            utype_emp=Label(self.root,text="User type",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
            utype_emp.place(x=611,y=130,height=40,width=110)


            ###---------ENTRY -----------
            user_Eemp=Entry(self.root,textvariable=self.var_user_id,font=("times new roman" ,15),bg="white",bd=4)
            user_Eemp.place(x=271,y=20,height=40,width=210)

            ###---------NAME -----------
            nam_Eemp=Entry(self.root,textvariable=self.var_name,font=("times new roman" ,15),bg="white",bd=4)
            nam_Eemp.place(x=271,y=80,height=40,width=210)

            ###---------DOJ -----------
            self.doj_Eemp=Entry(self.root,textvariable=self.var_doj,font=("times new roman",2),bg="white",bd=4)
            self.doj_Eemp.place(x=771,y=20,height=25,width=200)
            self.cal=DateEntry(self.doj_Eemp,width=16,bg="red",fg="black",bd=3,textvariable=self.var_doj)
            self.cal.pack(fill=BOTH)
            

            
        
        

            

            ###---------MOBILE_NO -----------
            mob_Eemp=Entry(self.root,textvariable=self.var_mobileno,font=("times new roman" ,15),bg="white",bd=4)
            mob_Eemp.place(x=771,y=80,height=40,width=210)


            ###---------PASSWORD -----------
            pass_Eemp=Entry(self.root,textvariable=self.var_password,font=("times new roman" ,15),bg="white",bd=4)
            pass_Eemp.place(x=271,y=130,height=40,width=210)


            ###---------USERTYPE -----------
            utype_Eemp=Entry(self.root,textvariable=self.var_utype,font=("times new roman" ,15),bg="white",bd=4)
            utype_Eemp.place(x=771,y=130,height=40,width=210)



            #####--------------BUTTONS--------------


            add_emp=Button(self.root,text="ADD",command=self.add,font=("times new roman" ,15),bg="#4caf50",fg="grey",bd=4)
            add_emp.place(x=271,y=180,height=40,width=110)

            delete_emp=Button(self.root,text="DELETE",command=self.delete,font=("times new roman" ,15),bg="#4caf50",fg="grey",bd=4)
            delete_emp.place(x=471,y=180,height=40,width=130)

            update_emp=Button(self.root,text="UPDATE",command=self.update,font=("times new roman" ,15),bg="#4caf50",fg="grey",bd=4)
            update_emp.place(x=671,y=180,height=40,width=130)


            clear_emp=Button(self.root,text="CLEAR",command=self.clear,font=("times new roman" ,15),bg="#4caf50",fg="grey",bd=4)
            clear_emp.place(x=871,y=180,height=40,width=130)


           
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

            
            

#############--------------ADD--------------
            

        def add(self):
            con=sqlite3.connect(database=r'ims.db')
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
            con=sqlite3.connect(database=r'ims.db')
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
            con=sqlite3.connect(database=r'ims.db')
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
         con=sqlite3.connect(database=r'ims.db')
         cur=con.cursor()
         try:
              cur.execute("select * from employee")
              rows=cur.fetchall()
              self.EmployeeTable.delete(*self.EmployeeTable.get_children())
              for row in rows:
                  self.EmployeeTable.insert('',END,values=row)
               
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)



             
               
                   
        


    



       


      



if  __name__=="__main__":
     root=Tk()
     obj=MEMP(root)
     root.mainloop()
