from tkinter import *
from tkinter import ttk
from tkcalendar import  Calendar,DateEntry
import sqlite3
from tkinter import messagebox as ms
class upd:
    def __init__(s,root):
        s.root=root
        s.root.geometry("1530x850+380+172")
        s.root.title("PLACEMENT MANAGEMENT SYSTEM | MCA STUDENTS")
        s.root.config(bg="white")
        s.root.focus_force()

        ####---------- ALL VARIABLES---
        s.var_searchby=StringVar()
        s.var_search=StringVar()
        s.var_stud_id=StringVar()
        s.var_name=StringVar()
        s.var_dob=StringVar()
        s.var_mobileno=StringVar()
        s.var_email=StringVar()
        s.var_company=StringVar()
        s.var_status=StringVar()
        s.var_pwd=StringVar()

        

        #++++++++++++ search frame ++++++++++
        searc=LabelFrame(s.root,text="Search Product",font=("times new roman",10,"bold"),bd=2,relief=RIDGE,bg="white")
        searc.place(x=310,y=0,width=800,height=80)

        # ++++++++ options +++++++
        cmb_cat=ttk.Combobox(searc,textvariable=s.var_searchby,values=("Select","stud_id","name","company"),state="readonly",justify=CENTER,font=("tgoudy old style",10,"bold"))
        cmb_cat.place(x=0,y=0)
        cmb_cat.current(0)
        txtsearch=Entry(searc,textvariable=s.var_search,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=280,y=9,width=220,height=30)

        btsearch=Button(searc,text="search",command=s.search1,font=("Times new Roman",15),bd=2,bg="white",cursor="hand2").place(x=520,y=10,height=30,width=160)

        title=Label(s.root,text="Student details",font=("goudy old style",15),bg="brown").place(x=40,y=100,width=1300)


          ##--------EMP ENTERIES-----------
