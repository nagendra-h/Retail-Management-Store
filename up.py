from tkinter import*
from tkinter import ttk
from managesup import MSUP
from supview import VSUP



class SUP:
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1140x560+210+130")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="white")
            self.root.focus_force()



            ##### search frame
     #       searc=LabelFrame(self.root,text="Search Employee",font=("times new roman",10,"bold"),bd=2,relief=RIDGE,bg="white")
       #     searc.place(x=250,y=20,width=600,height=70)


            #########option
         #   cmb_search=ttk.Combobox(searc,values=("select","user_id","name"),state="readonly",justify=CENTER,font=("tgoudy old style",10,"bold"))
           # cmb_search.place(x=10,y=10,width=200,height=30)
            #cmb_search.current(0)

            #txtsearch=Entry(searc,font=("tgoudy old style",15,"bold"),bg="lightyellow").place(x=230,y=10,width=200)

            #btsearch=Button(searc,text="search",font=("tgoudy old style",15,"bold"),bg="lightyellow",fg="black").place(x=440,y=10,height=30,width=100)
#-----------------------TITLE---------------------------------------------
            sup_title=Label(self.root,text="SUPPLIER INFORMATION",font=("times new roman",40,"bold"),fg="green",bd=4,relief=RIDGE,padx=20).place(x=0,y=0,relwidth=1,height=60)

   #  button MANAGE AND VIEW
            btn_manage=Button(self.root,text="MANAGE SUPPLIER",command=self.msupplier,font=("times new roman",10,"italic"),bg="black",fg="orange",cursor="hand2").place(x=340,y=70,height=60,width=210)


            btn_view=Button(self.root,text="vVIEW",command=self.vsupplier,font=("times new roman",10,"italic"),bg="black",fg="orange",cursor="hand2").place(x=640,y=70,height=60,width=210)

##----------MANAGE EMP DETAILS -------
        def  msupplier(self):
           self.new_win=Toplevel(self.root)
           self.new_obj=MSUP(self.new_win)

  ##---------VIEWW -------
        def  vsupplier(self):
           self.new_win=Toplevel(self.root)
           self.new_obj=VSUP(self.new_win)
           
           
        

      
            


        


if  __name__=="__main__":
     root=Tk()
     obj=SUP(root)
     #obj1=VSUP(root)
     root.mainloop()
