from tkinter import*
from tkinter import ttk
#from managesup import MSUP
#from supview import VSUP
import sqlite3
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import time
class SUP:
        def    __init__(self,master):
            self.master=master
            self.master.geometry("1350x710+0+0")
            self.master.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.master.config(bg="#4B5320")
            self.master.focus_force()
            self.my_canvas=Canvas(self.master,width=1350,height=80,bd=1)
            self.Lo=Image.open("images/bgg1.jpeg")
            self.Lo=self.Lo.resize((650,40),Image.ANTIALIAS)
            self.Lo=ImageTk.PhotoImage(self.Lo)
            self.my_canvas.create_image(650,40,image=self.Lo)
                
            self.my_canvas.place(x=0,y=0)
            self.my_canvas.configure(bg="black")
            self.my_canvas.create_text(650,40,text="SUPPLIER DETAILS",font=("times new roman",30,"bold"),fill="PINK")

            self.Lo=Image.open("images/bgg2.jpeg")
            self.Lo=self.Lo.resize((1340,710),Image.ANTIALIAS)
            self.Lo=ImageTk.PhotoImage(self.Lo)
            self.phone_im=Label(self.master,bd=3)#image=self.Lo)
            self.phone_im.place(x=0,y=90,width=1350,height=610)
            self.Logo1=Image.open("images/s1.jpg")
            self.Logo1=self.Logo1.resize((1340,610),Image.ANTIALIAS)
            self.Logo1=ImageTk.PhotoImage(self.Logo1)
            
            self.Logo2=Image.open("images/s2.jpg")
            self.Logo2=self.Logo2.resize((1340,710),Image.ANTIALIAS)
            self.Logo2=ImageTk.PhotoImage(self.Logo2)
            
#-----------------------TITLE---------------------------------------------
            #sup_title=Label(self.master,text="SUPPLIER INFORMATION",font=("times new roman",40,"bold"),fg="green",bd=4,relief=RIDGE,padx=20).place(x=0,y=0,relwidth=1,height=60)

   #  button MANAGE AND VIEW
            btn_manage=Button(self.master,text="MANAGE SUPPLIER",command=self.msupplier,font=("times new roman",15,"italic"),bg="black",fg="orange",cursor="hand2",bd=6).place(x=340,y=70,height=60,width=210)


            btn_view=Button(self.master,text="VIEW",command=self.vsupplier,font=("times new roman",13,"italic"),bg="black",fg="orange",cursor="hand2",bd=6).place(x=640,y=70,height=60,width=210)

            self.ani()

            '''leftmenu=Frame(self.master,bd=0,relief=RIDGE,bg="black")
            leftmenu.place(x=200,y=150,width=600,height=400)

            self.MenuLogo=Image.open("images/cat.jpg")
            self.MenuLogo=self.MenuLogo.resize((580,380),Image.ANTIALIAS)
            self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

            LeftMenuLogo=Label(leftmenu,image=self.MenuLogo,bg="black",bd=2)
            LeftMenuLogo.pack(side=TOP,fill=BOTH)'''

##----------MANAGE EMP DETAILS -------
        def  msupplier(self):
           self.new_win=Toplevel(self.master)
           self.new_obj=MSUP(self.new_win)

  ##---------VIEWW -------
        def  vsupplier(self):
           self.new_win=Toplevel(self.master)
           self.new_obj=VSUP(self.new_win)
        def ani(self):
                self.im=self.Logo1
                self.Logo1=self.Logo2
                self.Logo2=self.im
                #self.Logo3=self.im
                self.phone_im.config(image=self.im)
                self.phone_im.after(1200,self.ani)
        
           
           
         
        
