from tkinter import*
from tkinter import ttk,messagebox
import  sqlite3
import os
from PIL import Image,ImageTk
class bill:
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1140x560+210+130")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="white")
            self.root.focus_force()

            self.var_bill_no=StringVar()

            self.b_list=[]


            #####TITLES==========
            titile=Label(self.root,text="CUSTOMER BILL DETALS",font=("goudy old style",15),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X,padx=10,pady=20)

            lbl_billno=Label(self.root,text="BILL NO:",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=70)


            lbl_billno=Entry(self.root,textvariable=self.var_bill_no,font=("goudy old style",15),bg="white",fg="#0f4d7d").place(x=200,y=70,width=200)

            button_search=Button(self.root,text="search",command=self.search,font=("goudy old style",15,"bold"),cursor="hand2",bg="lightyellow").place(x=460,y=70,width=200)

            button_clear=Button(self.root,text="clear",command=self.clear,font=("goudy old style",15,"bold"),cursor="hand2",bg="lightyellow").place(x=680,y=70,width=200)


            bill_frame=Frame(self.root,bd=3,relief=RIDGE)
            bill_frame.place(x=50,y=140,height=330,width=200)


            scrolly=Scrollbar(bill_frame,orient=VERTICAL)
            self.bill_list=Listbox(bill_frame,font=("goudy old style",15,"bold"))
            scrolly.pack(side=RIGHT,fill=Y)
            scrolly.config(command=self.bill_list.yview)
            self.bill_list.pack(fill=BOTH,expand=1)
            self.bill_list.bind("<ButtonRelease-1>",self.get_data)



            bl_frame=Frame(self.root,bd=3,relief=RIDGE)
            bl_frame.place(x=290,y=140,height=360,width=500)

            b_titile=Label(bl_frame,text="BILL AREA",font=("goudy old style",15),bg="ORANGE",fg="white").pack(side=TOP,fill=X)

            scrolly=Scrollbar(bl_frame,orient=VERTICAL)
            self.bl_list=Listbox(bl_frame,font=("goudy old style",15,"bold"),bg="lightyellow")
            scrolly.pack(side=RIGHT,fill=Y)
            scrolly.config(command=self.bl_list.yview)
            self.bl_list.pack(fill=BOTH,expand=1)

###########IMAGE#########
            b_frame=Frame(self.root,bd=3,relief=RIDGE)
            b_frame.place(x=810,y=140,height=330,width=320)

            self.Logo=Image.open("images/bg.png")
            self.Logo=self.Logo.resize((300,300),Image.ANTIALIAS)
            self.Logo=ImageTk.PhotoImage(self.Logo)

            LeftMenuLogo=Label(b_frame,image=self.Logo)
            LeftMenuLogo.place(x=0,y=0,relwidth=1,height=310)

            self.show()
            


            ######=========

        def show(self):
            del self.b_list[:]
            self.bill_list.delete(0,END)
            for i in os.listdir('bill'):
                if i.split('.')[-1]=='txt':
                    self.bill_list.insert(END,i)
                    self.b_list.append(i.split('.')[0])

        
        def get_data(self,ev):
            index_=self.bill_list.curselection()
            file_name=self.bill_list.get(index_)
            self.bl_list.delete('0',END)
            fp=open(f'bill/{file_name}','r')
            for i in fp:
                self.bl_list.insert(END,i)
            fp.close()

        def search(self):
            if self.var_bill_no.get()=="":
                messagebox.showerror("Error:","Bill no should be requored",parent=self.root)
            else:
                if self.var_bill_no.get() in self.b_list:
                    fp=open(f'bill/{self.var_bill_no.get()}.txt','r')
                    self.bl_list.delete('0',END)
                    for i in fp:
                        self.bl_list.insert(END,i)
                    fp.close()
                else:
                    messagebox.showerror("Error:","Invalid Bill no",parent=self.root)


        def clear(self):
                
            self.show()
            self.var_bill_no.set('')
            self.bl_list.delete('0',END)
                    
            

            


            


            








if  __name__=="__main__":
     root=Tk()
     obj=bill(root)
     root.mainloop()


            
