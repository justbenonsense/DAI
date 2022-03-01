# ejercicios/ejercicio3.py

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
	

# Programa principal
try:
		# Leemos el número que introducen 
		num = int(input())

		if num <= 0:
			print("Error. No ha introducido un número natural.")
		else:
			print("Los números primos menores que "+str(num)+" son: "+cribaEratostenes(num))  

except ValueError:
		print("Error. No ha introducido un número natural.")                   

