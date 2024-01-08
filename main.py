from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox

master = Tk()
master.title("Window Title")
master.geometry("250x130")
master.configure(background='seagreen')
#master.resizable(False,False)

# BD parole eventual

users = {
    "1": "1",
    "user456": "pass456",
    "user789": "pass789"
}

#functii

def validate_login(username, password):
    # Check if the entered username exists and the password matches
    if username in users and users[username] == password:
        return True
    else:
        return False

def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if validate_login(entered_username, entered_password):
        messagebox.showinfo("Login Successful", "Welcome, " + entered_username + "!")
        open_main_window()
        master.destroy()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


    ######################################
def newpass():
    username = username_entry.get()
    new_password = new_password_entry.get()
    users[username] = new_password
    messagebox.showinfo("","Password changed successfully!")
    newpass_window.destroy()


def open_newpass_window():
    global newpass_window
    #newpass_window = Toplevel(background='seagreen')
    newpass_window = Tk()
    newpass_window.configure(background='seagreen')
    newpass_window.title("Change Password")

    username_label = Label(newpass_window, text="Username:",background='seagreen')
    username_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

    global username_entry
    username_entry = Entry(newpass_window)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    new_password_label = Label(newpass_window, text="New Password:",background='seagreen')
    new_password_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

    global new_password_entry
    new_password_entry = Entry(newpass_window, show="*")
    new_password_entry.grid(row=1, column=1, padx=10, pady=10)

    signup_button = Button(newpass_window, text="Change", command=newpass)
    signup_button.grid(row=2, column=0, columnspan=2, pady=10)



#################################################



#################################################    
def signup():
    new_username = new_username_entry.get()
    new_password = new_password_entry.get()

    if new_username and new_password:
        users[new_username] = new_password
        messagebox.showinfo("Signup Successful", "Account created for " + new_username)
        signup_window.destroy()
    else:
        messagebox.showerror("Signup Failed", "Please enter both username and password")

#ferestre

def open_signup_window():
    global signup_window
    signup_window = Toplevel(master,background='seagreen')
    signup_window.title("Signup")

    new_username_label = Label(signup_window, text="New Username:",background='seagreen')
    new_username_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    global new_username_entry
    new_username_entry = Entry(signup_window)
    new_username_entry.grid(row=0, column=1, padx=10, pady=10)

    new_password_label = Label(signup_window, text="New Password:",background='seagreen')
    new_password_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
    global new_password_entry
    new_password_entry = Entry(signup_window, show="*")
    new_password_entry.grid(row=1, column=1, padx=10, pady=10)

    signup_button = Button(signup_window, text="Signup", command=signup)
    signup_button.grid(row=2, column=0, columnspan=2, pady=10)

def open_main_window():

    main_window = Tk()
    main_window.title("Main Window")
    main_window.geometry("500x300")
    main_window.configure(background='seagreen')
    taburi = Notebook(main_window)
    taburi.pack(expand=1,fill="both")
    tab1 = Frame(taburi)
    tab2 = Frame(taburi)

    taburi.add(tab1,text="Home")
    taburi.add(tab2,text="About")

    change_pass = Button(tab1, text="Change Passsword", command=open_newpass_window)
    change_pass.grid(row=2, column=0, pady=10, padx=20)

    logout = Button(tab1, text = "Logout",command = master.mainloop())
    logout.grid(row=3, column=0, pady=10, padx=20)
    
    info = Label(tab2, text="Username: " + user_curent)####################
    username_label = Label(tab2, text="Username:" + user_curent)##################
    username_label.grid(row=1, column=1, padx=5, pady=10)############################


#widgeturi master // puteam folosi place in loc de grid dar este mai mult de umblat la valori
#username
user_curent = ""#########################################
username_label = Label(master, text="Username:",background='seagreen')
username_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
username_entry = Entry(master)
username_entry.grid(row=0, column=1, padx=5, pady=10)
user_curent = username_entry.get()################################################

#parole
password_label = Label(master, text="Password:",background='seagreen')
password_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
password_entry = Entry(master, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=10)

#login
login_button = Button(master, text="Login", command=login)
login_button.grid(row=2, column=0, pady=10, padx=20)

#signup
signup_button = Button(master, text="Signup", command=open_signup_window)
signup_button.grid(row=2, column=1, pady=10, padx=10)

mainloop()