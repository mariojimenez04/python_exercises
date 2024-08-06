print("######## Bienvenido a La familia ########")
print("Para el menu de hoy, tenemos pizzas")
print("El menu es el siguiente:")
print("Ingredientes vegetarianos: Pimiento y tofu.")
print("Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.")

ingrediente_elegido = ''

pizza = input("Elige una de las siguientes pizzas:\n -Vegetariana\n -No vegetariana\n").lower()

if pizza == "vegetariana":
    ingrediente_elegido = input("Puedes elegir entre los siguientes ingredientes:\n -Pimientos\n -Tofu\n ").lower()
    if ingrediente_elegido == "pimientos":
        print(f"La pizza que elegiste es vegetariana y elegiste como ingrediente {ingrediente_elegido}")
    elif ingrediente_elegido == "tofu":
        print(f"La pizza que elegiste es vegetariana y elegiste como ingrediente {ingrediente_elegido}")
    else:
        print(f"El ingrediente {ingrediente_elegido} no existe")
elif pizza == "no vegetariana":
    ingrediente_elegido = input("Puedes elegir entre los siguientes ingredientes:\n -Peperoni\n -Jamon\n -Salmon\n").lower()
    if ingrediente_elegido == "peperoni":
        print(f"La pizza que elegiste es vegetariana y elegiste como ingrediente {ingrediente_elegido}")
    elif ingrediente_elegido == "jamon":
        print(f"La pizza que elegiste es vegetariana y elegiste como ingrediente {ingrediente_elegido}")
    elif ingrediente_elegido == "salmon":
        print(f"La pizza que elegiste es vegetariana y elegiste como ingrediente {ingrediente_elegido}")
    else:
        print(f"El ingrediente {ingrediente_elegido} no existe")
else:
    print(f"La pizza {pizza} no existe, vuelve a elegir")

