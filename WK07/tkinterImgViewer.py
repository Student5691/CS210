from tkinter import *
from PIL import ImageTk, Image # must use this for files other than .png, .gif, .pgm, .ppm; files like .jpg, .jpeg, etc.

root = Tk()
root.geometry("1000x1000")
root.title("Viewer")
root.iconbitmap(r"C:\Users\User01\Desktop\download.ico")

img1 = PhotoImage(file=r"C:\Users\User01\Desktop\download.png")

# img1 = PhotoImage(file=r"C:\Users\User01\Downloads\1.jpg") # .jpg file type causes a crash, must do lines below



#non-support image file types, .jpg test
jpg_img = ImageTk.PhotoImage(Image.open(r"C:\Users\User01\Downloads\1.jpg"))
jpg_label = Label(image=jpg_img)

img1_label= Label(root, image=img1)


jpg_label.place(x=100, y=100)
img1_label.place(x=0, y=0)


btn_quit = Button(root, text="QUIT", command=root.quit)
# btn_quit.config(state=DISABLED) # use .config to update button parameters without recreating the button
btn_quit.place(x=100, y=100)

root.mainloop()