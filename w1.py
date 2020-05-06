from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox  
window=Tk()
window.geometry('1800x1200')

canvas=Canvas(window,width=1600,height=900)
image1=ImageTk.PhotoImage(Image.open("E:\Python Hyderabad\Python Projects\Hospital management system\hos4121.jpg"))
canvas.create_image(0,50,anchor=NW,image=image1)
canvas.place(x=0,y=50)

window.title("Hospital Management System")
frame=Frame(window,width=1600,height=100,bg="light blue")
frame.place(x=0,y=0)
l1=Label(window,text="HOSPITAL MANAGEMENT SYSTEM",bg="light blue",font=('calibre',40,'bold'))
l1.place(x=330,y=20)

l2=Label(window,text="USERNAME",font=('calibre',30,'bold'),bg="light blue")
l2.place(x=640,y=220)
global user,pwd
global e1,e2
user=StringVar()
pwd=StringVar()
e1=Entry(window,textvar='user',width=20,font=('Helvetica',20,'bold'))
e1.place(x=610,y=290)

l3=Label(window,text="PASSWORD",font=('calibre',30,'bold'),bg="light blue")
l3.place(x=640,y=360)
e2=Entry(window,textvar='pwd',width=20,font=('Helvetica',20,'bold'))
e2.place(x=610,y=430)


from tkinter import *
from wb import doctor
from wc import patient
from wd import appointment
from PIL import Image,ImageTk

def login():
    a=e1.get()
    b=e2.get()
    if a=="aman" and b=="1234":

        window1=Tk()
        window1.geometry('1600x1100')


        
        window1.title("Hospital Management System")
        frame1=Frame(window1,width=1600,height=100,bg="light blue")
        frame1.place(x=0,y=0)
        la=Label(window1,text="ADMIN PANEL",bg="light blue",font=('calibre',35,'bold'))
        la.place(x=620,y=20)


        b1=Button(window1,text="DOCTOR",bg="light blue",bd=15,font=('calibre',18,'bold'),width=15,command=doctor)
        b1.place(x=350,y=280)

        b2=Button(window1,text="PATIENT",bg="light blue",bd=15,font=('calibre',18,'bold'),width=15,command=patient)
        b2.place(x=900,y=280)

        b3=Button(window1,text="APPOINTMENT",bg="light blue",bd=15,font=('calibre',18,'bold'),width=15,command=appointment)
        b3.place(x=350,y=500)

        b4=Button(window1,text="ABOUT US",bg="light blue",bd=15,font=('calibre',18,'bold'),width=15)
        b4.place(x=900,y=500)
        window.destroy()
    else:
        messagebox.showinfo("Information","Your Username and Password is Wrong")  
        

b=Button(window,text="LOGIN",bg="light blue",bd=15,font=('calibre',18,'bold'),width=10,command=login)
b.place(x=660,y=510)











    
