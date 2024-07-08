nombresClase = ["Angelo", "Luis", "Victor", "Brenda", "Carlos", "Edgar", "Carlos"]
print(nombresClase)

print(set(nombresClase))

print(tuple(nombresClase))

# setNombresClase = set(nombresClase)
# print(nombresClase[2])
# print(setNombresClase[2])

nombreProfesor = nombresClase[0]
print(nombreProfesor)

nombreFinal = nombresClase[-2]
print(nombreFinal)

nombresTres = nombresClase[0:3]
print(nombresTres)

nombresTres = nombresClase[4:7]
print(nombresTres)

nombresTres = nombresClase[:3]
print(nombresTres)

nombresTres = nombresClase[-3:]
print(nombresTres)

lista01 = [5,8,9,5,4,56]
print(lista01)
lista01.append(20)
print(lista01)

lista01[3] = 11
print(lista01)

Pedro = {
    "Nombre": "Pedro",
    "Apellido": "Perez",
    "Edad": 21
    }
print(Pedro["Edad"])

Pedro["Peso"] = 70
print(Pedro["Peso"])

print(list(Pedro.keys()))
print(list(Pedro.values()))

Pedro = {
    "Nombre": "Pedro",
    "Apellido": "Perez",
    "Edad": 21,
    "Cursos" : {
        "Mates" : 8.5,
        "Lenguaje" : 7.6,
        "Fisica" : 8.2
    },
    "Juegos" : ["Lol", "cod", "bt2042"]
    }
print(Pedro["Cursos"])

# Programa que determina si un número es positivo, negativo o cero:
numero = int(input("Ingrese un número: "))

if numero>0:
  print(f"{numero} es mayor que 0.")
elif numero<0:
  print(f"{numero} es menor que 0.")
else:
  print(f"{numero} es igual a cero.")

  vocales = ["a", "e", "i", "o", "u"]
for vocal in vocales:
  print(vocal)

for i in range(6):
  print(i)

for i in range(3,9):
  print(i)

for i in range(2, 15, 2):
  print(i)

for i in range(21, -5, -2):
  print(i)

# Dado un número entero positivo n, imprimir todos los números pares menores o iguales a n.

n = int(input("Ingrese un número entero positivo: "))
for i in range(2, n+1, 2):
    print(i)


n = int(input("Ingrese un número entero positivo: "))
i = 2
while i <= n:
    print(i)
    # i = i+2
    i += 2

i = 0
while True:
  print(i)
  if i==5:
    break
  i += 1