from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox
import csv

import random

master = Tk()
master.title("Window Title")
master.geometry("250x130")
master.configure(background='seagreen')
master.resizable(False,False)


class SlotMachineGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Slot Machine Game")

        self.symbols = ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar", "Seven"]

        self.reels = [[StringVar(), StringVar(), StringVar()],
                      [StringVar(), StringVar(), StringVar()],
                      [StringVar(), StringVar(), StringVar()]]

        self.result_text = StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Display reels
        for i in range(3):
            for j in range(3):
                label = Label(self.root, textvariable=self.reels[i][j], width=8)
                label.grid(row=i, column=j, padx=5, pady=5)

        # Result label
        result_label = Label(self.root, textvariable=self.result_text)
        result_label.grid(row=3, column=0, columnspan=3, pady=10)

        # Spin button
        spin_button = Button(self.root, text="Spin", command=self.spin_reels)
        spin_button.grid(row=4, column=1, pady=10)

    def spin_reels(self):
        # Spin reels and update labels
        result = []
        for i in range(3):
            row_symbols = []
            for j in range(3):
                symbol = random.choice(self.symbols)
                self.reels[i][j].set(symbol)
                row_symbols.append(symbol)
            result.append(" ".join(row_symbols))

        # Check for winning combination
        if self.check_winning():
            messagebox.showinfo("Congratulations!", "You won!")
        else:
            messagebox.showinfo("Sorry", "You didn't win this time.")

        # Update result label
        self.result_text.set("Result: " + " | ".join(result))

    def check_winning(self):
        # Check for winning combinations
        for i in range(3):
            if all(self.reels[i][j].get() == self.reels[i][0].get() for j in range(1, 3)):
                return True

        for j in range(3):
            if all(self.reels[i][j].get() == self.reels[0][j].get() for i in range(1, 3)):
                return True

        if all(self.reels[i][i].get() == self.reels[0][0].get() for i in range(1, 3)):
            return True

        if all(self.reels[i][2 - i].get() == self.reels[0][2].get() for i in range(1, 3)):
            return True

        return False


#################################
def read_user_data():
    try:
        with open('user_data.csv', 'r') as file:
            reader = csv.reader(file)
            user_data = {rows[0]: rows[1] for rows in reader}
    except FileNotFoundError:
        user_data = {}
    return user_data

def write_user_data(user_data):
    with open('user_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for username, password in user_data.items():
            writer.writerow([username, password])

#################################
             

###########################################
def validate_login(username, password):
    user_data = read_user_data()
    if username in user_data and user_data[username] == password:
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


######################################
def newpass():
    username = username_entry.get()
    new_password = new_password_entry.get()
    user_data = read_user_data()
    user_data[username] = new_password
    write_user_data(user_data)
    messagebox.showinfo("","Password changed successfully!")
    newpass_window.destroy()


def open_newpass_window():
    global newpass_window
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
        user_data = read_user_data()
        user_data[new_username] = new_password
        write_user_data(user_data)
        
        messagebox.showinfo("Signup Successful", "Account created for " + new_username)
        signup_window.destroy()
    else:
        messagebox.showerror("Signup Failed", "Please enter both username and password")

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
#######################################
    
def destroy_and_reopen():
    main_window.destroy()
    mainloop()
    


def open_joc():
    root = Tk()
    slot_machine_gui = SlotMachineGame(root)
    root.mainloop()
#######################################
def open_main_window():
    global main_window
    main_window = Tk()
    main_window.title("Main Window")
    main_window.geometry("500x300")
    main_window.configure(background='seagreen')
    taburi = Notebook(main_window)
    taburi.pack(expand=1,fill="both")
    tab1 = Frame(taburi)
    tab2 = Frame(taburi)

    taburi.add(tab1,text="Home")
    # taburi.add(tab2,text="About")

    joc = Button(tab1, text="Joc", command=open_joc)
    joc.grid(row=5, column=0, pady=10, padx=20)

    change_pass = Button(tab1, text="Change Passsword", command=open_newpass_window)
    change_pass.grid(row=2, column=0, pady=10, padx=20)

    logout = Button(tab1, text = "Logout",command=destroy_and_reopen) 
    logout.grid(row=3, column=0, pady=10, padx=20) 
##########################################

#widgeturi master // puteam folosi place in loc de grid dar este mai mult de umblat la valori

#username
username_label = Label(master, text="Username:",background='seagreen')
username_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
username_entry = Entry(master)
username_entry.grid(row=0, column=1, padx=5, pady=10)

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
