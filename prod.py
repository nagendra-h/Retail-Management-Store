from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import  sqlite3


class PROD:
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1350x710+0+0")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="black")
            self.root.focus_force()
            self.my_canvas=Canvas(self.root,width=1350,height=80,bd=1)
            self.Lo=Image.open("images/bgg1.jpeg")
            self.Lo=self.Lo.resize((650,40),Image.ANTIALIAS)
            self.Lo=ImageTk.PhotoImage(self.Lo)
            self.my_canvas.create_image(650,40,image=self.Lo)
                
            self.my_canvas.place(x=0,y=0)
            self.my_canvas.configure(bg="grey")
            self.my_canvas.create_text(650,40,text="PRODUCT DETAILS",font=("times new roman",30,"bold"),fill="PINK")

            self.Lo=Image.open("images/bgg2.jpeg")
            self.Lo=self.Lo.resize((1340,710),Image.ANTIALIAS)
            self.Lo=ImageTk.PhotoImage(self.Lo)
            self.phone_im=Label(self.root,bd=3)#image=self.Lo)
            self.phone_im.place(x=0,y=90,width=1350,height=610)
            self.Logo1=Image.open("images/p1.jpg")
            self.Logo1=self.Logo1.resize((1340,610),Image.ANTIALIAS)
            self.Logo1=ImageTk.PhotoImage(self.Logo1)
            
            self.Logo2=Image.open("images/p2.jpg")
            self.Logo2=self.Logo2.resize((1340,710),Image.ANTIALIAS)
            self.Logo2=ImageTk.PhotoImage(self.Logo2)
            

#-----------------------TITLE---------------------------------------------
            #emp_title=Label(self.root,text="EMPLOYEE DETAILS",font=("times new roman",40,"bold"),fg="#FF2800",bg="#4B3619",bd=4,relief=RIDGE,padx=20).place(x=0,y=0,relwidth=1,height=60)

   #  button MANAGE AND VIEW
            btn_manage=Button(self.root,text="MANAGE PRODUCTS",command=self.mproduct,font=("times new roman",15,"italic"),fg="#FF2800",bg="black",cursor="hand2",bd=5)
            btn_manage.place(x=340,y=70,height=60,width=210)


            btn_view=Button(self.root,text="view",command=self.vproduct,font=("times new roman",17,"italic"),fg="#FF2800",bg="black",cursor="hand2",bd=5)
            btn_view.place(x=640,y=70,height=60,width=210)
            self.ani()

           # leftmenu=Frame(self.root,bd=0,relief=RIDGE,bg="#4B3619")
           # leftmenu.place(x=200,y=150,width=600,height=400)

            '''self.MenuLogo=Image.open("images/cat.jpg")
            self.MenuLogo=self.MenuLogo.resize((580,380),Image.ANTIALIAS)
            self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

            LeftMenuLogo=Label(leftmenu,image=self.MenuLogo,bg="#4B3619")
            LeftMenuLogo.pack(side=TOP,fill=BOTH)'''




##----------MANAGE EMP DETAILS -------
        def  mproduct(self):
           self.new_win=Toplevel(self.root)
           self.new_obj=PRODUCT(self.new_win)

  ##---------VIEWW -------
        def  vproduct(self):
           self.new_win=Toplevel(self.root)
           self.new_obj=VPRO(self.new_win)

        def ani(self):
                self.im=self.Logo1
                self.Logo1=self.Logo2
                self.Logo2=self.im
                #self.Logo3=self.im
                self.phone_im.config(image=self.im)
                self.phone_im.after(1200,self.ani)
                
         

