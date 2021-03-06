# ejercicios/ejercicio6.py

import re

# Identifica cualquier palabra seguida de un espacio y una única letra mayúscula (por ejemplo: Apellido N).
def palabraSeguidaEspacioyMayus(cadena):

	return bool(re.match(r'\w+\s+[A-Z]', cadena))


# Identifica correos electrónicos válidos (empieza por una expresión genérica y ve refinándola todo lo posible)
def correoValido(cadena):

	return bool(re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$', cadena))


# Identifica números de tarjeta de crédito cuyos dígitos estén separados por - o espacios en blanco cada paquete de cuatro dígitos: 1234-5678-9012-3456 ó 1234 5678 9012 3456.	
def numeroTarjeta(cadena):

	return bool(re.match(r'\d{4}[\s|-]+\d{4}[\s|-]+\d{4}[\s|-]+\d{4}', cadena))


# Programa principal

