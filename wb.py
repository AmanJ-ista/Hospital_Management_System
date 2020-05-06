
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
def doctor():
    global window3
    window3=Tk()
    window3.geometry('1800x1200') 
    window3.title("Hospital Management System")
    frame2=Frame(window3,width=1600,height=54,bg="violet")
    frame2.place(x=0,y=0)
    lb=Label(window3,text="MANAGE DOCTOR",bg="violet",font=('calibre',30,'bold'))
    lb.place(x=615,y=0)

    lc=Label(window3,text="NAME",font=('calibre',20,'bold'))
    lc.place(x=280,y=200)
    
    ld=Label(window3,text="SPECIALIZATION",font=('calibre',20,'bold'))
    ld.place(x=280,y=250)

    le=Label(window3,text="CONTACT",font=('calibre',20,'bold'))
    le.place(x=280,y=300)

    lf=Label(window3,text="ADDRESS",font=('calibre',20,'bold'))
    lf.place(x=1200,y=200)

    global Name, specialization,contact,address
    Name=StringVar()
    specialization=StringVar()
    contact=StringVar()
    address=StringVar()
    global ea,eb,ec,ed
    ea=Entry(window3,textvar="Name",width=20,font=('calibre',18,'bold'))
    ea.place(x=550,y=200)

    eb=Entry(window3,textvar="specialization",width=20,font=('calibre',18,'bold'))
    eb.place(x=550,y=250)

    ec=Entry(window3,textvar="contact",width=20,font=('calibre',18,'bold'))
    ec.place(x=550,y=300)

    ed=Entry(window3,textvar="address",width=20,font=('calibre',18,'bold'))
    ed.place(x=900,y=200)
 



    
    ba=Button(window3,text="BACK",bg="orange",font=('calibre',18,'bold'),width=15,command=back)
    ba.place(x=0,y=1)

    bb=Button(window3,text="SUBMIT",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=doctor1)
    bb.place(x=300,y=500)

    bc=Button(window3,text="DELETE",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=delete)
    bc.place(x=530,y=500)

    bd=Button(window3,text="UPDATE",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=update)
    bd.place(x=760,y=500)

    be=Button(window3,text="VIEW",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=show)
    be.place(x=990,y=500)
    window3.mainloop()
    
   


def back():
    window3.destroy()




def doctor1():
    a=ea.get()
    b=eb.get()
    c=ec.get()
    d=ed.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    sql="INSERT INTO doctor(name,specialization,contact,address)VALUES(%s,%s,%s,%s)"
    val=(a,b,c,d)
    cs.execute(sql,val)
    conn.commit()
    cs.close()
    conn.close()
    ea.delete(first=0,last=20)
    eb.delete(first=0,last=20)
    ec.delete(first=0,last=20)
    ed.delete(first=0,last=20)


def show():
  
    window6=Tk()
    window6.geometry('1800x1200')
    
    tree=ttk.Treeview(window6,column=(1,2,3,4),show="headings",height=30)
    tree.column("1",width=200)
    tree.column("2",width=200)
    tree.column("3",width=200)
    tree.column("4",width=200)

    tree.heading(1,text="Name")
    tree.heading(2,text="Specialization")
    tree.heading(3,text="Contact")
    tree.heading(4,text="Address")
    tree.place(x=400,y=100)
    frame2=Frame(window6,width=1600,height=54,bg="violet")
    frame2.place(x=0,y=0)
    lb=Label(window6,text="List Of Doctors",bg="violet",font=('calibre',30,'bold'))
    lb.place(x=615,y=0)


    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    cs.execute("SELECT * FROM doctor")
    rows=cs.fetchall()
    for x in rows:
        tree.insert('','end',values=x)
   
        
        

def delete():
    messagebox.askquestion("Confirmation","Are you sure want to delete?")  

    b=ea.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    sql="DELETE FROM doctor WHERE name=%s"
    val=(b,)
    cs.execute(sql,val)     
    conn.commit()
    cs.close()
    conn.close() 
    
 
def update():
    b=ea.get()
    c=ec.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    sql="UPDATE doctor SET contact=%s WHERE name=%s"
    val=(c,b)
    cs.execute(sql,val)
    conn.commit()
    cs.close()
    conn.close()
 






