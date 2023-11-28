from tkinter import *
from tkinter import ttk
from tkinter import font

root = Tk()
#root.geometry('300x200')

root.title('Label Widget Demo')
photo = PhotoImage(file='d:/Programming/My Python projects/tkinter tutorial/auto.png')
# show a label
label = ttk.Label(root, text='This is a label', image=photo, compound="text")
label.pack(ipadx=10, ipady=10)

root.mainloop()
