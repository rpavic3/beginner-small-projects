from tkinter import *
from tkinter import ttk
from tkinter import font

root = Tk()
root.geometry('300x200')
def download_clicked():
    showinfo(
        title='Information',
        message='Download button clicked!'
    )


download_icon = PhotoImage(file='d:/Programming/My Python projects/tkinter tutorial/auto.png')

download_button = ttk.Button(
    root,
    image=download_icon,
    text='Download',
    compound=LEFT,
    command=download_clicked
)

download_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()
