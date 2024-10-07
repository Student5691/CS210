from tkinter import * # import tkinter

root = Tk() # create the base canvas/window

labelWidget01 = Label(root, text="hello world") # create a "label", assign it to the root, define its contents/text

labelWidget01.pack() # send te label to its predefined destination, root in this case

root.mainloop() # loop to run the gui