# ejercicios/ejercicios.py

import time
import random
import re


#--------------------- Ejercicio 2 -------------------------

# Método de ordenación de matrices unidimensionales burbuja
def burbuja(m):
	t_inicio = time.time()

	for vuelta in range(len(m)-1,0,-1):
		for i in range(vuelta):
			if m[i] > m[i+1]:
				aux = m[i]
				m[i] = m[i+1]
				m[i+1] = aux

	t_final = time.time()
	tiempo = t_final - t_inicio

	return m, tiempo

# Método de ordenación de matrices unidimensionales selección
def seleccion(m):
	t_inicio = time.time()

	for vuelta in range(len(m)-1,0,-1):
		posMayor = 0
		for i in range (1,vuelta+1):
			if m[i] > m[posMayor]:
				posMayor = i

		aux = m[vuelta]
		m[vuelta] = m[posMayor]
		m[posMayor] = aux

	t_final = time.time()
	tiempo = t_final - t_inicio

	return m, tiempo
	

# Método de ordenación de matrices unidimensionales inserción
def insercion(m):
	t_inicio = time.time()

	for i in range(1,len(m)):

		valorActual = m[i]
		pos = i

		while pos > 0 and m[pos-1] > valorActual:
			m[pos] = m[pos-1]
			pos = pos-1

		m[pos] = valorActual

	t_final = time.time()
	tiempo = t_final - t_inicio

	return m, tiempo



#--------------------- Ejercicio 3 -------------------------

# Criba de Eratóstenes
def cribaEratostenes(n):

	primos = []
	esPrimo = [1 for i in range(n)]
	esPrimo[0] = esPrimo[1] = 0

	# Recorremos la matriz unidimensional
	for i in range(n):
		if esPrimo[i]:
			primos.append(i)
			cont = 2
			while i*cont < n:
				esPrimo[i*cont] = 0
				cont += 1

	return primos




#--------------------- Ejercicio 4 -------------------------

# Función que calcula el n-ésimo número de la sucesión de Fibonacci
def nNumFibonacci(n):

	n1 = 0
	n2 = 1

	if n == 1:
		num = 0
	else:
		
		if n == 2:
			num = 1
		else:
			for i in range(n-2):
				num = n1 + n2
				n1 = n2
				n2 = num

	return num



#--------------------- Ejercicio 5 -------------------------

# Comprueba si una secuencia de corchetes está balanceada, es decir, que se componga de parejas de corchetes de apertura y cierre correctamente anidados.
def secuenciaBalanceada(sec):

	correcta = True
	cont = 0
	tam = len(sec)
	suma = 0

	if tam % 2 != 0 or sec[0] == "]" or sec[tam-1] == "[":
		correcta = False
	else: 
		while cont < tam and suma <= 0:	
			if sec[cont] == "[":
				suma -= 1
			else:
				suma += 1
			cont += 1		
				
		if suma != 0:
			correcta = False

	return correcta
	

#--------------------- Ejercicio 6 -------------------------

# Identifica cualquier palabra seguida de un espacio y una única letra mayúscula (por ejemplo: Apellido N).
def palabraSeguidaEspacioyMayus(cadena):

	return bool(re.fullmatch(r'\w+\s+[A-Z]', cadena))


# Identifica correos electrónicos válidos (empieza por una expresión genérica y ve refinándola todo lo posible)
def correoValido(cadena):

	return bool(re.fullmatch(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$', cadena))


# Identifica números de tarjeta de crédito cuyos dígitos estén separados por - o espacios en blanco cada paquete de cuatro dígitos: 1234-5678-9012-3456 ó 1234 5678 9012 3456.	
def numeroTarjeta(cadena):

	return bool(re.fullmatch(r'\d{4}[\s|-]+\d{4}[\s|-]+\d{4}[\s|-]+\d{4}', cadena))