class PRODUCT:
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1350x710+0+0")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="#4D561D")
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
            self.prod={}

            st=ttk.Style()
            st.theme_use("clam")
            

        ######## productttt FRAME=============
            pr_frame=Frame(self.root,bd=2,relief=RIDGE,bg="#48494B")
            pr_frame.place(x=10,y=10,width=650,height=640)


            #+++++TITLE+++++++++++++
            titile=Label(pr_frame,text="PRODUCT DETALS",font=("goudy old style",15,"italic"),bg="#48494B",fg="#FE5BAC").pack(side=TOP,fill=X)


            Clbl=Label(pr_frame,text="Category",font=("goudy old style",15),bg="#48494B",fg="#FE5BAC").place(x=30,y=40)

            SIlbl=Label(pr_frame,text="Supplier_id",font=("goudy old style",15),bg="#48494B",fg="#FE5BAC").place(x=30,y=80)

            Ilbl=Label(pr_frame,text="Item_no",font=("goudy old style",15),bg="#48494B",fg="#FE5BAC").place(x=30,y=120)

            INlbl=Label(pr_frame,text="Item_name",font=("goudy old style",15),bg="#48494B",fg="#FE5BAC").place(x=30,y=160)

            plbl=Label(pr_frame,text="Price",font=("goudy old style",15),bg="#48494B",fg="#FE5BAC").place(x=30,y=200)

            qlbl=Label(pr_frame,text="Quantity",font=("goudy old style",15),bg="#48494B",fg="#FE5BAC").place(x=30,y=240)

            Slbl=Label(pr_frame,text="Status",font=("goudy old style",15),bg="#48494B",fg="#FE5BAC").place(x=30,y=280)



            #===option====

            self.cmb_cat=ttk.Combobox(pr_frame,textvariable=self.var_cat,values=("Select","Stationary","Cosmetics","Grocery","Sports","Clothes","Gadjets"),state="readonly",justify=CENTER,font=("tgoudy old style",10,"bold"))
            self.cmb_cat.place(x=190,y=40)
            self.cmb_cat.current(0)


            cmb_si=ttk.Combobox(pr_frame,textvariable=self.var_id,values=self.sup_list,state="readonly",justify=CENTER,font=("tgoudy old style",10,"bold"))
            cmb_si.place(x=190,y=80)
            cmb_si.current(0)


            txt_item=Entry(pr_frame,textvariable=self.var_item_no,font=("goudy old style",15),bg="#48494B",fg="#FE5BAC").place(x=190,y=120)

            txt_itemname=Entry(pr_frame,textvariable=self.var_item_name,font=("goudy old style",15),bg="#48494B",fg="#FE5BAC").place(x=190,y=160)

            txt_price=Entry(pr_frame,textvariable=self.var_price,font=("goudy old style",15),bg="#48494B",fg="#FE5BAC").place(x=190,y=200)

            txt_qty=Entry(pr_frame,textvariable=self.var_iqty,font=("goudy old style",15),bg="#48494B",fg="#FE5BAC").place(x=190,y=240)

            cmb_st=ttk.Combobox(pr_frame,textvariable=self.var_status,values=("Active","Inactive"),state="readonly",justify=CENTER,font=("tgoudy old style",10,"bold"))
            cmb_st.place(x=190,y=280)
            cmb_st.current(0)


             #####--------------BUTTONS--------------


            add_p=Button(pr_frame,text="ADD",command=self.add,font=("times new roman" ,15),cursor="hand2",bg="#48494B",fg="#FE5BAC",bd=4)
            add_p.place(x=30,y=350,width=110)
            

            delete_p=Button(pr_frame,text="DELETE",command=self.delete,font=("times new roman" ,15),cursor="hand2",bg="#48494B",fg="#FE5BAC",bd=4)
            delete_p.place(x=200,y=350,height=40,width=130)

            update_p=Button(pr_frame,text="UPDATE",command=self.update,font=("times new roman" ,15),cursor="hand2",bg="#48494B",fg="#FE5BAC",bd=4)
            update_p.place(x=30,y=410,height=40,width=130)


            clear_p=Button(pr_frame,text="CLEAR",command=self.clear,font=("times new roman" ,15),cursor="hand2",bg="#48494B",fg="#FE5BAC",bd=4)
            clear_p.place(x=200,y=410,height=40,width=130)

            ba_p=Button(pr_frame,text="BACK",command=self.cl,font=("times new roman" ,15),cursor="hand2",bg="#48494B",fg="#FE5BAC",bd=4)
            ba_p.place(x=30,y=510,height=40,width=130)



            #========search frame=====
            searc=LabelFrame(self.root,text="Search product",font=("times new roman",10,"bold"),bd=2,relief=RIDGE,bg="silver")
            searc.place(x=670,y=10,width=660,height=150)
 
 
            #########SEARCH FRAME=====
            cmb_search=ttk.Combobox(searc,textvariable=self.var_searchby,values=("select","item_name","category"),state="readonly",justify=CENTER,font=("tgoudy old style",10,"bold"))
            cmb_search.place(x=10,y=20,width=200,height=40)
            cmb_search.current(0)
            
            
            txtsearch=Entry(searc,textvariable=self.var_searchtxt,font=("times new roman",15,"bold"),bg="#48494B",fg="#FE5BAC").place(x=220,y=20,width=180,height=40)
            btsearch=Button(searc,text="search",command=self.search,font=("times new roman",15,"bold"),bg="#48494B",fg="#FE5BAC").place(x=440,y=10,height=40,width=120)
            showall=Button(searc,text="Show All",command=self.show_all,font=("times new roman",15,"bold"),bg="#48494B",fg="#FE5BAC").place(x=230,y=70,height=40,width=120)


            p_frame=Frame(self.root,bd=0,relief=RIDGE,bg="PINK")
            p_frame.place(x=670,y=200,width=670,height=270)

            self.MenuLogo=Image.open("images/cat2.jpg")
            self.MenuLogo=self.MenuLogo.resize((670,270),Image.ANTIALIAS)
            self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

            self.LeftMenuLogo=Label(p_frame,image=self.MenuLogo,bg="navy")
            self.LeftMenuLogo.pack(side=TOP,fill=BOTH)
            



             ###############---------------------TREEVIEW-------------------

            t_titile=Label(self.root,text="VIEW",font=("goudy old style",15,"italic"),bg="BLACK",fg="#FE5BAC")
            t_titile.place(x=670,y=480,width=670,height=30)
           
            view_p=Frame(self.root,bd=3,relief=RIDGE)
            view_p.place(x=670,y=520,width=670,height=170)
            

            scrolly=Scrollbar(view_p,orient=VERTICAL)
            scrollx=Scrollbar(view_p,orient=HORIZONTAL)


            self.producttTable=ttk.Treeview(view_p,columns=("prod_no","category","id","item_no","item_name","price","iqty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            scrollx.pack(side=BOTTOM,fill=X)
            scrolly.pack(side=RIGHT,fill=Y)
            
            scrollx.config(command=self.producttTable.xview)
            scrolly.config(command=self.producttTable.yview)
            
            
            
            self.producttTable.heading("prod_no",text="PROD_NO")
            self.producttTable.heading("category",text="category")
            self.producttTable.heading("id",text="id")
            self.producttTable.heading("item_no",text="item_no ")
            self.producttTable.heading("item_name",text="item_name")
            self.producttTable.heading("price",text="price")
            self.producttTable.heading("iqty",text="iqty")
            self.producttTable.heading("status",text="status")



            self.producttTable["show"]="headings"


            self.producttTable.column("prod_no",width=90)
            self.producttTable.column("category",width=100)
            self.producttTable.column("id",width=100)
            self.producttTable.column("item_no",width=100)
            self.producttTable.column("item_name",width=100)
            self.producttTable.column("price",width=100)
            self.producttTable.column("iqty",width=100)
            self.producttTable.column("status",width=100)

            self.producttTable.pack(fill=BOTH,expand=1)
            self.producttTable.bind("<ButtonRelease-1>",self.get_data)
            self.show()
            st.configure("Treeview",
                      background="grey",
                      foregroung="#FF2800",
                      rowheight=25,
                      fieldbackground="grey"
                      )
            st.map("Treeview",background=[("selected","navy")])
            


            #############--------------ADD--------------
        

        def  sup_cat(self):
                self.sup_list.append("Empty")
                con=sqlite3.connect(database=r'coding.db')
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

        def cl(self):
              self.root.destroy()  
        
                       
        def  add(self):
                
                con=sqlite3.connect(database=r'coding.db')
                cur=con.cursor()
                try:
                    
                    if self.var_cat.get()=="select" or self.var_item_name.get()=="":
                        messagebox.showerror("Error","Category must be required ",parent=self.root)
                    else:
                            cur.execute("select  item_no,item_name from productt where item_no=?",(self.var_item_no.get(),))
                            row=cur.fetchone()
                            if row != None:
                                    #kself.var_item_no.set(row[0])
                                    self.var_item_name.set(row[1])  
                            cur.execute("select  item_no,item_name from productt where item_name=?",(self.var_item_name.get(),))
                            row=cur.fetchone()
                            if row != None:
                                    self.var_item_no.set(row[0])
                                    #self.var_item_name.set(row[1])
                            
                        
                            cur.execute("Insert into productt(category,id,item_no,item_name,price,iqty,status) values(?,?,?,?,?,?,?)",(
                                    self.var_cat.get(),
                                    self.var_id.get(),
                                    self.var_item_no.get(),
                                    self.var_item_name.get(),
                                    self.var_price.get(),
                                    self.var_iqty.get(),
                                    self.var_status.get()
                            ))
                            con.commit()
                            messagebox.showinfo("Success","producttt added successfully",parent=self.root)
                            self.show()
                            self.cat()
                            
                       
                except Exception as ex:
                    messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)



#############--------------UPDATE--------------

        def update(self):
                 con=sqlite3.connect(database=r'coding.db')
                 cur=con.cursor()
                 try:
                    if self.var_prod_no.get()=="":
                        messagebox.showerror("Error","Please select producttt number",parent=self.root)
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
                            messagebox.showinfo("Success","producttt updated successfully",parent=self.root)
                            self.show()
                            self.cat()
                        
                 except Exception as ex:
                        messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)


