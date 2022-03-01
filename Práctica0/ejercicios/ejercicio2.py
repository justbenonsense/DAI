# ejercicios/ejercicio2.py

import time
import random

# Método de ordenación de matrices unidimensionales burbuja
def burbuja(m):
	for vuelta in range(len(m)-1,0,-1):
		for i in range(vuelta):
			if m[i] > m[i+1]:
				aux = m[i]
				m[i] = m[i+1]
				m[i+1] = aux

# Método de ordenación de matrices unidimensionales selección
def seleccion(m):
	for vuelta in range(len(m)-1,0,-1):
		posMayor = 0
		for i in range (1,vuelta+1):
			if m[i] > m[posMayor]:
				posMayor = i

		aux = m[vuelta]
		m[vuelta] = m[posMayor]
		m[posMayor] = aux
	

# Método de ordenación de matrices unidimensionales inserción
def insercion(m):
	for i in range(1,len(m)):
		
		valorActual = m[i]
		pos = i

		while pos > 0 and m[pos-1] > valorActual:
			m[pos] = m[pos-1]
			pos = pos-1

		m[pos] = valorActual


# Programa principal

tam = 10
m1 = []

# Generamos la matriz unidimensional de forma aleatoria
for i in range(0,tam-1):
	num = random.randint(0,100)
	m1.append(num)

# Hacemos dos copias para probar todos los métodos
m2 = m1[:]
m3 = m1[:]

print("Matriz sin ordenar: ", m1)

# La ordenamos mediante el método burbuja
t_inicio = time.time()
burbuja(m1)
t_final = time.time()

print("Matriz ordenada: ", m1)

print("Tiempo mediante ordenación burbuja (s): ", t_final-t_inicio)


# La ordenamos mediante el método selección
t_inicio = time.time()
seleccion(m2)
t_final = time.time()

print("Matriz ordenada: ", m2)

print("Tiempo mediante ordenación selección (s): ", t_final-t_inicio)


# La ordenamos mediante el método inserción
t_inicio = time.time()
insercion(m3)
t_final = time.time()

print("Matriz ordenada: ", m3)

print("Tiempo mediante ordenación inserción (s): ", t_final-t_inicio)

