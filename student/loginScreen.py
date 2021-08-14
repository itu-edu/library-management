from bookHome import *

root = Tk()
root.title("Library")
root.minsize(width=400, height=400)
root.geometry("600x500")
count = 0
empFrameCount = 0
Canvas1 = Canvas(root)

headingFrame1 = Frame(root, bg="green", bd=2)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

headingLabel = Label(headingFrame2, text="Python Project : Library Management", fg='black')
headingLabel.place(relx=0.02, rely=0.1, relwidth=0.96, relheight=0.5)


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
        e_text = en4.get()
        print(e_text)

        print('student selected')
        manageBookOperations()

    elif role == 'librarian':
        # if credentials matches from the databse with user role, open librarian menu options
        # add book, view book, search book, view all books, view status for availability
        print('librarian or something else selected')

def UserLogin():
    global headingFrame1, headingFrame2, headingLabel, btn1, btn1, Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()

    Canvas1 = Canvas(root)

    headingFrame1 = Frame(root, bg="green", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
    headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

    headingLabel = Label(headingFrame2, text="Welcome to Login Screen", fg='black')
    headingLabel.place(relx=0.02, rely=0.1, relwidth=0.96, relheight=0.5)

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
    entry2.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Role
    lb4 = Label(labelFrame, text="Role : ", bg='white', fg='black')
    lb4.place(relx=0.05, rely=0.7)

    en4 = Entry(labelFrame)
    en4.place(relx=0.3, rely=0.7, relwidth=0.62)

    btn2 = Button(root, text="Quit", bg='#455A64', fg='black', command=root.quit)
    btn2.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    enter_button2 = Button(text="Enter", bg='#264348', fg='blue', command=lambda: validate())
    enter_button2.place(relx=0.75, rely=0.9, relwidth=0.18, relheight=0.08)


btn1 = Button(root, text="User Login", bg='green', fg='black', command=UserLogin)
btn1.place(relx=0.40, rely=0.3, relwidth=0.2, relheight=0.1)

UserLogin()
root.mainloop()
