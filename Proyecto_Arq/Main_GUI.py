from tkinter import *

cinta = "0" * 200

root=Tk()
root.title("Main Window")
root.resizable(False,False)
root.geometry("1000x600")
root.config(bg="light yellow")

""" myFrameBut1=Frame()
myFrameBut1.pack()
myFrameBut1.place(relx=0.5, rely=0.45, anchor="s")
CustomFontBut1= ("Arial",18,"bold")
myFrameBut1.config(bg="light green")
myFrameBut1.config(width="600",height="100")
myFrameBut1.config(relief="groove")
myFrameBut1.config(bd="20")
myLabel = Label(myFrameBut1, text="Editar líneas del archivo CSV",font= CustomFontBut1)
myLabel.pack()
myFrameBut1.config(cursor="hand2") """

Button()

myTitle=Frame()
myTitle.pack()
myTitle.place(relx=0.5,rely=0.04, anchor="n")
CustomFontTi= ("Arial",22,"bold")
myLabelTi = Label(myTitle, text="Bienvenido al simulador de la máquina de Touring",font= CustomFontTi)
myLabelTi.pack()

myFrameBut2=Frame()
myFrameBut2.pack()
myFrameBut2.place(relx=0.5, rely=0.65, anchor="s")
CustomFontBut2= ("Arial",18,"bold")
myFrameBut2.config(bg="red")
myFrameBut2.config(width="600",height="100")
myFrameBut2.config(relief="groove")
myFrameBut2.config(bd="20")
myLabel = Label(myFrameBut2, text="Ejecutar el programa",font= CustomFontBut2)
myLabel.pack()
myFrameBut2.config(cursor="hand2")


myFrameBut3=Frame()
myFrameBut3.pack()
myFrameBut3.place(relx=0.6, rely=0.85, anchor="s")
CustomFontBut3= ("Arial",18,"bold")
myFrameBut3.config(bg="blue")
myFrameBut3.config(width="600",height="100")
myFrameBut3.config(relief="groove")
myFrameBut3.config(bd="20")
myLabel = Label(myFrameBut3, text="Modificar la cabeza \n de la cinta",font= CustomFontBut3)
myLabel.pack()
myFrameBut3.config(cursor="hand2")


myFrametxt1=Frame()
myFrametxt1.pack()
myFrametxt1.place(relx=0.08, rely=0.31, anchor="s")
CustomFonttxt1= ("Arial",11,"bold")
myFrametxt1.config(bd="20")
myLabel = Label(myFrametxt1, text="La cinta es \n la siguiente:",font= CustomFonttxt1)
myLabel.pack()


myFrametxt2=Frame()
myFrametxt2.pack(side="bottom",anchor="e")
CustomFonttxt2= ("Arial",12,"bold")
myFrametxt2.config(bd="20")
myLabel = Label(myFrametxt2, text="Realizado por:\n Asier Errasti C.I:30497244 \n Luis Morales C.I: \n Jesús Fernández C.I:",font= CustomFonttxt2)
myLabel.pack()

myFrameTF1 = Frame(root, width=2000, height=600)
myFrameTF1.pack()
myFrameTF1.place(relx=0.3, rely=0.76)
TextField1 = Entry(myFrameTF1)
TextField1.pack()

myFrametxt3=Frame()
myFrametxt3.pack()
myFrametxt3.place(relx=0.015, rely=0.68)
CustomFonttxt3= ("Arial",10,"bold")
myFrametxt3.config(bd="20")
myLabel = Label(myFrametxt3, text="Escribir el número \n de orden \n a donde quiera mover la \n cabeza del programa:",font= CustomFonttxt3)
myLabel.pack()

myFrametxt4=Frame()
myFrametxt4.pack()
myFrametxt4.place(relx=0.15, rely=0.2)
CustomFonttxt4= ("Arial",5,"bold")
myFrametxt4.config(bd="20")
myLabel = Label(myFrametxt4, text=cinta,font= CustomFonttxt4)
myLabel.pack()





root.mainloop()