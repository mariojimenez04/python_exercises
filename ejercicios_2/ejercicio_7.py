peso = float(input("Cual es tu peso? "))
altura = float(input("Cual es tu estatura en metros: "))

imc = peso / ( (altura) ** 2 )

print("Tu IMC es de: ", round(imc, 2))