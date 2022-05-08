from tkinter import*
from tkinter import ttk,messagebox
import  sqlite3
import time
import os
from PIL import Image,ImageTk

class billss:
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1350x710+0+0")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="black")
            self.root.focus_force()
            self.my_canvas=Canvas(self.root,width=1350,height=80,bd=1)
            '''self.Lo=Image.open("images/bgg2.jpeg")
            self.Lo=self.Lo.resize((1350,700),Image.ANTIALIAS)
            self.Lo=ImageTk.PhotoImage(self.Lo)
            self.phone_i=Label(self.root,image=self.Lo)
            self.phone_i.place(x=0,y=0,width=1350,height=700)
            my_canvas=Canvas(self.root,width=1140,height=560)'''
            self.my_canvas.place(x=0,y=0)
            self.my_canvas.configure(bg="white")
            self.my_canvas.create_text(650,40,text="EMPLOYEE WORK BOARD",font=("times new roman",30,"bold"),fill="PINK")
            self.button1=Button(self.my_canvas,text="Logout",font=("times new roman",15,"bold"),command=self.logout,anchor=W)
            self.button1.configure(width=40,bg="white",fg="pink",bd=0)
            self.button1.place(x=1000,y=20)
            

            self.phone_im=Label(self.root,bd=3)#image=self.Lo)
            self.phone_im.place(x=0,y=90,width=1350,height=610)
            self.Logo1=Image.open("images/emp1.jpg")
            self.Logo1=self.Logo1.resize((1340,610),Image.ANTIALIAS)
            self.Logo1=ImageTk.PhotoImage(self.Logo1)
            
            self.Logo2=Image.open("images/emp2.jpg")
            self.Logo2=self.Logo2.resize((1340,710),Image.ANTIALIAS)
            self.Logo2=ImageTk.PhotoImage(self.Logo2)
            self.Logo3=Image.open("images/emp3.jpg")
            self.Logo3=self.Logo3.resize((1340,710),Image.ANTIALIAS)
            self.Logo3=ImageTk.PhotoImage(self.Logo3)
            
            
            

#-----------------------TITLE---------------------------------------------
            #emp_title=Label(self.root,text="EMPLOYEE DETAILS",font=("times new roman",40,"bold"),fg="#FF2800",bg="#4B3619",bd=4,relief=RIDGE,padx=20).place(x=0,y=0,relwidth=1,height=60)

   #  button MANAGE AND VIEW
            btn_manage=Button(self.root,text="MANAGE BILL ",command=self.mbill,font=("times new roman",10,"italic"),fg="#FF2800",bg="#4B3619",cursor="hand2",bd=5)
            btn_manage.place(x=440,y=70,height=60,width=210)
            self.ani()


            
            '''leftmenu=Frame(self.root,bd=0,relief=RIDGE,bg="#4B3619")
            leftmenu.place(x=200,y=150,width=600,height=400)

            self.MenuLogo=Image.open("images/bg.png")
            self.MenuLogo=self.MenuLogo.resize((580,380),Image.ANTIALIAS)
            self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

            LeftMenuLogo=Label(leftmenu,image=self.MenuLogo,bg="#4B3619")
            LeftMenuLogo.pack(side=TOP,fill=BOTH)'''




##----------MANAGE EMP DETAILS -------
        def  mbill(self):
           self.new_win=Toplevel(self.root)
           self.new_obj=billing(self.new_win)
        def ani(self):
                self.im=self.Logo1
                self.Logo1=self.Logo2
                self.Logo2=self.Logo3
                self.Logo3=self.im
                self.phone_im.config(image=self.im)
                self.phone_im.after(1200,self.ani)

        def logout(self):
                self.root.destroy()
                os.startfile("login.py")

                

