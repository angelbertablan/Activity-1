import tkinter as tk
from tkinter import messagebox

# A simple in-memory user database
users_db = {}

def sign_up():
    username = entry_username.get()
    password = entry_password.get()
    
    if username in users_db:
        messagebox.showerror("Error", "Username already exists!")
    elif username == "" or password == "":
        messagebox.showerror("Error", "Username and Password cannot be empty!")
    else:
        users_db[username] = password
        messagebox.showinfo("Success", "User  registered successfully!")
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username in users_db and users_db[username] == password:
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password!")

# Create the main window
root = tk.Tk()
root.title("Sign Up / Login Form")

# Create and place the labels and entries for username and password
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)

entry_username = tk.Entry(root)
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Create and place the Sign Up and Login buttons
button_sign_up = tk.Button(root, text="Sign Up", command=sign_up)
button_sign_up.pack(pady=5)

button_login = tk.Button(root, text="Login", command=login)
button_login.pack(pady=5)

# Run the application
root.mainloop()