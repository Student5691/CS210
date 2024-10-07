from tkinter import * # import tkinter

root = Tk() # create the base canvas/window

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name: ")

def click():
    mylabel = Label(root, text='hello ' + e.get())
    mylabel.pack()

button01 = Button(root, text='Enter name', padx=50, pady=50, command=click, fg='blue', bg='orange') # can use hex codes for colors
button01.pack()

root.mainloop() # loop to run the gui