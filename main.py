from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox

master = Tk()
master.title("Window Title")
master.geometry("500x300")
master.configure(background='seagreen')

# BD parole eventual

users = {
    "user123": "pass123",
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
    signup_window = Toplevel(master)
    signup_window.title("Signup")

    new_username_label = Label(signup_window, text="New Username:")
    new_username_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    global new_username_entry
    new_username_entry = Entry(signup_window)
    new_username_entry.grid(row=0, column=1, padx=10, pady=10)

    new_password_label = Label(signup_window, text="New Password:")
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




#widgeturi

def center_widget(widget):
    # Get the width and height of the window
    window_width = master.winfo_reqwidth()
    #window_height = master.winfo_reqheight()

    # Get the width and height of the widget
    widget_width = widget.winfo_reqwidth()
    #widget_height = widget.winfo_reqheight()

    # Calculate the x and y coordinates for centering the widget
    x = (window_width - widget_width) // 2
    # y = (window_height - widget_height) // 2

    # Set the widget's position using the grid geometry manager
    widget.grid(row=0, column=0, padx=x)

  
###########################################################################

# l1 = Label(master, text = "Username:",background='seagreen')
# l2 = Label(master, text = "Password:",background='seagreen')

# center_widget(l1)
# center_widget(l2) 

# l1.grid(row = 3, column = 0, sticky = E)
# l2.grid(row = 4, column = 0, sticky = E)
 
# e1 = Entry(master)
# e2 = Entry(master)

# e1.grid(row = 3, column = 1, pady = 0)
# e2.grid(row = 4, column = 1, pady = 0)

# button = Button(master, text='Login', width=25)

username_label = Label(master, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
username_entry = Entry(master)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Password Label and Entry
password_label = Label(master, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
password_entry = Entry(master, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Login Button
login_button = Button(master, text="Login", command=login)
login_button.grid(row=2, column=0, pady=10)

# Signup Button
signup_button = Button(master, text="Signup", command=open_signup_window)
signup_button.grid(row=2, column=1, pady=10)

mainloop()