class billing:
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1350x710+0+0")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="white")
            self.Lo=Image.open("images/b1.png")
            self.Lo=self.Lo.resize((1350,700),Image.ANTIALIAS)
            self.Lo=ImageTk.PhotoImage(self.Lo)
            self.phone_i=Label(self.root,image=self.Lo)
            self.phone_i.place(x=0,y=0,width=1350,height=700)


            self.cart_list=[]
            self.qq=0
            st=ttk.Style()
            st.theme_use("clam")
            
        

            #  title
            self.MenuLogo=Image.open("images/logo5.jpg")
            self.MenuLogo=self.MenuLogo.resize((70,70),Image.ANTIALIAS)
            self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
            title=Label(self.root,text="Retail Management",image=self.MenuLogo,compound=LEFT,font=("times new roman",40,"bold"),bg="black",fg="#FFBF00",padx=20).place(x=0,y=0,relwidth=1,height=70)

          
            b_title=Label(self.root,text=" Welcome  to Retail Management",font=("times new roman",15,"bold"),fg="#FF2800",bg="#4B3619",bd=2).place(x=0,y=70,relwidth=1,height=30)

            #=PRODUCT FRAME=======
            self.var_search=StringVar()
            prod1_frame=Frame(self.root,bd=3,relief=RIDGE,bg="#003151")
            prod1_frame.place(x=5,y=110,height=530,width=400)

            ptitle=Label(prod1_frame,text="All Products",font=("times new roman",20,"bold"),bg="#003151",fg="#FDA50F").pack(side=TOP,fill=X)

            prod2_frame=Frame(prod1_frame,bd=3,relief=RIDGE,bg="#003151")
            prod2_frame.place(x=2,y=42,height=90,width=390)

            psearch=Label(prod2_frame,text="Search product",font=("times new roman",10,"bold"),bg="#003151",fg="#FDA50F").place(x=2,y=5)

            lbl_name=Label(prod2_frame,text="Product name",font=("times new roman",10,"bold"),bg="#003151",fg="#FDA50F").place(x=5,y=45)

            txt_search=Entry(prod2_frame,textvariable=self.var_search,font=("times new roman",10,"bold"),bg="#003151",fg="#FDA50F").place(x=90,y=45)

            butt_search=Button(prod2_frame,text="Search",command=self.search,font=("times new roman",10,"bold"),cursor="hand2",bg="#003151",fg="#FDA50F").place(x=250,y=45)

            butt_show=Button(prod2_frame,text="Show all",command=self.showall,font=("times new roman",10,"bold"),cursor="hand2",bg="#003151",fg="#FDA50F").place(x=250,y=5)


