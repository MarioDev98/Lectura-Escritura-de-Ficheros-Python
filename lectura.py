n=int(input('Introduce un número entero entre 1 y 10: '))
nombre_fichero = 'fichero-' + str(n) + '.txt'
try: 
    f = open(nombre_fichero, 'r')
except FileNotFoundError:
    print('No existe el fichero con ese numero', n)
else:
    print("--CONTENIDO DEL FICHERO--")
    print(f.read())
    f.close()