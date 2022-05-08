from tkinter import*
from tkinter import ttk,messagebox
import  sqlite3
class PRO:
    def    __init__(self,root):
            self.root=root
            view_p=Frame(self.root,bd=3,relief=RIDGE)
            view_p.place(x=510,y=630,relwidth=1,height=500)
            
            
            scrolly=Scrollbar(view_p,orient=VERTICAL)
            scrollx=Scrollbar(view_p,orient=HORIZONTAL)
            
            
            self.ProductTable=ttk.Treeview(view_p,columns=("useri_id","name","doj","mobileno","password","utype"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            scrollx.pack(side=BOTTOM,fill=X)
            scrolly.pack(side=RIGHT,fill=Y)
            
            scrollx.config(command=self.ProductTable.xview)
            scrolly.config(command=self.ProductTable.yview)
            
            
            
            self.ProductTable.heading("useri_id",text="USER_ID")
            self.ProductTable.heading("name",text="NAME")
            self.ProductTable.heading("doj",text="DOJ")
            self.ProductTable.heading("mobileno",text="MOBILE NO")
            self.ProductTable.heading("password",text="PASSWORD")
            self.ProductTable.heading("utype",text="USER TYPE")
            
            
            
            self.ProductTable["show"]="headings"

        















if  __name__=="__main__":
     root=Tk()
     obj=PRO(root)
     root.mainloop()
    
