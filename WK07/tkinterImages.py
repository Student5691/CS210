from tkinter import *
from PIL import ImageTk, Image # must use this for files other than .png, .gif, .pgm, .ppm; files like .jpg, .jpeg, etc.

root = Tk()
root.title("Images")
root.iconbitmap(r"C:\Users\User01\Desktop\download.ico")

img1 = PhotoImage(file=r"C:\Users\User01\Desktop\download.png")

# img1 = PhotoImage(file=r"C:\Users\User01\Downloads\1.jpg") # .jpg file type causes a crash, must do lines below

img1_label= Label(root, image=img1)
img1_label.pack()

#non-support image file types, .jpg test
jpg_img = ImageTk.PhotoImage(Image.open(r"C:\Users\User01\Downloads\1.jpg"))
jpg_label = Label(image=jpg_img)
jpg_label.pack()


btn_quit = Button(root, text="QUIT", command=root.quit)
btn_quit.pack()

root.mainloop()