from tkinter import*
from tkinter import ttk,messagebox
import  sqlite3
class PRODUCT:
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1140x560+210+130")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="white")
            self.root.focus_force()

            #========VARIABLES======
            self.var_cat=StringVar()
            self.var_id=StringVar()
            self.var_item_no=StringVar()
            self.var_prod_no=StringVar()
            self.var_searchby=StringVar()
            self.var_searchtxt=StringVar()
            self.sup_list=[]
            self.sup_cat()
            self.var_item_name=StringVar()
            self.var_price=StringVar()
            self.var_iqty=StringVar()
            self.var_status=StringVar()

        ######## PRODUCT FRAME=============
            pr_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
            pr_frame.place(x=10,y=10,width=450,height=540)


            #+++++TITLE+++++++++++++
            titile=Label(pr_frame,text="MANAGE PRODUCT ",font=("goudy old style",15),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)


            Clbl=Label(pr_frame,text="Category",font=("goudy old style",15),bg="white").place(x=30,y=40)

            SIlbl=Label(pr_frame,text="Supplier_id",font=("goudy old style",15),bg="white").place(x=30,y=80)

            Ilbl=Label(pr_frame,text="Item_no",font=("goudy old style",15),bg="white").place(x=30,y=120)

            INlbl=Label(pr_frame,text="Item_name",font=("goudy old style",15),bg="white").place(x=30,y=160)

            plbl=Label(pr_frame,text="Price",font=("goudy old style",15),bg="white").place(x=30,y=200)

            qlbl=Label(pr_frame,text="Quantity",font=("goudy old style",15),bg="white").place(x=30,y=240)

            Slbl=Label(pr_frame,text="Status",font=("goudy old style",15),bg="white").place(x=30,y=280)



            


            #===option====

            cmb_cat=ttk.Combobox(pr_frame,textvariable=self.var_cat,values=("Select","Stationary","Cosmetics","Grocery"),state="readonly",justify=CENTER,font=("tgoudy old style",10,"bold"))
            cmb_cat.place(x=190,y=40)
            cmb_cat.current(0)


            cmb_si=ttk.Combobox(pr_frame,textvariable=self.var_id,values=self.sup_list,state="readonly",justify=CENTER,font=("tgoudy old style",10,"bold"))
            cmb_si.place(x=190,y=80)
            cmb_si.current(0)


            txt_item=Entry(pr_frame,textvariable=self.var_item_no,font=("goudy old style",15),bg="white").place(x=190,y=120)

            txt_itemname=Entry(pr_frame,textvariable=self.var_item_name,font=("goudy old style",15),bg="white").place(x=190,y=160)

            txt_price=Entry(pr_frame,textvariable=self.var_price,font=("goudy old style",15),bg="white").place(x=190,y=200)

            txt_qty=Entry(pr_frame,textvariable=self.var_iqty,font=("goudy old style",15),bg="white").place(x=190,y=240)

            cmb_st=ttk.Combobox(pr_frame,textvariable=self.var_status,values=("Active","Inactive"),state="readonly",justify=CENTER,font=("tgoudy old style",10,"bold"))
            cmb_st.place(x=190,y=280)
            cmb_st.current(0)




             #####--------------BUTTONS--------------


            add_p=Button(pr_frame,text="ADD",command=self.add,font=("times new roman" ,15),bg="#4caf50",fg="grey",bd=4)
            add_p.place(x=30,y=350,width=110)
            

            delete_p=Button(pr_frame,text="DELETE",command=self.delete,font=("times new roman" ,15),bg="#4caf50",fg="grey",bd=4)
            delete_p.place(x=200,y=350,height=40,width=130)

            update_p=Button(pr_frame,text="UPDATE",command=self.update,font=("times new roman" ,15),bg="#4caf50",fg="grey",bd=4)
            update_p.place(x=30,y=410,height=40,width=130)


            clear_p=Button(pr_frame,text="CLEAR",command=self.clear,font=("times new roman" ,15),bg="#4caf50",fg="grey",bd=4)
            clear_p.place(x=200,y=410,height=40,width=130)


            #========search frame=====
            searc=LabelFrame(self.root,text="Search Product",font=("times new roman",10,"bold"),bd=2,relief=RIDGE,bg="white")
            searc.place(x=510,y=10,width=600,height=100)
 
    
 
 
            #########SEARCH FRAME=====
            cmb_search=ttk.Combobox(searc,textvariable=self.var_searchby,values=("select","item_name","category"),state="readonly",justify=CENTER,font=("tgoudy old style",10,"bold"))
            cmb_search.place(x=10,y=10,width=200,height=30)
            cmb_search.current(0)
            
            txtsearch=Entry(searc,textvariable=self.var_searchtxt,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=230,y=10,width=180)
            btsearch=Button(searc,text="search",command=self.search,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=440,y=10,height=30,width=120)
            showall=Button(searc,text="Show All",command=self.show_all,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=230,y=45,height=30,width=120)
            

            
            


             ###############---------------------TREEVIEW-------------------
           
            view_p=Frame(self.root,bd=3,relief=RIDGE)
            view_p.place(x=510,y=140,width=600,height=400)
            

            scrolly=Scrollbar(view_p,orient=VERTICAL)
            scrollx=Scrollbar(view_p,orient=HORIZONTAL)


            self.ProductTable=ttk.Treeview(view_p,columns=("prod_no","category","id","item_no","item_name","price","iqty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            scrollx.pack(side=BOTTOM,fill=X)
            scrolly.pack(side=RIGHT,fill=Y)
            
            scrollx.config(command=self.ProductTable.xview)
            scrolly.config(command=self.ProductTable.yview)
            
            
            
            self.ProductTable.heading("prod_no",text="PROD_NO")
            self.ProductTable.heading("category",text="category")
            self.ProductTable.heading("id",text="id")
            self.ProductTable.heading("item_no",text="item_no ")
            self.ProductTable.heading("item_name",text="item_name")
            self.ProductTable.heading("price",text="price")
            self.ProductTable.heading("iqty",text="iqty")
            self.ProductTable.heading("status",text="status")



            self.ProductTable["show"]="headings"


            self.ProductTable.column("prod_no",width=90)
            self.ProductTable.column("category",width=100)
            self.ProductTable.column("id",width=100)
            self.ProductTable.column("item_no",width=100)
            self.ProductTable.column("item_name",width=100)
            self.ProductTable.column("price",width=100)
            self.ProductTable.column("iqty",width=100)
            self.ProductTable.column("status",width=100)

            self.ProductTable.pack(fill=BOTH,expand=1)
            self.ProductTable.bind("<ButtonRelease-1>",self.get_data)
            self.show()
            


            #############--------------ADD--------------
        

        def  sup_cat(self):
                self.sup_list.append("Empty")
                con=sqlite3.connect(database=r'ims.db')
                cur=con.cursor()
                try:
                        cur.execute("select  id from supplier")
                        cat=cur.fetchall()
                        if len(cat)>0:
                                del self.sup_list[:]
                                self.sup_list.append("select")
                                for i in cat:
                                        self.sup_list.append(i[0])
                        
                        
                except Exception as ex:
                    messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)
        
                       
        def  add(self):
                
                con=sqlite3.connect(database=r'ims.db')
                cur=con.cursor()
                try:
                    
                    if self.var_cat.get()=="select" or self.var_item_name.get()=="":
                        messagebox.showerror("Error","Category must be required ",parent=self.root)
                    else:
                            cur.execute("Insert into product(category,id,item_no,item_name,price,iqty,status) values(?,?,?,?,?,?,?)",(
                                    self.var_cat.get(),
                                    self.var_id.get(),
                                    self.var_item_no.get(),
                                    self.var_item_name.get(),
                                    self.var_price.get(),
                                    self.var_iqty.get(),
                                    self.var_status.get()
                          ))
                
                            '''
                        cur.execute("Select * from productt where  item_no=?",(self.var_item_no.get(),))
                        row=cur.fetchone()
                        
                    if row!=None:
                        messagebox.showerror("Error","This product already there ",parent=self.root)
                    else:'''
                            
                
                                    
                            
                            con.commit()
                            messagebox.showinfo("Success","product added successfully",parent=self.root)
                            self.show()
                            

                       
                except Exception as ex:
                    messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)



