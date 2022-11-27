from tkinter import*
from PIL import ImageTk,Image
from tkinter import *
from PIL import ImageTk
#Create SQlite database
import sqlite3
from tkinter import messagebox

con=sqlite3.connect("try.db")
cur=con.cursor()
def search():
    book_id=search_entry.get()
    cur.execute("""SELECT* FROM books WHERE bid=?""",(book_id,))
    i=cur.fetchone()
    print(i)
    con.commit()
    if i==None:
        messagebox.showerror("check id")
    else:
        result=i[3]
        messagebox.askokcancel(result)


def viewwindow():
    global search_entry
    view=Tk()
    view.minsize(height="400",width="400")
    img=PhotoImage(file="home.png",master=view)
    back_label=Label(view,image=img)
    back_label.place(x="0",y="30")

    headlabel = Label(view, text="Books Available ", bg='black', fg='white', font=('Courier', 20))
    headlabel.pack()



    table_labelframe=Frame(view,bg="black")
    scrollbar=Scrollbar(table_labelframe,bg="black")

    scrollbar.pack(side=RIGHT,fill=BOTH)



    cur.execute("SELECT* FROM books")
    con.commit()

    Label(table_labelframe, text="%-20s%-40s%-30s%-20s" % ("bid", "title", "author", "status"), bg="black", fg="white").place(
        relx=0.1, rely=0.05)

    #adding line remaining

    y=0.1
    for i in cur:
        print(i)
        print("00000")

        Label(table_labelframe,text="______________________________________________________________________________________",
              bg="black",fg="white").place(relx=0.0,rely=y)
        y=y+0.05
        Label(table_labelframe,text="%-20s%-40s%-30s%-20s"%(i[0],i[1],i[2],i[3]),bg="black",fg="white").place(relx=0.1,rely=y)
        y+=0.05

    table_labelframe.place(rely=0.2,relx=0.2,relheight=0.5,relwidth=0.35)

    status_frame=Frame(view,bg="black")
    status_frame.place(relheight=0.3,relwidth=0.3,relx=0.6,rely=0.2)

    search_label=Label(status_frame,bg="black",text="ENTER BOOK ID TO CHECK STATUS",fg="white")
    search_label.place(relwidth=0.4,relheight=0.1,relx=0.1,rely=0.3)

    search_entry=Entry(status_frame,bg="white")
    search_entry.place(relheight=0.1,relwidth=0.4,relx=0.1,rely=0.5)

    submit_button=Button(status_frame,bg="white",text="SEARCH",command=search)
    submit_button.place(relwidth=0.1,relheight=0.1,relx=0.7,rely=0.8)




    view.mainloop()
