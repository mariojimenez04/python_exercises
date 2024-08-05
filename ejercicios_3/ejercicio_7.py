edad = int(input("¿Cual es tu edad? "))

if edad < 4:
    print("Tu entrada es gratis")
elif edad <= 18:
    print("Tu entrada cuesta 5€")
else:
    print("Tu entrada cuesta 10€")