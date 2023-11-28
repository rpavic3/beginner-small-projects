from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Login')
#root.geometry("350x220")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

username_label = ttk.Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=E, padx=5, pady=5)

# password
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=W, padx=5, pady=5)

password_entry = ttk.Entry(root,  show="*")
password_entry.grid(column=1, row=1, sticky=E, padx=5, pady=5)

# login button
login_button = ttk.Button(root, text="Login")
login_button.grid(column=1, row=3, sticky=E, padx=5, pady=5)

root.mainloop()
