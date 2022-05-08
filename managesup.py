from tkinter import*
from tkinter import ttk,messagebox
import  sqlite3
class MSUP:
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1140x400+214+298")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="white")
            self.root.focus_force()


        ####---------- ALL VARIABLES---

            self.var_id=StringVar()
            self.var_name=StringVar()
            self.var_mobile_no=StringVar()
            
            
    ##--------sup ENTERIES-----------
##-----------   id--------
            user_sup=Label(self.root,text="Id",font=("times new roman" ,15, "bold"),fg="orange",bd=3)
            user_sup.place(x=11,y=20,height=40,width=110)
            ##-----------   NAME--------
            name_sup=Label(self.root,text="Name",font=("times new roman" ,15, "bold"),fg="orange",bd=3)
            name_sup.place(x=611,y=20,height=40,width=110)
    ##-----------   MOBILE_NO--------
            mob_sup=Label(self.root,text="Mobile no",font=("times new roman" ,15, "bold"),fg="orange",bd=3)
            mob_sup.place(x=611,y=80,height=40,width=110)
         
   ###---------ENTRY -----------
            user_ssup=Entry(self.root,textvariable=self.var_id,font=("times new roman" ,15),bg="white",bd=4)
            user_ssup.place(x=271,y=20,height=40,width=210)

            ###---------NAME -----------
            nam_ssup=Entry(self.root,textvariable=self.var_name,font=("times new roman" ,15),bg="white",bd=4)
            nam_ssup.place(x=771,y=20,height=40,width=210)

      
            ###---------MOBILE_NO -----------
            mob_Esup=Entry(self.root,textvariable=self.var_mobile_no,font=("times new roman" ,15),bg="white",bd=4)
            mob_Esup.place(x=771,y=80,height=40,width=210)


         


            #####--------------BUTTONS--------------


            add_sup=Button(self.root,text="ADD",command=self.add,font=("times new roman" ,15),bg="#4caf50",fg="grey",bd=4)
            add_sup.place(x=271,y=180,height=40,width=110)

            delete_sup=Button(self.root,text="DELETE",command=self.delete,font=("times new roman" ,15),bg="#4caf50",fg="grey",bd=4)
            delete_sup.place(x=471,y=180,height=40,width=130)

            update_sup=Button(self.root,text="UPDATE",command=self.update,font=("times new roman" ,15),bg="#4caf50",fg="grey",bd=4)
            update_sup.place(x=671,y=180,height=40,width=130)


            clear_sup=Button(self.root,text="CLEAR",command=self.clear,font=("times new roman" ,15),bg="#4caf50",fg="grey",bd=4)
            clear_sup.place(x=871,y=180,height=40,width=130)


            
    ###############---------------------TREEVIEW-------------------
           
            view_sup=Frame(self.root,bd=3,relief=RIDGE)
            view_sup.place(x=0,y=230,relwidth=1,height=200)

            scrolly=Scrollbar(view_sup,orient=VERTICAL)
            scrollx=Scrollbar(view_sup,orient=HORIZONTAL)


            self.supplierTable=ttk.Treeview(view_sup,columns=("id","name","mobile_no"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            scrollx.pack(side=BOTTOM,fill=X)
            scrolly.pack(side=RIGHT,fill=Y)
            
            scrollx.config(command=self.supplierTable.xview)
            scrolly.config(command=self.supplierTable.yview)
            
            
            
            self.supplierTable.heading("id",text="ID")
            self.supplierTable.heading("name",text="NAME")
            
            self.supplierTable.heading("mobile_no",text="MOBILE NO")
            



            self.supplierTable["show"]="headings"


            self.supplierTable.column("id",width=90)
            self.supplierTable.column("name",width=100)
            
            self.supplierTable.column("mobile_no",width=100)
            

            self.supplierTable.pack(fill=BOTH,expand=1)
            self.supplierTable.bind("<ButtonRelease-1>",self.get_data)
            self.show()

            
            

#############--------------ADD--------------
            

        def add(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                if self.var_id.get()=="":
                    messagebox.showerror("Error","id must be required ",parent=self.root)
                else:
                    cur.execute("Select * from supplier where id=?",(self.var_id.get(),))
                    row=cur.fetchone()
                    if row!=None:
                        messagebox.showerror("Error","This id already there ",parent=self.root)
                    else:
                        cur.execute("Insert into supplier(id,name,mobile_no) values(?,?,?)",(
                            self.var_id.get(),
                            self.var_name.get(),
                            
                            self.var_mobile_no.get(),
                            
                        ))

                        con.commit()
                        messagebox.showinfo("Success","supplier added successfully",parent=self.root)
                        self.show()
                        
                       
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)



        #############--------------UPDATE--------------
            

        def update(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                if self.var_id.get()=="":
                    messagebox.showerror("Error","id must be required ",parent=self.root)
                else:
                    cur.execute("Select * from supplier where id=?",(self.var_id.get(),))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error","INVALID  id  ",parent=self.root)
                    else:
                        cur.execute("Update  supplier set name=?,mobile_no=?  where id=?",(
                            self.var_name.get(),
                            
                            self.var_mobile_no.get(),
                            
                            self.var_id.get()
                        ))

                        con.commit()
                        messagebox.showinfo("Success","supplier updated successfully",parent=self.root)
                        self.show()
                        
                       
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)


     #############--------------DELETE--------------
               
        def delete(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                if self.var_id.get()=="":
                    messagebox.showerror("Error","id must be required ",parent=self.root)
                else:
                    cur.execute("Select * from supplier where id=?",(self.var_id.get(),))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error","INVALID  id  ",parent=self.root)
                    else:
                        op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                        cur.execute("delete from supplier where id=?",(self.var_id.get(),))
                        if op==True:
                                
                                con.commit()
                                messagebox.showinfo("Success","supplier deleted successfully",parent=self.root)
                                self.show()
                                
             

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)

                
#############--------------CLEAR--------------
    
        def clear(self):
             self.var_id.set("")
             self.var_name.set("")
           
             self.var_mobile_no.set("")
             
             self.show()

            

        def  get_data(self,ev):
            f=self.supplierTable.focus()
            content=self.supplierTable.item(f)
            row=content['values']
            #print(row)
            self.var_id.set(row[0])
            self.var_name.set(row[1])
            
            self.var_mobile_no.set(row[2])
            

       
        def show(self):
         con=sqlite3.connect(database=r'ims.db')
         cur=con.cursor()
         try:
              cur.execute("select * from supplier")
              rows=cur.fetchall()
              self.supplierTable.delete(*self.supplierTable.get_children())
              for row in rows:
                  self.supplierTable.insert('',END,values=row)
               
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)
             
               
                   
          
         
        
             
             
                          
              
              



    




     
     
         
           
        
      #      try:
          
             
          #      print("tete")
         
            
          #          
             #       
                    
                   
                
                            
                        
                        
                         
          #  
          #      
                
                         
                  
                            
                       
                                    
                                


      



if  __name__=="__main__":
     root=Tk()
     obj=MSUP(root)
     root.mainloop()
