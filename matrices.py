# ******* CALCULADORA CON OPERACIONES MATRICIALES *******

# Declaramos la lista matriz_A y la lista matriz_B que contendra los elementos de la primera y segunda matriz respectivamente
matriz_A = []
matriz_B = []

def mostrar_operaciones():
	print("########## BIENVENIDO A LA CALCULADORA DE MATRICES ###########")
	menu = """
	1_ Suma de matrices
	2_ Resta de matrices
	3_ Multiplicacion de matrices
	4_ Adjunto de una matriz

	"""
	print(menu)

def pedir_opcion():
	opcion = input("Ingrese una opcion : ")
	return opcion 

def pedir_filas_y_columnas():
	n = input("Ingrese el numero de filas y columnas de la matriz (separado por un espacio) : ")
	n = n.split(" ")
	for i in range(len(n)):
		a = n[i]
		n[i] = int(a)
	filas = n[0]
	columnas = n[1]
	return filas, columnas

def pedir_elementos(num_filas,matriz):
	for i in range(num_filas):
		a = input()
		a = a.split(" ")
		for i in range(len(a)):
			aux = a[i]
			a[i] = int(aux)

		matriz.append(a)

def suma_matrices(matriz1,matriz2):
	matriz_suma = matriz1
	for i in range(filas):
		for j in range(columnas):
			matriz_suma[i][j] = matriz1[i][j] + matriz2[i][j]

	return matriz_suma

def resta_matrices(matriz1,matriz2):
	matriz_resta = matriz1
	for i in range(filas):
		for j in range(columnas):
			matriz_resta[i][j] = matriz1[i][j] - matriz2[i][j]

	return matriz_resta

def producto_matrices(matriz1,matriz2):
	

# Mostramos el menu con las operaciones
mostrar_operaciones()

# Pedimos una opcion al usuario
opcion = pedir_opcion()

# Pedimos el numero de filas y columnas para la primera matriz
filas,columnas = pedir_filas_y_columnas()

# Pedimos los elementos de la primera matriz
pedir_elementos(filas,matriz_A)


# Pedimos el numero de filas y columnas para la segunda matriz
filas2,columnas2 = pedir_filas_y_columnas()

# Pedimos los elementos de la segunda matriz
pedir_elementos(filas2,matriz_B)

# 

if opcion == "1":
	matriz_suma = suma_matrices(matriz_A,matriz_B)
	
elif opcion == "2":
	matriz_resta = resta_matrices(matriz_A,matriz_B)

elif opcion == "3":
	pass
elif opcion == "4":
	pass