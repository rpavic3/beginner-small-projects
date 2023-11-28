from tkinter import *


root = Tk()
root.geometry('300x200')

Label(root,text="gay", bg="green").pack(ipadx=10, ipady=10,fill=BOTH, expand=True, side=LEFT)
Label(root,text="bray", bg="red").pack(ipadx=10,fill=BOTH, expand=True, side=RIGHT)

root.mainloop()
