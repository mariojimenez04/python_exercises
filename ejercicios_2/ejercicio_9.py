cantidad = float(input("Cuanto va a invertir: ")) #cantidad significa Cantidad Invertir
interes = float(input("De cuanto es el interes anual: "))
anios = int(input("Cuantos años seran de la inversion? "))

capital_obtenido = round(cantidad * (interes / 100 + 1) ** anios, 2)
# capital_obtenido = cantidad * (interes / 100 + 1) ** anios

print(f"El total de capital obtenido sera de {capital_obtenido}")