class VSUP:
        def    __init__(self,master):
            self.master=master
            self.master.geometry("1350x710+0+0")
            self.master.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.master.config(bg="white")
            self.master.focus_force()

            self.var_id=StringVar()
            self.var_name=StringVar()
            
            self.var_mobileno=StringVar()
            
            st=ttk.Style()
            st.theme_use("clam")
           
            
            view_sup=Frame(self.master,bd=3,relief=RIDGE)
            view_sup.place(x=0,y=0,relwidth=1,height=400)

            scrolly=Scrollbar(view_sup,orient=VERTICAL)
            scrollx=Scrollbar(view_sup,orient=HORIZONTAL)


            self.SupplierTable=ttk.Treeview(view_sup,columns=("id","item_no","item_name","price","iqty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            scrollx.pack(side=BOTTOM,fill=X)
            scrolly.pack(side=RIGHT,fill=Y)
            
            scrollx.config(command=self.SupplierTable.xview)
            scrolly.config(command=self.SupplierTable.yview)
            
            
            
            self.SupplierTable.heading("id",text="id")
            self.SupplierTable.heading("item_no",text="item_no ")
            self.SupplierTable.heading("item_name",text="item_name")
            self.SupplierTable.heading("price",text="price")
            self.SupplierTable.heading("iqty",text="iqty")

            self.SupplierTable["show"]="headings"


            self.SupplierTable.column("id",width=100)
            self.SupplierTable.column("item_no",width=100)
            self.SupplierTable.column("item_name",width=100)
            self.SupplierTable.column("price",width=100)
            self.SupplierTable.column("iqty",width=100)
            

            self.SupplierTable.pack(fill=BOTH,expand=1)
            #self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)
            self.show()
            st.configure("Treeview",
                      background="grey",
                      foregroung="#FF2800",
                      rowheight=25,
                      fieldbackground="black"
                      )
            st.map("Treeview",background=[("selected","navy")])
            

        def show(self):
            con=sqlite3.connect(database=r'coding.db')
            cur=con.cursor()
            try:
                global c
                c=1
                cur.execute("select id,item_no,item_name,price,iqty from productt")
                rows=cur.fetchall()
                self.SupplierTable.delete(*self.SupplierTable.get_children())
                self.SupplierTable.tag_configure('oddrow',background="pink")
                self.SupplierTable.tag_configure('evrow',background="brown")
                for row in rows:
                     if c % 2 == 0:
                             self.SupplierTable.insert('',END,values=row,tag=('evrow',))
                     else:
                             self.SupplierTable.insert('',END,values=row,tag=('oddrow',))
                     c +=1
                    

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.master)


            
class MSUP:
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1350x710+0+0")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="#4B3619")
            self.root.focus_force()
            
            st=ttk.Style()
            st.theme_use("clam")


        ####---------- ALL VARIABLES---

            self.var_id=StringVar()
            self.var_name=StringVar()
            self.var_mobile_no=StringVar()
            
            
    ##--------sup ENTERIES-----------
##-----------   id--------
            user_sup=Label(self.root,text="Id",font=("times new roman" ,15, "bold"),bg="#4B5320",fg="#FDA50F",bd=3)
            user_sup.place(x=11,y=20,height=40,width=110)
            ##-----------   NAME--------
            name_sup=Label(self.root,text="Name",font=("times new roman" ,15, "bold"),bg="#4B5320",fg="#FDA50F",bd=3)
            name_sup.place(x=611,y=20,height=40,width=110)
    ##-----------   MOBILE_NO--------
            mob_sup=Label(self.root,text="Mobile no",font=("times new roman" ,15, "bold"),bg="#4B5320",fg="#FDA50F",bd=3)
            mob_sup.place(x=11,y=80,height=40,width=110)
         
   ###---------ENTRY -----------
            user_ssup=Entry(self.root,textvariable=self.var_id,font=("times new roman" ,15),bg="#4B5320",fg="#FDA50F",bd=4)
            user_ssup.place(x=271,y=20,height=40,width=210)

            ###---------NAME -----------
            nam_ssup=Entry(self.root,textvariable=self.var_name,font=("times new roman" ,15),bg="#4B5320",fg="#FDA50F",bd=4)
            nam_ssup.place(x=771,y=20,height=40,width=210)

      
            ###---------MOBILE_NO -----------
            mob_Esup=Entry(self.root,textvariable=self.var_mobile_no,font=("times new roman" ,15),bg="#4B5320",fg="#FDA50F",bd=4)
            mob_Esup.place(x=271,y=80,height=40,width=210)


            #####--------------BUTTONS--------------
            self.bns=False
            self.onimg=Image.open("images/switch on.png")
            self.onimg=self.onimg.resize((80,30),Image.ANTIALIAS)
            self.onimg=ImageTk.PhotoImage(self.onimg)
            
            self.offimg=Image.open("images/switch off.png")
            self.offimg=self.offimg.resize((80,30),Image.ANTIALIAS)
            self.offimg=ImageTk.PhotoImage(self.offimg)
            

            self.t=Label(self.root,text="Dark Mode: OFF",font=("times new roman",10,"bold"),fg="#FF2800",bg="#4B3619")
            self.t.place(x=5,y=180,width=100,height=40)

            self.btn=Button(self.root,text="OFF",command=self.switchh,font=("times new roman",17),fg="#FF2800",bg="white",image=self.offimg)
            self.btn.place(x=110,y=180,width=80,height=40)



            self.add_sup=Button(self.root,text="ADD",command=self.add,font=("times new roman" ,15),cursor="hand2",bg="#4B5320",fg="#FDA50F",bd=4)
            self.add_sup.place(x=271,y=180,height=40,width=110)

            delete_sup=Button(self.root,text="DELETE",command=self.delete,font=("times new roman" ,15),cursor="hand2",bg="#4B5320",fg="#FDA50F",bd=4)
            delete_sup.place(x=471,y=180,height=40,width=130)

            update_sup=Button(self.root,text="UPDATE",command=self.update,font=("times new roman" ,15),cursor="hand2",bg="#4B5320",fg="#FDA50F",bd=4)
            update_sup.place(x=671,y=180,height=40,width=130)


            clear_sup=Button(self.root,text="CLEAR",command=self.clear,font=("times new roman" ,15),cursor="hand2",bg="#4B5320",fg="#FDA50F",bd=4)
            clear_sup.place(x=871,y=180,height=40,width=130)

            self.clear_sup=Button(self.root,text="BACK",command=self.cl,font=("times new roman" ,15),cursor="hand2",bg="#4B5320",fg="#FDA50F",bd=4)
            self.clear_sup.place(x=1071,y=180,height=40,width=130)

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
            st.configure("Treeview",
                      background="grey",
                      foregroung="#FF2800",
                      rowheight=25,
                      fieldbackground="black"
                      )
            st.map("Treeview",background=[("selected","navy")])
            
            
            

#############--------------ADD--------------
        def switchh(self):
            #global bns
            #bns=False
            if self.bns:
                self.btn.config(image=self.offimg,bg="white")
                self.root.config(bg="#4B3619")
                self.t.config(text="Dark Mode: OFF",bg="#4B3619")
                self.bns=False
            else:
                self.btn.config(image=self.onimg,bg="white")
                self.root.config(bg="black")
                self.t.config(text="Dark Mode: ON",bg="black")
                self.bns=True

        def cl(self):
                self.root.destroy()
                
        
         
        def add(self):
            
            con=sqlite3.connect(database=r'coding.db')
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
            con=sqlite3.connect(database=r'coding.db')
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
            con=sqlite3.connect(database=r'coding.db')
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
                                self.clear()
             

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
         con=sqlite3.connect(database=r'coding.db')
         cur=con.cursor()
         try:
             global c
             c=1
             cur.execute("select * from supplier")
             rows=cur.fetchall()
             self.supplierTable.delete(*self.supplierTable.get_children())
             self.supplierTable.tag_configure('oddrow',background="pink")
             self.supplierTable.tag_configure('evrow',background="brown")
             for row in rows:
                 if c % 2 == 0: 
                         self.supplierTable.insert('',END,values=row,tag=('evrow',))
                 else:
                         self.supplierTable.insert('',END,values=row,tag=('oddrow',))
                 c +=1
         except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)
             

            
if  __name__=="__main__":
     root=Tk()
     obj=SUP(root)
     root.mainloop()
