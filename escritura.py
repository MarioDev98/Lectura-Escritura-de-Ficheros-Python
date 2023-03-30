n = int(input('Introduce un número entero entre 1 y 10: '))
nombre_fichero = 'fichero-' + str(n) + '.txt'
f = open(nombre_fichero, 'w')
texto = input("escribe lo que quieras")
f.write(texto)
f.close()