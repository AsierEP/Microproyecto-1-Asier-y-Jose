from tkinter import *
from CSV import *
from TXT import *
from MaquinaTuring import*
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
    Button(window1, text="Ejecutar el programa", width=28, height=4, command= window4).place(relx=0.4, rely=0.8)

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

def window4():
    global window4
    window4 = Tk()
    window4.geometry("1000x600")
    window4.title("Menu")
    window4.resizable(False, False)
    window4.configure(bg="light yellow")
    numero=StringVar()
    entry=Entry(window4,textvariable=numero)
    entry.place(x=300,y=300)
    entry.config(bg="white")
    cint=TXT(1)
    cint1=TXT.leer()
    csv1=CSV("hola")
    logic=csv1.leerCSV()
    MT=MaquinaTuring(logic,cint1,4)

    CustomFontTi= ("Arial",22,"bold")
    CustomFontTxt= ("Arial",12,"bold")
    CustomFontCinta= ("Arial",6,"bold")    
    Title = Label(window4, text= "Bienvenido a la simulación de la máquina de Turing", font=CustomFontTi)
    Title.pack()
    Txt1 = Label(window4, text= "La cinta del programa es la siguiente:", font=CustomFontTxt)
    Txt1.pack()
    Txt2 = Label(window4, text= MT.obtenerCinta(), font=CustomFontCinta)
    Txt2.pack(anchor=CENTER)
    Txt2.config(font=(24))
    Txt3 = Label(window4, text= "Estado actual", font=CustomFontCinta)
    Txt3.place(x=50,y=200)
    Txt4 = Label(window4,text="1",font=CustomFontTi)
    Txt4.place(x=50,y=250)


    Button(window4, text="Seleccionar Posicion de la cabeza lectora", width=28, height=4, command=lambda:selectPos()).place(relx=0.4, rely=0.8)
    Button(window4, text="Ejecutar el programa", width=28, height=4, command=lambda:ejecutar()).place(relx=0.4, rely=0.6)
   
    def getnum():
        num=numero.get()
        return num

    def selectPos():
        print(getnum())
        MT.SetPos(int(getnum()))

    def ejecutar():
        MT.operar()
        Txt4["text"]=MT.GetEstado()
        Txt2["text"]=MT.obtenerCinta()

    window1.mainloop()

def back_menu31():
    window1.iconify()
    window1.deiconify()
    window3.destroy()
def back_menu21():
    window1.iconify()
    window1.deiconify()
    window2.destroy()

window1()