##-----------   stud_id--------
        user_emp=Label(s.root,text="stud_id",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        user_emp.place(x=61,y=190,height=40,width=110)
        ##-----------   NAME--------
        name_emp=Label(s.root,text="Name",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        name_emp.place(x=611,y=190,height=40,width=110)
        ##-----------   DOB--------
        doj_emp=Label(s.root,text="Dob",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        doj_emp.place(x=61,y=250,height=40,width=110)
        ##-----------   MOBILE_NO--------
        mob_emp=Label(s.root,text="Mobile no",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        mob_emp.place(x=611,y=250,height=40,width=110)
        ##-----------EMAIL--------
        pass_emp=Label(s.root,text="Email",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        pass_emp.place(x=61,y=320,height=40,width=110)
        ##-----------COMPANY--------
        utype_emp=Label(s.root,text="Comapny",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        utype_emp.place(x=611,y=320,height=40,width=110)

        ##-----------STATUS--------
        utype_emp=Label(s.root,text="Status",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        utype_emp.place(x=61,y=390,height=40,width=110)

         ##-----------Password--------
        utype_stud=Label(s.root,text="Password",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        utype_stud.place(x=611,y=390,height=40,width=110)





        ###---------ENTRY -----------
        user_Eemp=Entry(s.root,textvariable=s.var_stud_id,font=("times new roman" ,15),bg="white",bd=4)
        user_Eemp.place(x=271,y=190,height=40,width=210)

        ###---------NAME -----------
        nam_Eemp=Entry(s.root,textvariable=s.var_name,font=("times new roman" ,15),bg="white",bd=4)
        nam_Eemp.place(x=771,y=190,height=40,width=210)

        ###---------DOB -----------
        s.doj_Eemp=Entry(s.root,textvariable=s.var_dob,font=("times new roman",15),bg="white",bd=4)
        s.doj_Eemp.place(x=271,y=250,height=40,width=200)
        
            
        
        ###---------MOBILE_NO -----------
        mob_Eemp=Entry(s.root,textvariable=s.var_mobileno,font=("times new roman" ,15),fg="black",bg="white",bd=4)
        mob_Eemp.place(x=771,y=250,height=40,width=210)

        ###---------EMAIL -----------
        pass_Eemp=Entry(s.root,textvariable=s.var_email,font=("times new roman" ,15),fg="black",bg="white",bd=4)
        pass_Eemp.place(x=271,y=320,height=40,width=210)

        ###---------COMPANY -----------
        utype_Eemp=Entry(s.root,textvariable=s.var_company,font=("times new roman" ,15),fg="black",bg="white",bd=4)
        utype_Eemp.place(x=771,y=320,height=40,width=210)

        ###---------STATUS -----------
        utype_Eemp=Entry(s.root,textvariable=s.var_status,font=("times new roman" ,15),fg="black",bg="white",bd=4)
        utype_Eemp.place(x=281,y=390,height=40,width=210)

         ##3 PAssword +++++++++
        pwd_Estud=Entry(s.root,textvariable=s.var_pwd,font=("times new roman" ,15),fg="black",bg="white",bd=4)
        pwd_Estud.place(x=771,y=390,height=40,width=210)
       #+++++++++++ BUTTON +++++++++++++++++  
        add_stud=Button(s.root,text="UPDATE",command=s.updates,font=("times new roman" ,15),bg="#b33c00",fg="black",bd=4)
        add_stud.place(x=61,y=450,height=40,width=110)

        clear_stud=Button(s.root,text="CLEAR",command=s.clear,font=("times new roman" ,15),bg="#b33c00",fg="black",bd=4)
        clear_stud.place(x=281,y=450,height=40,width=110)




    # ++++++++++++++ TRE VIEW ++++++++++++++++++
        st=ttk.Style()
        st.theme_use("clam")
        

        
        view_emp=Frame(s.root,bd=3,relief=RIDGE)
        view_emp.place(x=200,y=540,width=1200,height=280)

        scrolly=Scrollbar(view_emp,orient=VERTICAL)
        scrollx=Scrollbar(view_emp,orient=HORIZONTAL)


        s.studentTable=ttk.Treeview(view_emp,columns=("stud_id","name","dob","mobileno","email","company","status","password"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        
        scrollx.config(command=s.studentTable.xview)
        scrolly.config(command=s.studentTable.yview)
        
        
        
        s.studentTable.heading("stud_id",text="stud_id")
        s.studentTable.heading("name",text="NAME")
        s.studentTable.heading("dob",text="DOB")
        s.studentTable.heading("mobileno",text="MOBILE NO")
        s.studentTable.heading("email",text="EMAIL")
        s.studentTable.heading("company",text="COMPANY")
        s.studentTable.heading("status",text="STATUS")
        s.studentTable.column("password",width=100)



        s.studentTable["show"]="headings"


        s.studentTable.column("stud_id",width=90)
        s.studentTable.column("name",width=100)
        s.studentTable.column("dob",width=100)
        s.studentTable.column("mobileno",width=100)
        s.studentTable.column("email",width=100)
        s.studentTable.column("company",width=100)
        s.studentTable.column("status",width=100)
        s.studentTable.column("password",width=100)

        s.studentTable.pack(fill=BOTH,expand=1)
        s.studentTable.bind("<ButtonRelease-1>",s.get_data)
        s.show()
        st.configure("Treeview",
                  background="grey",
                  foregroung="#FF2800",
                  rowheight=25,
                  fieldbackground="#997950"
                  )
        st.map("Treeview",background=[("selected","navy")])
        
        

    def show(s):
        con=sqlite3.connect(database=r'student.db')
        cur=con.cursor()
        try:
                
          global c
          c=0
          s.studentTable.tag_configure('oddrow',background="#7C4700")
          s.studentTable.tag_configure('evrow',background="#808588")
          cur.execute("select * from student")
          rows=cur.fetchall()
          s.studentTable.delete(*s.studentTable.get_children())
          for row in rows:
              if c % 2 == 0:
                      s.studentTable.insert('',END,values=row,tags=('oddrow',))
              else:
                      s.studentTable.insert('',END,values=row,tags=('evrow',))
              c +=1
          
        except Exception as ex:
            ms.showerror("Error",f"Error due to :{(str(ex))}",parent=s.root)





    def updates(s):
        con=sqlite3.connect(database=r'student.db')
        cur=con.cursor()
        try:
            if s.var_stud_id.get()=="":
                ms.showerror("Error","stud_id must be required ",parent=s.root)
            else:
                cur.execute("Select * from student where stud_id=?",(s.var_stud_id.get(),))
                row=cur.fetchone()
                if row ==None:
                    ms.showerror("Error","This stud_id is new please use the ADD module ",parent=s.root)
                else:
                    print(3)
                    cur.execute("Update  student set name=?,dob=?,mobileno=?,email=?,company=?,status=?,password=?  where stud_id=?",(
                        s.var_name.get(),
                        s.var_dob.get(),
                        s.var_mobileno.get(),
                        s.var_email.get(),
                        s.var_company.get(),
                        s.var_status.get(),
                        s.var_pwd.get(),
                        s.var_stud_id.get()
                       

                    ))
                    con.commit()
                    ms.showinfo("Success","Employee added successfully",parent=s.root)
                    print("done")
                    s.show()                    
                   
        except Exception as ex:
            ms.showerror("Error",f"Error due to :{(str(ex))}",parent=s.root)

    ###### ++++++++ get data ++++++++++
    def  get_data(s,ev):
        f=s.studentTable.focus()
        content=s.studentTable.item(f)
        print(content)
        row=content['values']
        print(row)
        s.var_stud_id.set(row[0])
        s.var_name.set(row[1])
        s.var_dob.set(row[2])
        s.var_mobileno.set(row[3])
        s.var_email.set(row[4])
        s.var_company.set(row[5])
        s.var_status.set(row[6])
        s.var_pwd.set(row[7])

    ########### search +++++++
    def search1(self):
        con=sqlite3.connect(database=r'student.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="select":
                ms.showerror("Error","select the option  ",parent=self.root)
            elif   self.var_search.get()=="":
                ms.showerror("Error","search input should be required ",parent=self.root)
            else:
                cur.execute("Select * from student where  "+self.var_searchby.get()+" LIKE '%"+self.var_search.get()+ "%' ")
                print(8)
                ro=cur.fetchall()
                if len(ro)!=0:
                    print(33)
                    self.studentTable.delete(*self.studentTable.get_children())
                    for row in ro:
                        self.studentTable.insert('',END,values=row)
                else:
                    ms.showerror("Error","No record found",parent=self.root)

        except Exception as ex:
             ms.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root) 
        
    ####### ++++++  clear +++++++++++
    def clear(s):
        s.var_searchby.set("select")
        s.var_search.set("")
        s.var_stud_id.set("")
        s.var_name.set("")
        s.var_dob.set("")
        s.var_mobileno.set("")
        s.var_email.set("")
        s.var_company.set("")
        s.var_status.set("")
        s.var_pwd.set("")

        s.show()


if  __name__=="__main__":
     root=Tk()
     obj=upd(root)
     root.mainloop()
