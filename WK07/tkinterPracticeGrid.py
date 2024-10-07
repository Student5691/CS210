from tkinter import * # import tkinter

root = Tk() # create the base canvas/window

labelWidget01 = Label(root, text="hello world") # create a "label", assign it to the root, define its contents/text
labelWidget02 = Label(root, text="fds fdsa fdsa fdsa gfds gf") # create a "label", assign it to the root, define its contents/text

labelWidget01.grid(row=0, column=0)
labelWidget02.grid(row=1, column=0)

root.mainloop() # loop to run the gui