#############--------------UPDATE--------------

        def update(self):
                 con=sqlite3.connect(database=r'ims.db')
                 cur=con.cursor()
                 try:
                    if self.var_prod_no.get()=="":
                        messagebox.showerror("Error","Please select Product number",parent=self.root)
                    else:
                        cur.execute("Select * from productt where prod_no=?",(self.var_prod_no.get(),))
                        row=cur.fetchone()
                        if row==None:
                            messagebox.showerror("Error","INVALID  data  ",parent=self.root)
                        else:
                            cur.execute("Update  productt set category=?,id=?,item_no=?,item_name=?,price=?,iqty=?,status=?  where  prod_no=?",(
                                self.var_cat.get(),
                                self.var_id.get(),
                                self.var_item_no.get(),
                                self.var_item_name.get(),
                                self.var_price.get(),
                                self.var_iqty.get(),
                                self.var_status.get(),
                                self.var_prod_no.get()
                            ))

                            con.commit()
                            messagebox.showinfo("Success","product updated successfully",parent=self.root)
                            self.show()
                        
                 except Exception as ex:
                        messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)


#############--------------DELETE--------------
        def delete(self):
                con=sqlite3.connect(database=r'ims.db')
                cur=con.cursor()
                try:
                    if self.var_item_no.get()=="":
                        messagebox.showerror("Error","Item number  must be required ",parent=self.root)
                    else:
                        cur.execute("Select * from productt where item_no=?",(self.var_item_no.get(),))
                        row=cur.fetchone()
                        if row==None:
                            messagebox.showerror("Error","INVALID  user_id  ",parent=self.root)
                        else:
                            op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                            cur.execute("delete from productt where item_no=?",(self.var_item_no.get(),))
                            if op==True:
                                con.commit()
                                messagebox.showinfo("Success","product deleted successfully",parent=self.root)
                                self.show()
                                
             

                except Exception as ex:
                    messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)

        
