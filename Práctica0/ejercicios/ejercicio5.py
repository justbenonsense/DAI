# ejercicios/ejercicio5.py

import random

# Genera aleatoriamente una cadena de [ y ].
def generarSecuenciaCorchetes():

	sec = []
	
	tam = random.randint(1,10)	# Tamaño de la secuencia

	for i in range(tam):
		ori = random.randint(0,1) # si es 0 -> [ , si es 1 -> ]

		if ori == 0:
			sec.append("]")
		else:
			sec.append("[")

	return sec


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
	

# Programa principal

sec = generarSecuenciaCorchetes()

if secuenciaBalanceada(sec):
	print("La secuencia ",sec," está balanceada")
else:
	print("La secuencia ",sec," no está balanceada")
