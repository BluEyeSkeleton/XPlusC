# XPlusC
# A Python program created by TeamX+C.
# Generates integration questions and verify answer input from the user.

# IMPORT LIBRARIES
import tkinter
from tkinter import messagebox
from tkinter import *
import storage
import string


# GLOBAL VARIABLES
window = tkinter.Tk()
window2 = tkinter.Tk()
window2.withdraw()

# BASIC FUNCTIONS

# Forgets a widget
def forget(e): 
    e.forget()


# Sends a message to the user
def msg(title, message):
    tmp = tkinter.Tk()
    tmp.withdraw()
    messagebox.showinfo(title, message)

# Checks student ID validity
def checkID(sid):
    if sid.startswith("D") and len(sid) == 5:
        return True
    return False


# FUNCTIONS

def loginPage():
    global window

    # Login Page: Event Listeners
    def onRegisterButtonClicked():
        print("")
    def onLoginButtonClicked():
        sid = entry1.get()
        pwd = entry2.get()
        if storage.login(sid, pwd) == 0:
            if sid == "admin":
                adminMainPage()
            mainPage(sid)
            
        elif storage.login(sid, pwd) == 1:
            msg("Warning", "The student ID doesn't exist.")
            
        elif storage.login(sid, pwd) == 2:
            msg("Warning", "Your password is incorrect.")

    window.withdraw()
    window = tkinter.Tk()
    window.title("School Management System")
    window.geometry("640x480")
    window.resizable(False, False)
    label1 = Label(window, text="Chung Ling High School", font=("Arial Bold", 24))
    label1.place(anchor=N, relx=0.5, rely=0.01)
    label2 = Label(window, text="SCHOOL MANAGEMENT SYSTEM", font=("Arial", 16))
    label2.place(anchor=N, relx=0.5, rely=0.11)
    label3 = Label(window, text="Student ID:", font=("Arial Unicode MS", 16))
    label3.place(anchor=W, relx=0.11, rely=0.31)
    entry1 = Entry(window, font=("Arial Unicode MS", 14), width=32)
    entry1.place(anchor=E, relx=0.89, rely=0.31)
    label4 = Label(window, text="Password:", font=("Arial Unicode MS", 16))
    label4.place(anchor=W, relx=0.11, rely=0.41)
    entry2 = Entry(window, font=("Arial Unicode MS", 14), show="•", width=32)
    entry2.place(anchor=E, relx=0.89, rely=0.41)
    button1 = Button(window, text="I don't have an account", command=onRegisterButtonClicked, font=("Arial Unicode MS", 12), width=32, height=2)
    button1.place(anchor=W, relx=0.11, rely=0.61)
    button2 = Button(window, text="Login", command=onLoginButtonClicked, font=("Arial Unicode MS", 12), width=16, height=2)
    button2.place(anchor=E, relx=0.89, rely=0.61)
    window.mainloop()

def mainPage(sid):
    global window

    # Main Page: Event Listener
    def onLogOutButtonClicked():
        storage.logout()
        msg("Info", "Successfully logged out.")
        loginPage()
    def onExamButtonClicked():
        window.withdraw()
        examPage(sid)

    window.withdraw()
    window = tkinter.Tk()
    window.title("School Management System")
    window.geometry("640x480")
    window.resizable(False, False)
    label1 = Label(window, text="Chung Ling High School", font=("Arial Bold", 24))
    label1.place(anchor=N, relx=0.5, rely=0.01)
    label2 = Label(window, text="SCHOOL MANAGEMENT SYSTEM", font=("Arial", 16))
    label2.place(anchor=N, relx=0.5, rely=0.11)
    label3 = Label(window, text="Student Name: " + storage.getName() + "            Class: " + storage.getClass(), font=("Arial Unicode MS", 12))
    label3.place(anchor=W, relx=0.01, rely=0.21)
    button1 = Button(window, text="Log Out", command=onLogOutButtonClicked, font=("Arial Unicode MS", 8))
    button1.place(anchor=E, relx=0.99, rely=0.21)
    frame1 = Frame(window)
    frame1.place(anchor=N, relx=0.5, rely=0.31)
    button2 = Button(frame1, text="Check exam result", command=onExamButtonClicked, font=("Arial Unicode MS", 16))
    button2.grid(row=0, column=0, pady=3)
    button3 = Button(frame1, text="Check cocurriculum info", font=("Arial Unicode MS", 16))
    button3.grid(row=1, column=0, pady=3)
    button4 = Button(frame1, text="Change password", font=("Arial Unicode MS", 16))
    button4.grid(row=2, column=0, pady=3)
    window.mainloop()

