import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(user_id INTEGER PRIMARY KEY ,name text,doj text,mobileno text,password text,utype text)")
    con.commit()



    cur.execute("CREATE TABLE IF NOT EXISTS supplier(id INTEGER PRIMARY KEY ,name text ,mobile_no INTEGER)")
    con.commit()


    cur.execute("CREATE TABLE IF NOT EXISTS  product(prod_no INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL, category text NOT NULL, id  INTEGER NOT NULL,item_no INTEGER NOT NULL,item_name INTEGER NOT NULL,price INTEGER NOT NULL,iqty INTEGER NOT NULL,status TEXT NOT NULL)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS admin(aid INTEGER PRIMARY KEY  ,name TEXT ,password INTEGER )")
    con.commit()

    #cur.execute("Insert into admin (aid,name,password) values(?,?,?)",(1,"rama",111))
    #con.commit()
    #cur.execute("Insert into adm(aid,name,password) values(?,?,?)",(4,"ram",111))
    #con.commit()

    

    


create_db()    
