import csv

with open('Proyecto_Arquitectura_CSV.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print("Estado actual: {0}, Símbolo actual: {1}, Nuevo estado: {2}, Nuevo símbolo: {3}, Movimiento: {4}".format(row[0], row[1], row[2], row[3], row[4]))

#Escribir archivo csv
with open('Proyecto_Arquitectura_CSV.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