#############--------------CLEAR--------------

        def clear(self):
                self.var_cat.set("select")
                self.var_id.set("select")
                self.var_item_no.set("")
                self.var_item_name.set("")
                self.var_price.set("")
                self.var_iqty.set("")
                self.var_status.set("select")
                self.var_searchby.set("select")
                self.var_searchtxt.set('')
                self.show()
        def show_all(self):
                self.show()



        def  get_data(self,ev):
                f=self.ProductTable.focus()
                content=self.ProductTable.item(f)
                row=content['values']
                #print(row)
                self.var_prod_no.set(row[0])
                self.var_cat.set(row[1])
                self.var_id.set(row[2])
                self.var_item_no.set(row[3])
                self.var_item_name.set(row[4])
                self.var_price.set(row[5])
                self.var_iqty.set(row[6])
                self.var_status.set(row[7])


        def show(self):
                 con=sqlite3.connect(database=r'ims.db')
                 cur=con.cursor()
                 try:
                      cur.execute("select * from productt")
                      rows=cur.fetchall()
                      self.ProductTable.delete(*self.ProductTable.get_children())
                      for row in rows:
                          self.ProductTable.insert('',END,values=row)

                 except Exception as ex:
                     messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)



        def search(self):
                con=sqlite3.connect(database=r'ims.db')
                cur=con.cursor()
                try:
                        if self.var_searchby.get()=="select":
                                 messagebox.showerror("Error","select the option  ",parent=self.root)
                        elif   self.var_searchtxt.get()=="":
                                messagebox.showerror("Error","search input should be required ",parent=self.root)
                        else:
                                 cur.execute("Select * from productt where  "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+ "%' ")
                                 ro=cur.fetchall()
                                 if len(ro)!=0:
                                        self.ProductTable.delete(*self.ProductTable.get_children())
                                        for row in ro:
                                                self.ProductTable.insert('',END,values=row)
                                 else:
                                        messagebox.showerror("Error","No record found",parent=self.root)

                except Exception as ex:
                     messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root) 
                







if  __name__=="__main__":
     root=Tk()
     obj=PRODUCT(root)
     root.mainloop()
