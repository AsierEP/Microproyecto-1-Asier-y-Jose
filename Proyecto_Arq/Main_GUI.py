from tkinter import *

root=Tk()
root.title("Main Window")
root.resizable(False,False)
root.geometry("1000x600")
root.config(bg="light yellow")

myFrame=Frame()
myFrame.pack()
myFrame.place(relx=0.5, rely=0.9, anchor="s")
myFrame.config(bg="light gray")
myFrame.config(width="600",height="400")
myFrame.config(relief="groove")
myFrame.config(bd="20")

root.mainloop()