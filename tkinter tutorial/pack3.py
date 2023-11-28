from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Login')
root.geometry("350x220")


fields = {}

fields['username_label'] = ttk.Label(text='Username:')
fields['username'] = ttk.Entry()

fields['password_label'] = ttk.Label(text='Password:')
fields['password'] = ttk.Entry(show="*")


for field in fields.values():
    field.pack(anchor=W, padx=10, pady=5, fill=X)

ttk.Button(text='Login').pack(anchor=W, padx=10, pady=5)

root.mainloop()
