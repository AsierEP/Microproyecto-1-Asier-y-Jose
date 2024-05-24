from tkinter import *

cinta = "0"*200
def window1():
    global window1
    window1 = Tk()
    window1.geometry("1000x600")
    window1.title("Menu")
    window1.resizable(False, False)
    window1.configure(bg="light yellow")


    CustomFontTi= ("Arial",22,"bold")
    CustomFontTxt= ("Arial",12,"bold")
    CustomFontCinta= ("Arial",6,"bold")    
    Title = Label(window1, text= "Bienvenido a la simulación de la máquina de Turing", font=CustomFontTi)
    Title.pack()
    Txt1 = Label(window1, text= "La cinta del programa es la siguiente:", font=CustomFontTxt)
    Txt1.pack()
    Txt2 = Label(window1, text= cinta, font=CustomFontCinta)
    Txt2.pack()
    Txt3 = Label(window1, text= "Presentado por:\n Asier Errasti C.I: 30497244 \n Luis Morales C.I: \n Jesús Fernández C.I: ", font=CustomFontCinta)
    Txt3.place(rely=0.8)
    Txt3.anchor("sw")


    Button(window1, text="Modificar las líneas del CSV", width=28, height=4, command= window2).place(relx=0.4, rely=0.4)
    Button(window1, text="Modificar la cabeza de la cinta", width=28, height=4, command= window3).place(relx=0.4, rely=0.6)
    Button(window1, text="Ejecutar el programa", width=28, height=4, command= ejecutar).place(relx=0.4, rely=0.8)

    window1.mainloop()

def window2():
    global window2
    window2 = Toplevel(window1)
    window2.geometry("800x700")
    window2.title("CSV Mod")
    window2.resizable(False, False)
    window2.configure(bg="light blue")
    
    CustomFontTi= ("Arial",18,"bold")
    CustomFontTxt= ("Arial",12,"bold")
    Title = Label(window2, text= "Bienvenido al menú de modificación de modificación del CSV", font=CustomFontTi)
    Title.pack()

    Button(window2, text="Volver al menú", width=28, height=4, command= back_menu21).place(relx=0.4, rely=0.6)

    if(window2):
        window1.withdraw()
    
    window2.mainloop()


def window3():
    global window3
    window3 = Toplevel(window1)
    window3.geometry("900x700")
    window3.title("Head Mod")
    window3.resizable(False, False)
    window3.configure(bg="light green")

    CustomFontTi= ("Arial",18,"bold")
    CustomFontTxt= ("Arial",12,"bold")
    CustomFontCinta= ("Arial",6,"bold")
    Title = Label(window3, text= "Bienvenido al menú de modificación de la cabeza de la cinta", font=CustomFontTi)
    Title.pack()
    Txt1 = Label(window3, text="Por favor introducir la posición donde quiera localizar la cabeza: \n (siendo 1 el primer caracter de la cinta)", font=CustomFontTxt)
    Txt1.place(x=250, y=130)
    TF1 = Entry(window3)
    TF1.place(x=350, y=200)
    Txt2 = Label(window3, text=cinta, font=CustomFontCinta)
    Txt2.place(x=30, y=300)

    Button(window3, text="Volver al menú", width=28, height=4, command= back_menu31).place(relx=0.4, rely=0.6)

    if(window3):
        window1.withdraw()
    
    window3.mainloop()

def ejecutar():
    None

def back_menu31():
    window1.iconify()
    window1.deiconify()
    window3.destroy()
def back_menu21():
    window1.iconify()
    window1.deiconify()
    window2.destroy()

window1()