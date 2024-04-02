import csv

class CSV:

    def __init__(self,path):
        self.path=path

    def leerCSV(self):
        with open(r'C:\Users\UsuarioDeWindows\Documents\Proyecto Arqui\Proyecto-arquitectura\Proyecto_Arq\Proyecto_Arquitectura_CSV.csv') as f:
            reader = csv.reader(f)
            PingaDeString=""
            for fila in reader:
                PingaDeString += fila[0]+","+fila[1]+","+fila[2]+","+fila[3]+","+fila[4]+"\n"
                print("Estado actual: {0}, Símbolo actual: {1}, Nuevo estado: {2}, Nuevo símbolo: {3}, Movimiento: {4}".format(fila[0], fila[1], fila[2], fila[3], fila[4]))
        return PingaDeString

    def EscribirCSV(self):
        #Escribir archivo csv
        with open('Proyecto_Arquitectura_CSV.csv', 'w') as f:
            writer = csv.writer(f, delimiter=',')

