# nombre = "Mario" 

# nombre = "Alejandro"
# print(nombre)

# edad = 15
# print(edad)

# nombre = "Tony Soprano"
# edad = 30

# print("Hola " + nombre + ", tu edad es de: " + str(edad) + ", saludos y bienvenido")

# nombre = "Julia "
# apellido = "Roberts"
# nombre_completo = nombre + apellido

# print(nombre_completo)

# languaje = "Python"
# frase = "Estás tomando un curso de " + languaje

# print(frase)

# numero_entero = 30
# print("Tu edad es: " + str(numero_entero))
# print(type(numero_entero))

# num_decimal = 144.50
# print(type(num_decimal))

# num1 = 7.5
# num2 = 2.5
# resultado = num1 + num2
# print(type(resultado))

# num1 = "7.5"
# num2 = "10"

# resultado = float(num1) + int(num2)
# print(type(resultado))

# nombre = "Mario Alejandro"
# edad = 34

# print(f"Mi nombre es {nombre} y mi edad es de {edad}")

# nombre_asociado = "Jesse Pinkman"
# numero_asociado = 399058

# print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")

# puntos_nuevos = 350
# puntos_totales = 1225

# print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales + puntos_nuevos}")

# puntos_nuevos = 350
# puntos_totales = 1225

# print("Has ganado {} puntos! En total, acumulas {}".format(puntos_nuevos, puntos_nuevos + puntos_totales))

# puntos_nuevos = 350
# puntos_totales = 1225

# print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")

# puntos_anteriores = 875
# puntos_nuevos = 350

# print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_anteriores + puntos_nuevos} puntos") 

#           DIVISION AL PISO

# print(874//27)

#           MODULO
# print(456%33)

#           RAIZ CUADRADA
# print(783**0.5)

#           REDONDEAR CON round()
# print(round(10/3, 2)) # Se hace una division y se redondea con 2 digitos despues de el .

# valor = 10.676767

# print(round(valor))

# print(round(5**0.5, 4)) #aplicar raiz cuadrada y el resultado que aparezca con 4 digitos despues de el .
# num1 = 13.87

# print(round(num1))
# print(int(num1))

################# PROYECTO ###################

# nombre = input("¿Cual es tu nombre?")

# ventas = int(input("¿Cuanto haz vendido?"))

# # print(f"Hola {nombre}.\nTus comisiones de ventas es de el 10%, así que te toca de comision {ventas * 13 / 100}\nEsperemos la siguiente vez, vendas mas\nSaludos!!!")

# print(f"Ok {nombre}. Este mes ganaste ${round(ventas * 13 / 100, 2)}")

# if 5 > 2:
#     print("Five is greater than two!")

# if 5 > 2:
#     print("Five is greater than two!")
#     print("Five is greater than two!")
#     print("Five is greater than two!")
#     print("Five is greater than two!")

# palabra = "ordenador"
# resultado = palabra[4] <- esta linea indica que indique la letra posicionada en el indice 4
# print(resultado)

# frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
# resultado = frase.index("práctica") <- esta linea de indica que coloque el iniciador de el indice de la primera palabra "práctica"
# print(resultado)

# frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
# resultado = frase.index("práctica", 37) <- esta linea indica que busques en donde inicia de la siguiente palabra "práctica" a partir del indice 37
# print(resultado)

# frase = "Controlar la complejidad es la esencia de la programación"
# resultado = frase[0:9]    <- con esta linea puedes obtener el texto desde el indice 0 hasta el indice 9
# print(resultado)

# frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
# resultado = frase[8::3]   <-con esta linea puedes obtener desde el indice 8 que es 'n' hasta el final y imprimiendo la letra de cada 2 que saltea
# print(resultado)

# frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
# resultado = frase[::-1] <- con esta linea puedes obtener toda la frase al reves desde el indice -1 que es desde el de la derecha
# print(resultado)

# texto = "Nancy es la mejor persona del mundo"
# resultado = texto.upper()
# print(resultado)

# frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
# resultaado = frase.upper() <-Con esta linea puedes imprimir todo en mayuscula
# print(resultaado)

# lista_palabras = ["La","legibilidad","cuenta."]
# resutlado = " ".join(lista_palabras) <- Con esta linea puedes unir todo lo que esta en "lista_palabras" separados por un espacio
# print(resutlado)

# frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
# resultado = frase.replace("difícil", "fácil").replace("mala", "buena")
# print(resultado)

