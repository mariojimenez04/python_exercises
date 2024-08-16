import random

vidas = 8
na = random.randint(1, 100)

nombre = input("Cual es tu nombre? ")

print(f"Bueno, {nombre}, he pensado en un numero entre el 1 y 100, y tienes solo ocho intentos para adivinar cual crees que es el numero\n")
print("Que comience el juego")

ni = int(input("ingresa tu primer numero"))

while ni == na:
    