###########=TREEVIEW============
            prod3_frame=Frame(prod1_frame,bd=3,relief=RIDGE)
            prod3_frame.place(x=2,y=140,height=360,width=390)

            scrolly=Scrollbar(prod3_frame,orient=VERTICAL)
            scrollx=Scrollbar(prod3_frame,orient=HORIZONTAL)


            self.carttable=ttk.Treeview(prod3_frame,columns=("prod_no","category","item_no","item_name","price","iqty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            scrollx.pack(side=BOTTOM,fill=X)
            scrolly.pack(side=RIGHT,fill=Y)
            
            scrollx.config(command=self.carttable.xview)
            scrolly.config(command=self.carttable.yview)
            
            
            
            self.carttable.heading("prod_no",text="prod_no")
            self.carttable.heading("category",text="category")
            self.carttable.heading("item_no",text="item_no ")
            self.carttable.heading("item_name",text="item_name")
            self.carttable.heading("price",text="price")
            self.carttable.heading("iqty",text="iqty")
            self.carttable.heading("status",text="status")



            self.carttable["show"]="headings"


            self.carttable.column("prod_no",width=90)
            self.carttable.column("category",width=100)
            self.carttable.column("item_no",width=50)
            self.carttable.column("item_name",width=100)
            self.carttable.column("price",width=100)
            self.carttable.column("iqty",width=100)
            self.carttable.column("status",width=100)

            self.carttable.pack(fill=BOTH,expand=1)
            self.carttable.bind("<ButtonRelease-1>",self.get_data)
            self.show()
            st.configure("Treeview",
                      background="grey",
                      foregroung="#FF2800",
                      rowheight=25,
                      fieldbackground="black"
                      )
            st.map("Treeview",background=[("selected","navy")])
            

            last_lbl=Label(prod1_frame,text="Note:Enter 0 quantity to remove product from cart",font=("times new roman",10,"bold"),fg="red").pack(side=BOTTOM,fill=X)


            ###==========CUSTOMER FRAME==========
            self.var_name=StringVar()
            self.var_contact=StringVar()

            prod4_frame=Frame(self.root,bd=3,relief=RIDGE,bg="#48494B")
            prod4_frame.place(x=410,y=110,height=100,width=500)

            ctitle=Label(prod4_frame,text="Customer details",font=("times new roman",20,"bold"),bg="#48494B",fg="#FE5BAC").pack(side=TOP,fill=X)

            clbl_name=Label(prod4_frame,text=" name",font=("times new roman",10,"bold"),bg="#48494B",fg="#FE5BAC").place(x=5,y=45)
            ctxt_name=Entry(prod4_frame,textvariable=self.var_name,font=("times new roman",10,"bold"),bg="#48494B",fg="#FE5BAC").place(x=70,y=45,width=100)

            clbl_contact=Label(prod4_frame,text=" Contact no:",font=("times new roman",10,"bold"),bg="#48494B",fg="#FE5BAC").place(x=200,y=45)
            ctxt_contact=Entry(prod4_frame,textvariable=self.var_contact,font=("times new roman",10,"bold"),bg="#48494B",fg="#FE5BAC").place(x=280,y=45,width=150)


            cal_cart_frame=Frame(self.root,bd=3,relief=RIDGE,bg="#48494B")
            cal_cart_frame.place(x=410,y=210,height=280,width=500)
            
    #=====calculator==========
            self.var_cal=StringVar()

            cal_frame=Frame(cal_cart_frame,bd=5,relief=RIDGE,bg="#48494B")
            cal_frame.place(x=3,y=5,height=260,width=260)

            self.txt_cal=Entry(cal_frame,textvariable=self.var_cal,font=("times new roman",10),bg="#48494B",fg="#FE5BAC",width=39,bd=8,relief=GROOVE)
            self.txt_cal.grid(row=0,columnspan=4)

            btn7=Button(cal_frame,text="7",command=lambda:self.get_input(7),font=("times new roman",10),bg="#48494B",fg="#FE5BAC",cursor="hand2",width=4,pady=10).grid(row=1,column=0)
            btn8=Button(cal_frame,text="8",command=lambda:self.get_input(8),font=("times new roman",10),bg="#48494B",fg="#FE5BAC",cursor="hand2",width=4,pady=10).grid(row=1,column=1)
            btn9=Button(cal_frame,text="9",command=lambda:self.get_input(9),font=("times new roman",10),bg="#48494B",fg="#FE5BAC",cursor="hand2",width=4,pady=10).grid(row=1,column=2)
            btnsum=Button(cal_frame,text="+",command=lambda:self.get_input('+'),font=("times new roman",10),bg="#48494B",fg="#FE5BAC",cursor="hand2",width=4,pady=10).grid(row=1,column=3)

            btn4=Button(cal_frame,text="4",command=lambda:self.get_input(4),font=("times new roman",10),bg="#48494B",fg="#FE5BAC",cursor="hand2",width=4,pady=10).grid(row=2,column=0)
            btn5=Button(cal_frame,text="5",command=lambda:self.get_input(5),font=("times new roman",10),cursor="hand2",bg="#48494B",fg="#FE5BAC",width=4,pady=10).grid(row=2,column=1)
            btn6=Button(cal_frame,text="6",command=lambda:self.get_input(6),font=("times new roman",10),cursor="hand2",width=4,pady=10,bg="#48494B",fg="#FE5BAC").grid(row=2,column=2)
            btnminus=Button(cal_frame,text="-",command=lambda:self.get_input('-'),font=("times new roman",10),cursor="hand2",width=4,pady=10,bg="#48494B",fg="#FE5BAC").grid(row=2,column=3)

            btn1=Button(cal_frame,text="1",command=lambda:self.get_input(1),font=("times new roman",10),cursor="hand2",width=4,pady=10,bg="#48494B",fg="#FE5BAC",).grid(row=3,column=0)
            btn2=Button(cal_frame,text="2",command=lambda:self.get_input(2),font=("times new roman",10),cursor="hand2",width=4,pady=10,bg="#48494B",fg="#FE5BAC",).grid(row=3,column=1)
            btn3=Button(cal_frame,text="3",command=lambda:self.get_input(3),font=("times new roman",10),cursor="hand2",width=4,pady=10,bg="#48494B",fg="#FE5BAC",).grid(row=3,column=2)
            btnmul=Button(cal_frame,text="*",command=lambda:self.get_input('*'),font=("times new roman",10),cursor="hand2",width=4,pady=10,bg="#48494B",fg="#FE5BAC",).grid(row=3,column=3)

            btno=Button(cal_frame,text="0",command=lambda:self.get_input(0),bg="#48494B",fg="#FE5BAC",font=("times new roman",10),cursor="hand2",width=4,pady=10).grid(row=4,column=0)
            btnclear=Button(cal_frame,text="C",font=("times new roman",10),bg="#48494B",fg="#FE5BAC",command=self.cl,cursor="hand2",width=4,pady=10).grid(row=4,column=1)
            btneq=Button(cal_frame,text="=",font=("times new roman",10),bg="#48494B",fg="#FE5BAC",command=self.perform_cal,cursor="hand2",width=4,pady=10).grid(row=4,column=2)
            btndiv=Button(cal_frame,text="/",command=lambda:self.get_input('/'),bg="#48494B",fg="#FE5BAC",font=("times new roman",10),cursor="hand2",width=4,pady=10).grid(row=4,column=3)

        #=============CART FRAME========

            cart_frame=Frame(cal_cart_frame,bd=3,relief=RIDGE,bg="#48494B")
            cart_frame.place(x=270,y=5,height=260,width=210)
            self.cctitle=Label(cart_frame,text="Cart   total  Products [0]",bg="#48494B",fg="#FE5BAC",font=("times new roman",10))
            self.cctitle.pack(side=TOP,fill=X)

            scrolly=Scrollbar(cart_frame,orient=VERTICAL)
            scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)


            self.cartTable=ttk.Treeview(cart_frame,columns=("prod_no","item_name","price","iqty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            scrollx.pack(side=BOTTOM,fill=X)
            scrolly.pack(side=RIGHT,fill=Y)
            
            scrollx.config(command=self.cartTable.xview)
            scrolly.config(command=self.cartTable.yview)
            
            
            
            self.cartTable.heading("prod_no",text="prod_no")  
            self.cartTable.heading("item_name",text="item_name")
            self.cartTable.heading("price",text="price")
            self.cartTable.heading("iqty",text="iqty")
            



            self.cartTable["show"]="headings"


            self.cartTable.column("prod_no",width=70)
            self.cartTable.column("item_name",width=90)
            self.cartTable.column("price",width=70)
            self.cartTable.column("iqty",width=40)
            

            self.cartTable.pack(fill=BOTH,expand=1)
            self.cartTable.bind("<ButtonRelease-1>",self.get_cart)
            #self.show
            st.configure("Treeview",
                      background="grey",
                      foregroung="#FF2800",
                      rowheight=25,
                      fieldbackground="grey"
                      )
            st.map("Treeview",background=[("selected","navy")])
            

        #=MENU ADD CART BUTTON====

            self.var_pid=StringVar()
            self.var_pname=StringVar()
            self.var_price=StringVar()
            self.var_qty=StringVar()
            self.var_stock=StringVar()
            
            add_cart_frame=Frame(self.root,bd=3,relief=RIDGE,bg="#48494B")
            add_cart_frame.place(x=410,y=500,height=110,width=500)


            p_name=Label(add_cart_frame,text="Product name",font=("times new roman",10,),bg="#48494B",fg="#FE5BAC").place(x=5,y=5)
            txt_name=Entry(add_cart_frame,textvariable=self.var_pname,font=("times new roman",10,"bold"),bg="#48494B",fg="#FE5BAC",state="readonly").place(x=110,y=5)

            p_price=Label(add_cart_frame,text="price",font=("times new roman",10,"bold"),bg="#48494B",fg="#FE5BAC").place(x=5,y=35)
            txt_price=Entry(add_cart_frame,textvariable=self.var_price,font=("times new roman",10,"bold"),bg="#48494B",fg="#FE5BAC",state="readonly").place(x=110,y=35)

            p_qty=Label(add_cart_frame,text="qty",font=("times new roman",10,"bold"),bg="#48494B",fg="#FE5BAC").place(x=5,y=65)
            txt_qty=Entry(add_cart_frame,textvariable=self.var_qty,font=("times new roman",10,"bold"),bg="#48494B",fg="#FE5BAC").place(x=110,y=65)


            self.stock=Label(add_cart_frame,text="In stock ",font=("times new roman",10),bg="#48494B",fg="#FE5BAC")
            self.stock.place(x=280,y=5)

            btn_clr=Button(add_cart_frame,text="Clear",command=self.clear_cart,font=("times new roman",10),cursor="hand2",bg="#48494B",fg="#FE5BAC").place(x=280,y=35)
            btn_add=Button(add_cart_frame,text="Add | Update cart",command=self.ad_update,font=("times new roman",10),cursor="hand2",fg="black").place(x=280,y=65)


            #=========BILL AREA======

            billframe=Frame(self.root,bd=2,relief=RIDGE,bg="#222021")
            billframe.place(x=913,y=110,width=430,height=410)

            

            btitle=Label(billframe,text="Bill AREA",font=("times new roman",20,"bold"),bg="#222021",fg="#E4CD05").pack(side=TOP,fill=X)
            scrolly=Scrollbar(billframe,orient=VERTICAL)
            scrolly.pack(side=RIGHT,fill=Y)
            
            self.txt_bill=Text(billframe,yscrollcommand=scrolly.set)
            self.txt_bill.pack(fill=BOTH,expand=1)
            scrolly.config(command=self.txt_bill.yview)


            #########BILLLB UTTON=======
            bbillframe=Frame(self.root,bd=2,relief=RIDGE,bg="#222021")
            bbillframe.place(x=913,y=530,width=430,height=130)

            self.lbl_amt=Label(bbillframe,text="Bill amount\n [0]",font=("times new roman",10),bg="#222021",fg="#E4CD05")
            self.lbl_amt.place(x=2,y=5,width=120,height=60)

            self.dis=Label(bbillframe,text="Discount\n [5%]",font=("times new roman",10),bg="#222021",fg="#E4CD05")
            self.dis.place(x=124,y=5,width=120,height=60)

            self.netpay=Label(bbillframe,text="Net Pay\n [0]",font=("times new roman",10),bg="#222021",fg="#E4CD05")
            self.netpay.place(x=246,y=5,width=120,height=60)

            clear=Button(bbillframe,text="Clear all",command=self.clear_all,font=("times new roman",10),bg="#222021",fg="#E4CD05",cursor="hand2",)
            clear.place(x=2,y=74,width=120,height=50)

            addd=Button(bbillframe,text="Generate bill",command=self.generate_bill,font=("times new roman",10),cursor="hand2",bg="#222021",fg="#E4CD05")
            addd.place(x=129,y=74,width=120,height=50)
            
        
           
            ######====ALL FUNCTION============
        def  get_input(self,num):
            xnum=self.var_cal.get()+str(num)
            self.var_cal.set(xnum)

        def cl(self):
            self.var_cal.set(' ')

        def perform_cal(self):
            result=self.var_cal.get()
            self.var_cal.set(eval(result))

        def show(self):
                 con=sqlite3.connect(database=r'coding.db')
                 cur=con.cursor()
                 try:
                      global c
                      c=1
                      cur.execute("select  prod_no,category,item_no,item_name,price,iqty,status from productt where status='Active'")
                      rows=cur.fetchall()
                      self.carttable.delete(*self.carttable.get_children())
                      self.carttable.tag_configure('oddrow',background="pink")
                      self.carttable.tag_configure('evrow',background="red")
                      for row in rows:
                              if c % 2==0: 
                                    self.carttable.insert('',END,values=row,tags=('evrow',))
                              else:
                                    self.carttable.insert('',END,values=row,tags=('oddrow',))
                              c +=1 

                 except Exception as ex:
                     messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)

        def search(self):
                con=sqlite3.connect(database=r'coding.db')
                cur=con.cursor()
                global c
                c=1
                try:
                        if self.var_search.get()=="":
                                 messagebox.showerror("Error","search input required  ",parent=self.root)
                        else:
                                 cur.execute("Select  prod_no,category,item_no,item_name,price,iqty,status from productt where item_name LIKE '%"+self.var_search.get()+ "%' and  status='Active' ")
                                 rows=cur.fetchall()
                                 
                                 if len(rows)!=0:
                                        self.carttable.delete(*self.carttable.get_children())
                                        self.carttable.tag_configure('oddrow',background="pink")
                                        self.carttable.tag_configure('evrow',background="red")
                                        for row in rows:
                                                 if c % 2==0: 
                                                         self.carttable.insert('',END,values=row,tags=('evrow',))
                                                 else:
                                                          self.carttable.insert('',END,values=row,tags=('oddrow',))
                                                 c +=1 
                 
                                 else:
                                        messagebox.showerror("Error","No record found",parent=self.root)
                        

                except Exception as ex:
                     messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)


        def showall(self):
                 con=sqlite3.connect(database=r'coding.db')
                 cur=con.cursor()
                 global c
                 c=1
                 try:
                      cur.execute("select  prod_no,category,item_no,item_name,price,iqty,status from productt where status='Active'")
                      rows=cur.fetchall()
                      self.carttable.delete(*self.carttable.get_children())
                      self.carttable.tag_configure('oddrow',background="pink")
                      self.carttable.tag_configure('evrow',background="red")
                      for row in rows:
                              if c % 2==0: 
                                    self.carttable.insert('',END,values=row,tags=('evrow',))
                              else:
                                    self.carttable.insert('',END,values=row,tags=('oddrow',))
                              c +=1 

                 except Exception as ex:
                     messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)
        

        def  get_data(self,ev):
                f=self.carttable.focus()
                content=self.carttable.item(f)
                row=content['values']
                self.var_pid.set(row[0])
                self.var_pname.set(row[3])
                self.var_price.set(row[4])
                self.stock.config(text=f"In stock [{str(row[5])}]:")
                self.var_stock.set(row[5])
                self.var_qty.set('1')


        def  get_cart(self,ev):
                f=self.cartTable.focus()
                content=self.cartTable.item(f)
                row=content['values']
                self.var_pid.set(row[0])
                self.var_pname.set(row[1])
                self.var_price.set(row[2])
                self.var_qty.set(row[3])
                self.stock.config(text=f"In stock [{str(row[4])}]:")
                self.var_stock.set(row[4])

        def ad_update(self):
                if self.var_pid.get()=="" :
                        messagebox.showerror("Error","Please select product from list",parent=self.root)

                elif  self.var_qty.get()=="":
                        messagebox.showerror("Error","Quantity is required",parent=self.root)

                elif int(self.var_qty.get())>int(self.var_stock.get()):
                        messagebox.showerror("Error","Invalid Quantity ",parent=self.root)
                
                else:
                       # price_cal=float(int(self.var_qty.get())*float(self.var_price.get()))
                        
                        #prod_no","item_name","price","iqty
                        price_cal=self.var_price.get()
                        cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]
                        

                        ##UPDATE CART==========
                        present='no'
                        index_=0
                        for row in self.cart_list:
                                if self.var_pid.get()==row[0]:
                                        
                                        present='yes'
                                        break
                                index_ += 1
                               
                        if  present=='yes':
                                op=messagebox.askyesno('Confirm',"Product alredy there if you want to update | remove",parent=self.root)
                                if op==True:
                                        if self.var_qty.get()=="0":
                                                #self.cart_list[index_][2]=price_cal
                                                self.cart_list.pop(index_)
                                        else:
                                              
                                                self.cart_list[index_][3]=self.var_qty.get()
                        
                        else:
                                self.cart_list.append(cart_data)
                                
                        self.show_cart()
                        self.bill_update()

        def bill_update(self):
                self.bill_amt=0
                self.net_pay=0
                self.discount=0
                for row in self.cart_list:
                        self.bill_amt=self.bill_amt+(float(row[2]))*int(row[3])
                self.discount=(self.bill_amt*5)/100
                self.net_pay=self.bill_amt-(self.bill_amt*5)/100
                self.lbl_amt.config(text=f'Bill amount\n[{str(self.bill_amt)}] ')
                self.netpay.config(text=f'Net Pay\n[{str(self.net_pay)}] ')
                #cctitle=Label(cart_frame,text="Cart  \ttotal  Products [0]:",font=("times new roman",10),fg="green").pack(side=TOP,fill=X)
                self.cctitle.config(text=f'Cart   total  Products [{str(len(self.cart_list))}]')

        def show_cart(self):
                try:
                        self.cartTable.delete(*self.cartTable.get_children())
                        for row in self.cart_list:
                                
                                self.cartTable.insert('',END,values=row)
                

                except Exception as ex:
                     messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)
                
                        
        def generate_bill(self):
                if self.var_name.get()==" "or self.var_contact.get()=="":
                        messagebox.showerror("Error","Customer details are reqired",parent=self.root)

                elif len(self.cart_list)==0:
                        messagebox.showerror("Error","Please add product to cart",parent=self.root)

                else:
                        #BILLTOP==
                        self.bill_top()
                        
                        #BILLMIDDLE==
                        self.bill_middle()
                        ##BILL BOTTOM==
                        self.bill_bottom()

                        fp=open(f'bill/{self.bill_no}.txt','w')
                        fp.write(self.txt_bill.get('1.0',END))
                        fp.close()
                        messagebox.showinfo("Saved","Bill has been generated/Save in backend",parent=self.root)
                        
        
                        
        def bill_top(self):
                 
                 self.bill_no=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
                 bill_top_temp=f'''
\t\tBIG BAZZAR-Retail
\tPhone No:9844******,Kundapur-3873
{str("="*50)}
Customer Name:{self.var_name.get()}
Mobile No:{self.var_contact.get()}
Bill no:{str(self.bill_no)}\t\t\tDate: {str(time.strftime("%d:%m:%Y"))}
{str("="*50)}
 Product Name:\t\t\tQTY\tPRICE
{str("="*50)}
                '''
                 self.txt_bill.delete('1.0',END)
                 self.txt_bill.insert('1.0',bill_top_temp)
                
        def bill_bottom(self):
                bill_btemp=f'''
{str("="*50)}
Bill Amount\t\t\tRs.{self.bill_amt}
Discount\t\t\t  {self.discount}
Net Pay\t\t\tRs.{self.net_pay}
{str("="*50)}\n
                '''
                self.txt_bill.insert(END,bill_btemp)

        def bill_middle(self):
                con=sqlite3.connect(database=r'coding.db')
                cur=con.cursor()
                try:
                        
                        for row in self.cart_list:
                                name=row[1]
                                qty=(int (row[4])) - (int(row[3]))
                                prod_no=row[0]
                                if  int(row[3]) == int (row[4]):
                                        status="Inactive"
                                if  int(row[3]) != int (row[4]):
                                        status="Active"
                        
                                
                                price=float(row[2])*int(row[3])
                                pric=str(price)
                                self.txt_bill.insert(END,"\n"+name+"\t\t\t"+row[3]+"\tRs."+pric)
                                qq=str(qty)
                        
                                cur.execute("Update  productt set iqty=?,status=? where prod_no=?",(
                                        qq,
                                        status,
                                        prod_no
                                ))
                                con.commit()
                        con.close()
                        self.show()
                except Exception as ex:
                        messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)

                
            
        def clear_cart(self):
            self.var_pid.set(' ')
            self.var_pname.set(' ')
            self.var_price.set(' ')
            self.var_qty.set(' ')
            self.stock.config(text=f"In stock []:")
            self.var_stock.set(' ')
            self.var_cal.set('')

        def clear_all(self):
                del self.cart_list[:]
                self.lbl_amt.config(text="Bill amount\n [0]")
                self.dis.config(text="Discount\n [5%]")
                self.netpay.config(text="Net Pay\n [0]")
                self.var_name.set(' ')
                self.var_contact.set(' ')
                self.txt_bill.delete('1.0',END)
                self.cctitle.config(text=f'Cart   total  Products [0]')
                self.var_search.set(' ')
                self.clear_cart()
                self.show()
                self.show_cart()
                
                
        


            

            

            

            





if  __name__=="__main__":
     root=Tk()
     obj=billss(root)
     root.mainloop()
            
