print("Tributar impuestos")
edad = int(input("Cual es tu edad: "))
ingresos = float(input("Cual es tu ingreso mensual: "))

if edad >= 16 and ingresos >= 1000:
    print("Puedes tributar tus ingresos")
else:
    print("No puedes tributar tus impuestos, debes de tener mas de 16 años y debes de tener mas de 1000 en ingresos.")
    