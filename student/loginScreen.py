from bookHome import *
from db import *
import issueBook
import returnBook
from tkinter import messagebox


connection = sqlite3.connect('library_info.db')
cursor = conn.cursor()

#global root
root = Tk()
root.title("Library Management System - Login")
root.minsize(width=400, height=400)
root.geometry("600x500")
count = 0
empFrameCount = 0


# Canvas1 = Canvas(root)

# headingFrame1 = Frame(root, bg="green", bd=2)
# headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

# headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
# headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

# headingLabel = Label(headingFrame2, text="Python Project : Library Management", fg='black')
# headingLabel.place(relx=0.02, rely=0.1, relwidth=0.96, relheight=0.5)


def currentLogin():
    name = entry1.get()
    password = entry2.get()
    role = en4.get()

    cur.execute('''SELECT User_id FROM Users WHERE Users.Username = ? AND Users.Password = ?''', (name, password))
    result = cur.fetchall()
    for row in result:
        print(f'from login : id {row[0]:<3}')

    return result


def validate():
    print("in validate function 2")
    name = entry1.get()
    password = entry2.get()
    role = en4.get()
    role.lower()
    print(role)

    if role == 'student':
        # need to check credentials, if matches from database then open the student menu options
        # view book, search book, view all books, occupy or release book
        cur.execute('''SELECT * FROM Users WHERE Users.Username = ? AND Users.Password = ?''', (name, password))
        results = cur.fetchall()
        # print(len(results))

        # need to update later, we should have unique values for username and password
        if len(results) == 1:
            print("validation matches and perform book operations")
            cur.execute('''SELECT User_id FROM Users WHERE Users.Username = ? AND Users.Password = ?''',
                        (name, password))
            result = cur.fetchall()

            global logged_in_id
            issueBook.logged_in_id = result
            returnBook.logged_in_id = result

            manageBookOperations()
        else:
            messagebox.showerror("Error", "Invalid Credentials,Please try again!")
            #print("credentials doesn't match, please retry")

    elif role == 'librarian':
        # if credentials matches from the databse with user role, open librarian menu options
        # add book, view book, search book, view all books, view status for availability
        print('librarian or something else selected')

    else:
        messagebox.showerror("Error", "Invalid User")
        #print('invalid user, cannot access')


def UserLogin():
    # global headingFrame1, headingFrame2, headingLabel, btn1, btn1, Canvas1
    # headingFrame1.destroy()
    # headingFrame2.destroy()
    # headingLabel.destroy()
    # Canvas1.destroy()
    # btn1.destroy()

    #Canvas1 = Canvas(root)

    headingFrame1 = Frame(root, bg="green", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
    headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

    headingLabel = Label(headingFrame2, text="Welcome to Library Management", fg='black')
    headingLabel.place(relx=0.02, rely=0.2, relwidth=0.96, relheight=0.5)

    global entry1, entry2, en4, submit_button

    labelFrame = Frame(root, bg='white')
    labelFrame.place(relx=0.2, rely=0.44, relwidth=0.6, relheight=0.3)

    # Name
    label1 = Label(labelFrame, text="User Name : ", bg='white', fg='black')
    label1.place(relx=0.05, rely=0.3)

    entry1 = Entry(labelFrame)
    entry1.place(relx=0.3, rely=0.3, relwidth=0.62)

    # Password
    lable2 = Label(labelFrame, text="Password : ", bg='white', fg='black')
    lable2.place(relx=0.05, rely=0.5)

    entry2 = Entry(labelFrame)
    entry2.config(show="*")
    entry2.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Role
    lb4 = Label(labelFrame, text="Role : ", bg='white', fg='black')
    lb4.place(relx=0.05, rely=0.7)

    en4 = Entry(labelFrame)
    en4.place(relx=0.3, rely=0.7, relwidth=0.62)

    quitbtn2 = Button(root, text="Quit", bg='#455A64', fg='white', command=root.quit)
    quitbtn2.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    enter_button2 = Button(root,text="Login", bg='#455A64', fg='white', command=lambda: validate())
    enter_button2.place(relx=0.75, rely=0.9, relwidth=0.18, relheight=0.08)


# btn1 = Button(root, text="User Login", bg='green', fg='black', command=UserLogin)
# btn1.place(relx=0.40, rely=0.3, relwidth=0.2, relheight=0.1)

UserLogin()
root.mainloop()
