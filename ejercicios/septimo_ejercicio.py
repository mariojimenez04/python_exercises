peso = float(input("¿Cual es tu peso (kg)? "))
estatura = float(input("¿Cual es tu estatura (mts)? "))

imc = round(peso / (estatura)**2,2)

print("Tu indice masa corporal es de: ", imc)