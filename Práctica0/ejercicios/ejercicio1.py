# ejercicios/ejercicio1.py

import random

NUM_ADIVINAR = random.randint(1,100)	# Constante con el número a adivinar
NUM_INTENTOS = 10 							# Constante con el número de intentos totales
contador = 0  									# Variable contador	
adivinado = False 							# Variable booleana para saber si hemos adivinado el número

print("El siguiente programa es un juego de adivinar un número (entre 1 y 100). Dispone de 10 intentos para ganar. Introduzca un número: ")


# Repetimos mientras no hayamos acertado o nos queden intentos restantes
while contador < NUM_INTENTOS and not adivinado:

	#Contabilizamos el contador
	contador = contador + 1

	try:
		# Leemos el número que introducen 
		numero = int(input())

		# Comprobamos que se trata de un número entero entre 1 y 100
		if numero < 1 or numero > 100 :
			print("El número introducido no es válido. Por favor introduzca un número entre 1 y 100.")
		else:
			if numero >	NUM_ADIVINAR:
				print("El número buscado es menor.")
			else:
				if numero < NUM_ADIVINAR:
					print("El número buscado es mayor.")
				else:
					print("¡Enhorabuena! Ha adivinado el número "+str(NUM_ADIVINAR))
					adivinado = True

	except ValueError:
		print("Por favor introduzca un número entre 1 y 100.")


	# Si hemos gastado el número de intentos pero no hemos adivinado el número
	if contador == NUM_INTENTOS and not adivinado:
		print("¡Ha perdido! Se le han agotado el número de intentos... El número era "+str(NUM_ADIVINAR))
