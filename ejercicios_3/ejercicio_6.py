renta = int(input("Cual es tu renta anual? "))

if renta < 10000 :
    print("Te corresponde el tipo impositivo de 5%")
elif renta >= 10000 and renta <= 20000:
    print("Te corresponde el tipo impositivo de 15%")
elif renta >= 20000 and renta <= 35000:
    print("Te corresponde el tipo impositivo de 20%")
elif renta >= 35000 and renta <= 60000:
    print("Te corresponde el tipo impositivo de 30%")
else:
    print("Te corresponde el tipo impositivo de 45%")
