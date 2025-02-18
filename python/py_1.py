import csv

with open('C:/Users/Mario J/Downloads/ejemplo.csv', mode="r", encoding='utf-8') as archivo:
    lector = csv.reader(archivo)

    for fila in lector:
        print(fila)