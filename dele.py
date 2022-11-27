from tkinter import*
from PIL import ImageTk,Image
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
#Create SQlite database
import sqlite3

con=sqlite3.connect("try.db")
cur=con.cursor()



def delsql():
    try:
        book_id=delid.get()
        cur.execute("DELETE FROM books WHERE bid=?",(book_id,))
        cur.execute("DELETE FROM issued WHERE bid=?", (book_id,))
        cur.execute("DELETE FROM availed WHERE bid=?", (book_id,))

        con.commit()
        messagebox.showinfo("sucess")
    except:
        messagebox.showinfo("""ERROR : Enter Correct Id""")


def delall():
    ans=messagebox.askyesno("DELETE ALL BOOKS DATA PERMANANTLY ?")
    if ans==YES:
        cur.execute("DELETE FROM BOOKS")
        con.commit()
        messagebox.showinfo("all data removed ")
    else:
        messagebox.showinfo("Books Not DELETED")




def dele():
    global delid
    deletepage=Tk()
    deletepage.minsize(width="100",height="400")
    img=PhotoImage(file="home.png",master=deletepage)
    back_label=Label(deletepage,image=img)
    back_label.place(x=0,y=0)

    delframe=Frame(deletepage,bg="black")
    delframe.place(relx="0.1",rely="0.1",relheight="0.8",relwidth="0.8")

    messegelabel=Label(delframe,text="ENTER BOOK ID IN BOX",bg="black",fg="white")
    messegelabel.place(relwidth="0.8",relheight="0.2",relx="0.1",rely="0.1")
    delid=Entry(delframe)
    delid.place(relheight="0.05",relwidth="0.8",relx="0.1",rely=0.3)


    submitbutton=Button(delframe,text="DELETE",bg="white",fg="black",command=delsql)
    submitbutton.place(relwidth="0.3",relheight="0.08",relx="0.2",rely="0.5")

    quitbutton=Button(delframe,text="CANCEL",bg="white",fg="black",command=deletepage.destroy)
    quitbutton.place(relwidth="0.3",relheight="0.08",relx="0.6",rely="0.5")

    delete_all=Button(delframe,bg="white",fg="black",text="delete all books",command=delall)
    delete_all.place(relheight=0.1,relwidth=0.3,relx=0.4,rely=0.8)


    deletepage.mainloop()