#############--------------DELETE--------------
        def delete(self):
                con=sqlite3.connect(database=r'coding.db')
                cur=con.cursor()
                try:
                    if self.var_item_no.get()=="":
                        messagebox.showerror("Error","Item number  must be required ",parent=self.root)
                    else:
                        cur.execute("Select * from productt where prod_no=?",(self.var_prod_no.get(),))
                        row=cur.fetchone()
                        if row==None:
                            messagebox.showerror("Error","INVALID  user_id  ",parent=self.root)
                        else:
                            op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                            cur.execute("delete from productt where prod_no=?",(self.var_prod_no.get(),))
                            if op==True:
                                con.commit()
                                messagebox.showinfo("Success","producttt deleted successfully",parent=self.root)
                                self.show()
                                self.clear()
                                #self.cat()
             

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
                self.cat()
        def show_all(self):
                self.show()
        def cat(self):#"Select","Stationary","Cosmetics","Grocery"
                #st="Stationary"
                try:
                        if self.var_cat.get()=="Stationary":
                                self.MenuL=Image.open("images/sat1.jpg")
                                self.MenuL=self.MenuL.resize((670,270),Image.ANTIALIAS)
                                self.MenuL=ImageTk.PhotoImage(self.MenuL)

                                self.LeftMenuLogo.config(image=self.MenuL)
                        elif  self.var_cat.get()=="Cosmetics":
                                self.MenuL=Image.open("images/co1.jpg")
                                self.MenuL=self.MenuL.resize((670,270),Image.ANTIALIAS)
                                self.MenuL=ImageTk.PhotoImage(self.MenuL)

                                self.LeftMenuLogo.config(image=self.MenuL)
                        elif  self.var_cat.get()=="Grocery":
                                self.MenuL=Image.open("images/gr1.jpg")
                                self.MenuL=self.MenuL.resize((670,270),Image.ANTIALIAS)
                                self.MenuL=ImageTk.PhotoImage(self.MenuL)

                                self.LeftMenuLogo.config(image=self.MenuL)
                        elif  self.var_cat.get()=="Sports":
                                self.MenuL=Image.open("images/sports.jpeg")
                                self.MenuL=self.MenuL.resize((670,270),Image.ANTIALIAS)
                                self.MenuL=ImageTk.PhotoImage(self.MenuL)

                                self.LeftMenuLogo.config(image=self.MenuL)
                        elif  self.var_cat.get()=="Clothes":
                                self.MenuL=Image.open("images/clothe.jpg")
                                self.MenuL=self.MenuL.resize((670,270),Image.ANTIALIAS)
                                self.MenuL=ImageTk.PhotoImage(self.MenuL)

                                self.LeftMenuLogo.config(image=self.MenuL)
                        elif  self.var_cat.get()=="Gadjets":
                                self.MenuL=Image.open("images/gadjets.jpg")
                                self.MenuL=self.MenuL.resize((670,270),Image.ANTIALIAS)
                                self.MenuL=ImageTk.PhotoImage(self.MenuL)

                                self.LeftMenuLogo.config(image=self.MenuL)
                        
                        else:
                                     self.MenuLog=Image.open("images/pro.jpg")
                                     self.MenuLog=self.MenuLog.resize((670,270),Image.ANTIALIAS)
                                     self.MenuLog=ImageTk.PhotoImage(self.MenuLog)
                                     self.LeftMenuLogo.config(image=self.MenuLog)
                                        
                     
                except Exception as ex:
                        messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)



        def  get_data(self,ev):
                f=self.producttTable.focus()
                content=self.producttTable.item(f)
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
                 con=sqlite3.connect(database=r'coding.db')
                 cur=con.cursor()
                 try:
                      global c
                      c=1
                      cur.execute("select * from productt")
                      rows=cur.fetchall()
                      self.producttTable.delete(*self.producttTable.get_children())
                      self.producttTable.tag_configure('oddrow',background="pink")
                      self.producttTable.tag_configure('evrow',background="red")
                      for row in rows:
                          if c%2==0:
                                  self.producttTable.insert('',END,values=row,tag=('evrow'))
                          else:
                                   self.producttTable.insert('',END,values=row,tag=('oddrow'))
                          c +=1

                 except Exception as ex:
                     messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)



        def search(self):
                con=sqlite3.connect(database=r'coding.db')
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
                                        self.producttTable.delete(*self.producttTable.get_children())
                                        for row in ro:
                                                self.producttTable.insert('',END,values=row)
                                                bn=True
                                 else:
                                        messagebox.showerror("Error","No record found",parent=self.root)
                                        bn=False
                        if bn:
                                if self.var_cat.get()=="Stationary":
                                        self.MenuL=Image.open("images/sat1.jpg")
                                        self.MenuL=self.MenuL.resize((670,270),Image.ANTIALIAS)
                                        self.MenuL=ImageTk.PhotoImage(self.MenuL)

                                        self.LeftMenuLogo.config(image=self.MenuL)
                                elif  self.var_cat.get()=="Cosmetics":
                                        self.MenuL=Image.open("images/co1.jpg")
                                        self.MenuL=self.MenuL.resize((670,270),Image.ANTIALIAS)
                                        self.MenuL=ImageTk.PhotoImage(self.MenuL)

                                        self.LeftMenuLogo.config(image=self.MenuL)
                                elif  self.var_cat.get()=="Grocery":
                                        self.MenuL=Image.open("images/gr1.jpg")
                                        self.MenuL=self.MenuL.resize((670,270),Image.ANTIALIAS)
                                        self.MenuL=ImageTk.PhotoImage(self.MenuL)

                                        self.LeftMenuLogo.config(image=self.MenuL)
                                elif  self.var_cat.get()=="Sports":
                                        self.MenuL=Image.open("images/sports.jpeg")
                                        self.MenuL=self.MenuL.resize((670,270),Image.ANTIALIAS)
                                        self.MenuL=ImageTk.PhotoImage(self.MenuL)

                                        self.LeftMenuLogo.config(image=self.MenuL)
                                elif  self.var_cat.get()=="Clothes":
                                        self.MenuL=Image.open("images/clothe.jpg")
                                        self.MenuL=self.MenuL.resize((670,270),Image.ANTIALIAS)
                                        self.MenuL=ImageTk.PhotoImage(self.MenuL)

                                        self.LeftMenuLogo.config(image=self.MenuL)
                                elif  self.var_cat.get()=="Gadjets":
                                        self.MenuL=Image.open("images/gadjets.jpg")
                                        self.MenuL=self.MenuL.resize((670,270),Image.ANTIALIAS)
                                        self.MenuL=ImageTk.PhotoImage(self.MenuL)

                                        self.LeftMenuLogo.config(image=self.MenuL)
                                
                                else:
                                     self.MenuLog=Image.open("images/pro.jpg")
                                     self.MenuLog=self.MenuLog.resize((670,270),Image.ANTIALIAS)
                                     self.MenuLog=ImageTk.PhotoImage(self.MenuLog)
                                     self.LeftMenuLogo.config(image=self.MenuLog)
                                        
                     
                                

                except Exception as ex:
                     messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root) 
                
