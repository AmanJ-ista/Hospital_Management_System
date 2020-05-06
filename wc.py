from tkinter import *
import mysql.connector
from tkinter import messagebox
def patient():
    global window4
    window4=Tk()
    window4.geometry('1800x1200') 
    window4.title("Hospital Management System")
    frame2=Frame(window4,width=1600,height=54,bg="violet")
    frame2.place(x=0,y=0)
    lb=Label(window4,text="MANAGE PATIENT",bg="violet",font=('calibre',30,'bold'))
    lb.place(x=615,y=0)

    lg=Label(window4,text="NAME",font=('calibre',20,'bold'))
    lg.place(x=280,y=200)
    
    lh=Label(window4,text="GENDER",font=('calibre',20,'bold'))
    lh.place(x=280,y=250)

    li=Label(window4,text="CONTACT",font=('calibre',20,'bold'))
    li.place(x=280,y=300)

    lj=Label(window4,text="ADDRESS",font=('calibre',20,'bold'))
    lj.place(x=280,y=350)

    lk=Label(window4,text="SEARCH",font=('calibre',20,'bold'))
    lk.place(x=1200,y=200)


    global Name,Gender,Contact,Address,Search
    Name=StringVar()
    Gender=StringVar()
    Contact=StringVar()
    Address=StringVar()
    Search=StringVar()
    global ef,eg,eh,ei,ej
   
    ef=Entry(window4,textvar="Name",width=20,font=('calibre',18,'bold'))
    ef.place(x=550,y=200)

    eg=Entry(window4,textvar="Gender",width=20,font=('calibre',18,'bold'))
    eg.place(x=550,y=250)

    eh=Entry(window4,textvar="Contact",width=20,font=('calibre',18,'bold'))
    eh.place(x=550,y=300)


    ei=Entry(window4,textvar="Address",width=20,font=('calibre',18,'bold'))
    ei.place(x=550,y=350)

    ej=Entry(window4,textvar="Search",width=20,font=('calibre',18,'bold'))
    ej.place(x=900,y=200)



    
    bf=Button(window4,text="BACK",bg="orange",font=('calibre',18,'bold'),width=15,command=back)
    bf.place(x=0,y=1)

    bg=Button(window4,text="SUBMIT",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=patient1)
    bg.place(x=300,y=500)

    bh=Button(window4,text="DELETE",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=delete)
    bh.place(x=530,y=500)

    bi=Button(window4,text="SEARCH",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=search)
    bi.place(x=760,y=500)

    bj=Button(window4,text="VIEW",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=show)
    bj.place(x=990,y=500)


def back():
    window4.destroy()

def patient1():
    a=ef.get()
    b=eg.get()
    c=eh.get()
    d=ei.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    sql="INSERT INTO patient(Name,gender,contact,address)VALUES(%s,%s,%s,%s)"
    val=(a,b,c,d)
    cs.execute(sql,val)
    conn.commit()
    cs.close()
    conn.close()
    ef.delete(first=0,last=20)
    eg.delete(first=0,last=20)
    eh.delete(first=0,last=20)
    ei.delete(first=0,last=20)
def show():
    
    window6=Tk()
    window6.geometry('1800x1200')
    tree=ttk.Treeview(window6,column=(1,2,3,4),show="headings",height=30)
    tree.heading(1,text="Name")
    tree.heading(2,text="Gender")
    tree.heading(3,text="Contact")
    tree.heading(4,text="Address")
    tree.place(x=400,y=100)
    frame2=Frame(window6,width=1600,height=54,bg="violet")
    frame2.place(x=0,y=0)
    lb=Label(window6,text="List Of Patient",bg="violet",font=('calibre',30,'bold'))
    lb.place(x=615,y=0)


    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    cs.execute("SELECT * FROM patient")
    rows=cs.fetchall()
    for x in rows:
        tree.insert('','end',values=x)
        
        

def delete():
    messagebox.askquestion("Confirmation","Are you sure want to delete?")
    b=ef.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    sql="DELETE FROM patient WHERE Name=%s"
    val=(b,)
    cs.execute(sql,val)     
    conn.commit()
    cs.close()
    conn.close() 
    
def search():
    s=ej.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    sql="SELECT * FROM patient WHERE Name=%s "
    val=(s,)
    cs.execute(sql,val)
    rows=cs.fetchall()
    for x in rows:
        a=x[0]
        b=x[1]
        c=x[2]
        d=x[3]
    if s==a:
        ef.insert(0,a)
        eg.insert(0,b)
        eh.insert(0,c)
        ei.insert(0,d)

    ej.delete(first=0,last=20)

















