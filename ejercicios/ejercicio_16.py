precio = input("Introduce un precio con 2 decimales: ")

print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')

