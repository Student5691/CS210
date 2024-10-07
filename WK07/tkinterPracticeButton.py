from tkinter import * # import tkinter

root = Tk() # create the base canvas/window

def click():
    mylabel = Label(root, text='button clicked')
    mylabel.pack()

button01 = Button(root, text='Click Me', padx=50, pady=50, command=click, fg='blue', bg='orange') # can use hex codes for colors
button01.pack()

root.mainloop() # loop to run the gui