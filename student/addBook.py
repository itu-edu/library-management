from tkinter import *
from tkinter import messagebox
import sqlite3


def add_db():
    global id
    global title
    global author

    bid = id.get()
    btitle = title.get()
    bauthor = author.get()

    # db = sqlite3.connector.connect(host="localhost", user="root", password='your password', database='db')
    # cursor = db.cursor()

    print(bid, end='--')
    print(btitle, end='--')
    print(bauthor, end='--')
    print("add")

    # sqlquery = "insert into books values('" + bid + "','" + btitle + "','" + bauthor + "','YES');"
    # print(sqlquery)

    try:
        # cursor.execute(sqlquery)
        # db.commit()
        messagebox.showinfo('Success', "Book added Successfully")

    except:
        messagebox.showinfo("Error", "Cannot add given book data into Database")

    # window.destroy()


def addBooks():
    global id
    global title
    global author

    window = Tk()
    window.title('Library Management')
    window.minsize(width=400, height=400)
    window.geometry("600x600")

    headingFrame1 = Frame(window, bg="green", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
    headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

    headingLabel = Label(headingFrame2, text="Add Books", fg='black')
    headingLabel.place(relx=0.02, rely=0.1, relwidth=0.96, relheight=0.5)

    # ----------id-------------------

    L = Label(window, font=('arial', 15, 'bold'), text="Enter Book id: ")
    L.place(relx=0.05, rely=0.3)

    # L = Label(window, font=('arial', 15, 'bold'), text="   ")
    # L.grid(row=2, column=2)

    id = Entry(window, width=5, font=('arial', 15, 'bold'))
    id.place(relx=0.3, rely=0.3, relwidth=0.62)

    # ----------title-------------------

    L = Label(window, font=('arial', 15, 'bold'), text="Enter Title: ")
    L.place(relx=0.05, rely=0.5)

    # L = Label(window, font=('arial', 15, 'bold'), text="   ")
    # L.grid(row=4, column=2)

    title = Entry(window, width=5, font=('arial', 15, 'bold'))
    title.place(relx=0.3, rely=0.5, relwidth=0.62)

    # ----------author-------------------

    L = Label(window, font=('arial', 15, 'bold'), text="Enter Author: ")
    L.place(relx=0.05, rely=0.7)

    # L = Label(window, font=('arial', 15, 'bold'), text="   ")
    # L.grid(row=6, column=2)

    author = Entry(window, width=5, font=('arial', 15, 'bold'))
    author.place(relx=0.3, rely=0.7, relwidth=0.62)

    submitbtn = Button(window, text="Submit", command=add_db, bg="DodgerBlue2", fg="black", font=('arial', 15, 'bold'))
    submitbtn.place(relx=0.3, rely=0.9, relwidth=0.62)

    print("add")
    pass
