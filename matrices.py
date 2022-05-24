# ******* CALCULADORA CON OPERACIONES MATRICIALES *******

# Declaramos la lista matriz_A y la lista matriz_B que contendra los elementos de la primera y segunda matriz respectivamente
import numpy as np
matriz_A = []
matriz_B = []

def mostrar_operaciones():
	print("########## BIENVENIDO A LA CALCULADORA DE MATRICES ###########")
	menu = """
	1_ Suma de matrices
	2_ Resta de matrices
	3_ Multiplicacion de matrices
	4_ Determinante de una matriz

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
    a = np.array(matriz1)
    b = np.array(matriz2)
    matriz_producto = a.dot(b)
    return matriz_producto
	
def determinante_matriz(matriz1,matriz2):
    a = np.array(matriz1)
    b = np.array(matriz2)
    determinante_a = np.linalg.det(a)
    determinante_b = np.linalg.det(b)
    return determinante_a,determinante_b

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
	print(matriz_suma)
elif opcion == "2":
	matriz_resta = resta_matrices(matriz_A,matriz_B)
	print(matriz_resta)

elif opcion == "3":
	matriz_producto = producto_matrices(matriz_A,matriz_B)
	print(matriz_producto)
elif opcion == "4":
	determinante_A, determinante_B = determinante_matriz(matriz_A,matriz_B)
	print(determinante_A)
	print(determinante_B)
	
	
	
