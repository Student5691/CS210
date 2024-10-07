from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def btnClick(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def btnAdd():
    global add_val
    add_val = int(e.get())
    e.delete(0, END)


def btnEqual():
    current = int(e.get())
    result = current + add_val
    e.delete(0, END)
    e.insert(0, result)

def btnClear():
    e.delete(0, END)

btn_1 = Button(root, text='1', padx=40, pady=20, command=lambda: btnClick(1))
btn_2 = Button(root, text='2', padx=40, pady=20, command=lambda: btnClick(2))
btn_3 = Button(root, text='3', padx=40, pady=20, command=lambda: btnClick(3))
btn_4 = Button(root, text='4', padx=40, pady=20, command=lambda: btnClick(4))
btn_5 = Button(root, text='5', padx=40, pady=20, command=lambda: btnClick(5))
btn_6 = Button(root, text='6', padx=40, pady=20, command=lambda: btnClick(6))
btn_7 = Button(root, text='7', padx=40, pady=20, command=lambda: btnClick(7))
btn_8 = Button(root, text='8', padx=40, pady=20, command=lambda: btnClick(8))
btn_9 = Button(root, text='9', padx=40, pady=20, command=lambda: btnClick(9))
btn_0 = Button(root, text='0', padx=40, pady=20, command=lambda: btnClick(0))

btn_add = Button(root, text='+', padx=39, pady=20, command=lambda: btnAdd())
btn_equal = Button(root, text='=', padx=91, pady=20, command=lambda: btnEqual())
btn_clear = Button(root, text='Clear', padx=81, pady=20, command=lambda: btnClear())

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_0.grid(row=4, column=0)
btn_clear.grid(row=4, column=1, columnspan=2)
btn_add.grid(row=5, column=0)
btn_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()