class VPRO:
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1350x710+0+0")
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

            view_p=Frame(self.root,bd=3,relief=RIDGE)
            view_p.place(x=0,y=0,relwidth=1,height=400)
            

            scrolly=Scrollbar(view_p,orient=VERTICAL)
            scrollx=Scrollbar(view_p,orient=HORIZONTAL)


            self.producttTable=ttk.Treeview(view_p,columns=("prod_no","category","id","item_no","item_name","price","iqty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            scrollx.pack(side=BOTTOM,fill=X)
            scrolly.pack(side=RIGHT,fill=Y)
            
            scrollx.config(command=self.producttTable.xview)
            scrolly.config(command=self.producttTable.yview)
            
            
            
            self.producttTable.heading("prod_no",text="PROD_NO")
            self.producttTable.heading("category",text="category")
            self.producttTable.heading("id",text="id")
            self.producttTable.heading("item_no",text="item_no ")
            self.producttTable.heading("item_name",text="item_name")
            self.producttTable.heading("price",text="price")
            self.producttTable.heading("iqty",text="iqty")
            self.producttTable.heading("status",text="status")



            self.producttTable["show"]="headings"


            self.producttTable.column("prod_no",width=90)
            self.producttTable.column("category",width=100)
            self.producttTable.column("id",width=100)
            self.producttTable.column("item_no",width=100)
            self.producttTable.column("item_name",width=100)
            self.producttTable.column("price",width=100)
            self.producttTable.column("iqty",width=100)
            self.producttTable.column("status",width=100)

            self.producttTable.pack(fill=BOTH,expand=1)
            self.producttTable.bind("<ButtonRelease-1>",self.get_data)
            self.show()
            st.configure("Treeview",
                      background="grey",
                      foregroung="#FF2800",
                      rowheight=25,
                      fieldbackground="grey"
                      )
            st.map("Treeview",background=[("selected","navy")])


        def  get_data(self,ev):
                f=self.producttTable.focus()
                content=self.producttTable.item(f)
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
                 con=sqlite3.connect(database=r'coding.db')
                 cur=con.cursor()
                 try:
                      global c
                      c=1
                      cur.execute("select * from productt")
                      rows=cur.fetchall()
                      self.producttTable.delete(*self.producttTable.get_children())
                      self.producttTable.tag_configure('oddrow',background="pink")
                      self.producttTable.tag_configure('evrow',background="red")
                      for row in rows:
                          if c%2==0:
                                  self.producttTable.insert('',END,values=row,tag=('evrow'))
                          else:
                                   self.producttTable.insert('',END,values=row,tag=('oddrow'))
                          c +=1

                 except Exception as ex:
                     messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)

            

            

        

if  __name__=="__main__":
     root=Tk()
     obj=PROD(root)
     root.mainloop()