def examPage(sid):
    global window2

    # Main Page: Event Listener
    def onBackButtonClicked():
        window2.withdraw()
        mainPage(sid)

    window2 = tkinter.Tk()
    window2.title("School Management System")
    window2.geometry("640x480")
    window2.resizable(False, False)
    label1 = Label(window2, text="Chung Ling High School", font=("Arial Bold", 24))
    label1.place(anchor=N, relx=0.5, rely=0.01)
    label2 = Label(window2, text="SCHOOL MANAGEMENT SYSTEM", font=("Arial", 16))
    label2.place(anchor=N, relx=0.5, rely=0.11)
    label3 = Label(window2, text="Student Name: " + storage.getName() + "            Class: " + storage.getClass(), font=("Arial Unicode MS", 12))
    label3.place(anchor=W, relx=0.01, rely=0.21)
    button1 = Button(window2, text="Back", command=onBackButtonClicked, font=("Arial Unicode MS", 8))
    button1.place(anchor=E, relx=0.99, rely=0.21)
    frame1 = Frame(window2)
    frame1.place(anchor=N, relx=0.5, rely=0.26)
    label4 = Label(frame1, text="First Test", font=("Arial", 12))
    label4.grid(row=0, column=1, padx=32)
    label5 = Label(frame1, text="First Exam", font=("Arial", 12))
    label5.grid(row=0, column=2, padx=32)
    label6 = Label(frame1, text="Second Test", font=("Arial", 12))
    label6.grid(row=0, column=3, padx=32)
    label7 = Label(frame1, text="Final Exam", font=("Arial", 12))
    label7.grid(row=0, column=4, padx=32)
    label8 = Label(frame1, text="BC", font=("Arial", 12))
    label8.grid(row=1, column=0, pady=1)
    label9 = Label(frame1, text="BM", font=("Arial", 12))
    label9.grid(row=2, column=0, pady=1)
    label10 = Label(frame1, text="BI", font=("Arial", 12))
    label10.grid(row=3, column=0, pady=1)
    label11 = Label(frame1, text="MM", font=("Arial", 12))
    label11.grid(row=4, column=0, pady=1)
    label12 = Label(frame1, text="SC", font=("Arial", 12))
    label12.grid(row=5, column=0, pady=1)
    label13 = Label(frame1, text="ASK", font=("Arial", 12))
    label13.grid(row=6, column=0, pady=1)
    label14 = Label(frame1, text="SJ", font=("Arial", 12))
    label14.grid(row=7, column=0, pady=1)
    label15 = Label(frame1, text="GE", font=("Arial", 12))
    label15.grid(row=8, column=0, pady=1)
    label16 = Label(frame1, text="PM", font=("Arial", 12))
    label16.grid(row=9, column=0, pady=1)
    label17 = Label(frame1, text="PJK", font=("Arial", 12))
    label17.grid(row=10, column=0, pady=1)
    label18 = Label(frame1, text="PSV", font=("Arial", 12))
    label18.grid(row=11, column=0, pady=1)
    result = storage.getExamResult()
    for x in range(9):
        labelResult = Label(frame1, text=result[x], font=("Arial", 12))
        labelResult.grid(row=x + 1, column=1, padx=32, pady=3)
    for x in range(11):
        labelResult = Label(frame1, text=result[x + 9], font=("Arial", 12))
        labelResult.grid(row=x + 1, column=2, padx=32, pady=3)
    for x in range(9):
        labelResult = Label(frame1, text=result[x + 20], font=("Arial", 12))
        labelResult.grid(row=x + 1, column=3, padx=32, pady=3)
    for x in range(11):
        labelResult = Label(frame1, text=result[x + 29], font=("Arial", 12))
        labelResult.grid(row=x + 1, column=4, padx=32, pady=3)
    window2.mainloop()

def adminMainPage():
    global window

    # Admin Main Page: Event Listener
    def onLogOutButtonClicked():
        print("")
    
    window.withdraw()
    window = tkinter.Tk()
    window.title("School Management System")
    window.geometry("640x480")
    window.resizable(False, False)
    label1 = Label(window, text="Chung Ling High School", font=("Arial Bold", 24))
    label1.place(anchor=N, relx=0.5, rely=0.01)
    label2 = Label(window, text="SCHOOL MANAGEMENT SYSTEM", font=("Arial", 16))
    label2.place(anchor=N, relx=0.5, rely=0.11)
    label3 = Label(window, text="Current User: admin", font=("Arial Unicode MS", 12))
    label3.place(anchor=W, relx=0.01, rely=0.21)
    button1 = Button(window, text="Log Out", command=onLogOutButtonClicked, font=("Arial Unicode MS", 8))
    button1.place(anchor=E, relx=0.99, rely=0.21)
    window.mainloop()
    

# SCRIPT
storage.init("data/")
loginPage()