from CSV import *
from TXT import *
from MaquinaTuring import*


cint=TXT(1)
cint1=TXT.leer()
csv1=CSV("hola")
logic=csv1.leerCSV()
MT=MaquinaTuring(logic,cint1,4)
MT.operar()