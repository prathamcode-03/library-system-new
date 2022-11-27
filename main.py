from tkinter import*
from PIL import ImageTk,Image
from tkinter import *
from PIL import ImageTk
#Create SQlite database
import sqlite3
import adbook
import view
from dele import *
from adbook import *
from view import*
from issue import*
from returned import*

con=sqlite3.connect("try.db")
cur=con.cursor()

win = Tk()
win.minsize(height=1000,width=100)
win.maxsize(height='900',width="1550")

#Define the PhotoImage Constructor by passing the image file
img= PhotoImage(file="home.png", master= win)
img_label= Label(win,image=img)

#define the position of the image
img_label.place(x=0, y=0,width="1550",height="900")

#Heading with the help of Headframe
headlabel=Label(win, text="Welcome TO BING-BOOKS ",bg="LightSkyBlue2" ,fg='black', font=('Courier',20))
headlabel.pack()

#ADDING BUTTONS

btn1 = Button(win, text="Add Book Details",bg="black", fg='white',command=addwindow)
btn1.place(relx=0.28, rely=0.2, relwidth=0.45, relheight=0.1)

btn2 = Button(win, text="Delete Book", bg='black', fg='white',command=dele)
btn2.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

btn3 = Button(win, text="View Book List", bg='black', fg='white',command=viewwindow )
btn3.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn4 = Button(win, text="Issue Book to Student", bg='black', fg='white',command=issue)
btn4.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn5 = Button(win, text="Return Book", bg='black', fg='white',command=returned)
btn5.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

win.mainloop()