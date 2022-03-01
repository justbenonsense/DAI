# ejercicios/ejercicio4.py

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
	

# Programa principal

# Abrimos un fichero
f = open(input("Introduzca el nombre del fichero que contiene el número entero para calcular el n-ésimo número de la sucesión de Fibonacci: "))

# Leemos el número que introducen 
n = int(f.read())

# Cerramos el fichero
f.close()

print("El "+str(n)+"-ésimo número de la sucesión de Fibonacci es: "+str(nNumFibonacci(n)))
