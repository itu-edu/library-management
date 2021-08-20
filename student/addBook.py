from tkinter import *
from tkinter import messagebox
from db import *

conn = sqlite3.connect('library_info.db')
cursor = conn.cursor()


def add_db():
    global id
    global title
    global author

    btitle = title.get()
    bauthor = author.get()

    print(btitle, end='--')
    print(bauthor, end='--')
    print("add")

    try:
        cursor.execute('''INSERT INTO Books(Title, Author, Status, User_id )
                                       VALUES(?, ?, ?, ?)''', (btitle, bauthor, "available", 1))

        conn.commit()

        messagebox.showinfo('Success', btitle+" added.")

    except:
        messagebox.showerror("Error", "Could not add given book data into Database!")

    window.destroy()


def addBooks():
    global window
    global title
    global author

    window = Tk()
    window.title('Library Management System - Add a Book')
    window.minsize(width=400, height=400)
    window.geometry("450x400")

    headingFrame1 = Frame(window, bg="green", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
    headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

    headingLabel = Label(headingFrame2, text="Add new Book", fg='black')
    headingLabel.place(relx=0.02, rely=0.2, relwidth=0.96, relheight=0.5)

    # ----------title-------------------

    L = Label(window, text="Enter Title: ")
    L.place(relx=0.05, rely=0.4)

    title = Entry(window, width=5)
    title.place(relx=0.3, rely=0.4, relwidth=0.62,relheight=0.07)

    # ----------author-------------------

    L = Label(window, text="Enter Author: ")
    L.place(relx=0.05, rely=0.5)

    author = Entry(window, width=5)
    author.place(relx=0.3, rely=0.5, relwidth=0.62,relheight=0.07)

    submitbtn = Button(window, text="Add", command=add_db, bg="#455A64", fg="white")
    submitbtn.place(relx=0.6, rely=0.7, relwidth=0.30, relheight=0.08)

    print("add")
