#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

n = int(input("Ingresa un numero entero: "))

if n % 2 == 0:
    print(f"El numero {n} es par")
elif n % 2 == 1:
    print(f"El numero {n} es impar")

    