from tkinter import *
from tkinter import messagebox
from db import *


def close():
    window.destroy()

def viewBooks():
    global window

    window = Tk()
    window.title('Library Management System')
    window.minsize(width=400, height=400)
    window.geometry("600x500")

    greet = Label(window, font=('arial', 30, 'bold'), text="View Books")
    greet.grid(row=0, columnspan=3)

    submitbtn = Button(window, text="Close", bg="DodgerBlue2", fg="black", font=('arial', 15, 'bold'), command=close)
    submitbtn.place(relx=0.3, rely=0.9, relwidth=0.62)


    try:
        conn = None
        conn = sqlite3.connect('library_info.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Books')
        results = cur.fetchall()
        for row in results:
            print(f'Results: {row[0]}{row[1]}{row[2]}{row[3]}{row[4]}')

        L = Label(window, font=('arial', 15),
                  text="%-10s%-20s%-20s%-20s%-20s" % ('BID', 'Title', 'Author', 'Available', 'AssignedTo'))
        L.grid(row=1, columnspan=5)

        L = Label(window, font=('arial', 15), text="----------------------------------------------------------------")
        L.grid(row=2, columnspan=5)

        x = 5
        for i in results:
            L = Label(window, font=('arial', 15), text="%-10s%-20s%-20s%-20s%-20s" % (i[0], i[1], i[2], i[3], i[4]))
            L.grid(row=x, columnspan=5)
            x += 1

    except:
        messagebox.showinfo("Error", "Cannot Fetch data.")

    finally:
        if conn != None:
            conn.close()

    print("view")