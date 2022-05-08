from tkinter import *
from tkinter import ttk
from tkcalendar import  Calendar,DateEntry
import sqlite3
from tkinter import messagebox as ms


class dels:
    def __init__(s,root):
        s.root=root
        s.root.geometry("1530x850+380+172")
        s.root.title("PLACEMENT MANAGEMENT SYSTEM | MCA STUDENTS")
        s.root.config(bg="white")
        s.root.focus_force()

        ####---------- ALL VARIABLES---
        s.var_searchby=StringVar()
        s.var_search=StringVar()
        s.search=StringVar()  
        s.var_stud_id=StringVar()
        s.var_name=StringVar()


         #++++++++++++ search frame ++++++++++
        searc=LabelFrame(s.root,text="Search Product",font=("times new roman",10,"bold"),bd=2,relief=RIDGE,bg="white")
        searc.place(x=310,y=0,width=800,height=80)

        # ++++++++ options +++++++
        cmb_cat=ttk.Combobox(searc,textvariable=s.var_searchby,values=("Select","stud_id","name"),state="readonly",justify=CENTER,font=("tgoudy old style",10,"bold"))
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

        ###---------ENTRY -----------
        user_Eemp=Entry(s.root,textvariable=s.var_stud_id,font=("times new roman" ,15),bg="white",bd=4)
        user_Eemp.place(x=271,y=190,height=40,width=210)

        ###---------NAME -----------
        nam_Eemp=Entry(s.root,textvariable=s.var_name,font=("times new roman" ,15),bg="white",bd=4)
        nam_Eemp.place(x=771,y=190,height=40,width=210)

        #+++++++++++ BUTTON +++++++++++++++++  
        add_emp=Button(s.root,text="DELETE",command=s.del11,font=("times new roman" ,15),bg="#b33c00",fg="black",bd=4)
        add_emp.place(x=230,y=260,height=40,width=110)

        clear_emp=Button(s.root,text="CLEAR",command=s.clear,font=("times new roman" ,15),bg="#b33c00",fg="black",bd=4)
        clear_emp.place(x=531,y=260,height=40,width=110)
    
    # ++++++++++++++ TRE VIEW ++++++++++++++++++
        st=ttk.Style()
        st.theme_use("clam")
    
        
        view_emp=Frame(s.root,bd=3,relief=RIDGE)
        view_emp.place(x=100,y=340,width=1200,height=280)

        scrolly=Scrollbar(view_emp,orient=VERTICAL)
        scrollx=Scrollbar(view_emp,orient=HORIZONTAL)


        s.studentTable=ttk.Treeview(view_emp,columns=("stud_id","name","dob","mobileno","email","company","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
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



        s.studentTable["show"]="headings"


        s.studentTable.column("stud_id",width=90)
        s.studentTable.column("name",width=100)
        s.studentTable.column("dob",width=100)
        s.studentTable.column("mobileno",width=100)
        s.studentTable.column("email",width=100)
        s.studentTable.column("company",width=100)
        s.studentTable.column("status",width=100)

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
        
        




    def del11(s):
        con=sqlite3.connect(database=r'student.db')
        cur=con.cursor()
        try:
                if s.var_stud_id.get()=="":
                    ms.showerror("Error","stud_id must be required ",parent=s.root)
                else:
                    cur.execute("Select * from student where stud_id=?",(s.var_stud_id.get(),))
                    row=cur.fetchone()
                    if row==None:
                        ms.showerror("Error","INVALID  stud_id  ",parent=s.root)
                    else:
                        op=ms.askyesno("Confirm","Do you really want to delete?",parent=s.root)
                        cur.execute("delete from student where stud_id=?",(s.var_stud_id.get(),))
                        if op==True:
                            con.commit()
                            ms.showinfo("Success","student deleted successfully",parent=s.root)
                            s.show()
        except Exception as ex:
            ms.showerror("Error",f"Error due to :{(str(ex))}",parent=s.root)                    

    
       

        
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





        ###### ++++++++ get data ++++++++++
    def  get_data(s,ev):
        f=s.studentTable.focus()
        content=s.studentTable.item(f)
        row=content['values']
        s.var_stud_id.set(row[0])
        s.var_name.set(row[1])
        
    ########### search +++++++
    def search1(s):
        con=sqlite3.connect(database=r'student.db')
        cur=con.cursor()
        try:
            if s.var_searchby.get()=="select":
                ms.showerror("Error","select the option  ",parent=s.root)
            elif   s.var_search.get()=="":
                ms.showerror("Error","search input should be required ",parent=s.root)
            else:
                cur.execute("Select * from student where  "+s.var_searchby.get()+" LIKE '%"+s.var_search.get()+ "%' ")
                ro=cur.fetchall()
                if len(ro)!=0:
                    s.studentTable.delete(*s.studentTable.get_children())
                    for row in ro:
                        s.studentTable.insert('',END,values=row)
                else:
                    ms.showerror("Error","No record found",parent=s.root)

        except Exception as ex:
             ms.showerror("Error",f"Error due to :{(str(ex))}",parent=s.root) 
        
    ####### ++++++  clear +++++++++++
    def clear(s):
        s.var_searchby.set("select")
        s.var_search.set("")
        s.var_stud_id.set("")
        s.var_name.set("")
        
        s.show()



if  __name__=="__main__":
     root=Tk()
     obj=dels(root)
     root.mainloop()