# print("Repetición" * 15) <- con esta linea de codigo repites la palabra a imprimir determinadas veces, en este caso 15

# frase = """Tierra mojada
# mis recuerdos de viaje,
# entre las lluvias"""
# print("agua" not in frase) <- con esta linea puedes buscar que NO existe la palabra "agua" en la variable "frase"

# palabra = "electroencefalografista"
# print(len(palabra)) <- con esta linea con la palabra reservada len() imprimes el numero de letras que tiene la variable

# mi_lista = [1,0,2,"Mario",3.1416] <- Esta linea se utiliza para imprimir listas
# print(mi_lista)

# medios_transporte = ["avión", "auto", "barco", "bicicleta"]
# medios_transporte.append("motocicleta") <- El metodo append permite añadir valores, siempre los agregar al final
# print(medios_transporte)

# frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
# eliminado = frutas.pop(2) <- Con el metodo pop() puedes eliminar elementos de una lista, si le colocas un numero entre parentesis puedes eliminar el seleccionado tomando en cuenta el indice
# print(frutas)
# print(eliminado)

# dic = {'c1' : ['a', 'b', 'c'], 'c2' : ['d', 'e', 'f']}

# print(dic['c2'][1].upper( ))

# dic = {'1': 'a', '2': 'b'}

# print(dic)

# dic['3'] = 'c' <- Con esta linea agregas valores al diccionario colocando entre [] la llave y despues el valor

# print(dic)

#nombre: Karen
#apellido: Jurgens
#edad: 35
#ocupacion: Periodista

# mi_dic = {'nombre': 'Karen', 'apellido': 'Jurgens', 'edad': 35, 'ocupacion': 'Periodista'}

# mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
# print(mi_dict['puntos']['points2'][1])

# mi_dict['puntos']['points2'][1] = 400

# print(mi_dict)

# mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}

# mi_dic['pais'] = 'Colombia'
# mi_dic['edad'] = 36
# mi_dic['ocupacion'] = 'Editora'

# print(mi_dic)

# mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
# print(mi_tupla.count(2)) <- con .count() puedes contar las veces que se repite un valor

# mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)

# mi_lista = list(mi_tupla) <- Converti la tupla en una lista con la funcion list()

# print(type(mi_lista))

# mi_tupla = (1, 2, 3, 4)

# a,b,c,d = mi_tupla

# print(a)
# print(b)
# print(c)
# print(d)

# mi_set_1 = {1, 2, "tres", "cuatro"}
# mi_set_2 = {"tres", 4, 5} 

# mi_set_3 = mi_set_1.union(mi_set_2) <- con el metodo .union() unes 2 sets

# print(mi_set_3)

# sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

# sorteo.pop() <- con el metodo .pop() eliminas un elemento al azar del set

# print(sorteo)

# sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

# sorteo.add("Damián") <- con el metodo add() puedes agregar valores a los set

# print(sorteo)

# prueba = bool(5 == '5')

# print(prueba)

# resultado = 17834 / 34 > 87*56

# print(resultado)

# resultado = 25**0.5 == 5

# print(resultado)

# palabra = "éxito"

# print(palabra[4])

# redes = ["YouTube", "Facebook", "Twitter", "Whatsapp"]

# print(redes.sort())

######### PROYECTO ###############

# texto = input("Ingresa un texto, no importa la cantidad de caracteres: ")
# letras = input("Ingresa 3 letras de tu eleccion: ")
# l1 = list(letras)
# total_texto = texto.split()

# print("El conteo de letras de la primera que seleccionaste '", l1[0].strip(), "' es de ", texto.count(l1[0]))
# print("El conteo de letras de la primera que seleccionaste '", l1[1].strip(), "' es de ", texto.count(l1[1]))
# print("El conteo de letras de la primera que seleccionaste '", l1[2].strip(), "' es de ", texto.count(l1[2]))
# print("El texto ingresado contiene un total de", len(total_texto), "palabras")
# print("El texto ingresado el primer caracter es", texto[0], "y el ultimo caracter es", texto[-1])
# total_texto.reverse()
# texto_invertido = ' '.join(total_texto)
# print("El texto ingresado al reverso quedaria de la siguiente manera: ", texto_invertido)

# buscar_palabra = 'python' in texto
# dic = {True:"si", False:"no"}

# print("La palabra 'Python'", dic[buscar_palabra], "se encuentra en el texto ingresado")
