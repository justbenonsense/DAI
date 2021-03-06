#./app/app.py
from flask import Flask, render_template
app = Flask(__name__)

from ejercicios.ejercicios import *
          
@app.route('/')
def hello_world():
  return 'Hello, World!'


# ---------------- Ejercicio 1 ---------------------
# Interface web para los ejercicios 2-6 de la práctica anterior con entrada por URL

# Ej2 - Ordenación
# Método burbuja
@app.route('/ordenacion/burbuja/<string:entrada>')
def show_burbuja(entrada):
	m = entrada.split(',')
	salida = str(burbuja(m)[0])
	tiempo = str(burbuja(m)[1])
	return 'Ordenación método burbuja: '+salida+'\nTiempo empleado(s): '+tiempo      

# Método selección
@app.route('/ordenacion/seleccion/<string:entrada>')
def show_seleccion(entrada):
	m = entrada.split(',')
	salida = str(seleccion(m)[0])
	tiempo = str(seleccion(m)[1])

	return 'Ordenación método selección: '+salida+'\nTiempo empleado(s): '+tiempo      

# Método inserción
@app.route('/ordenacion/insercion/<string:entrada>')
def show_insercion(entrada):        
	m = entrada.split(',')
	salida = str(insercion(m)[0])
	tiempo = str(insercion(m)[1])

	return 'Ordenación método inserción: '+salida+'\nTiempo empleado(s): '+tiempo


# Ej3 - Criba de Eratóstenes
@app.route('/cribaEratostenes/<int:num>')
def show_criba_eratostenes(num):   
	if num <= 0:
		return 'Error. No ha introducido un número natural.'
	else:
		return 'Los números primos menores que '+str(num)+' son: '+str(cribaEratostenes(num)) 


# Ej4 - Sucesión de Fibonacci
@app.route('/fibonacci/<int:num>')
def show_fibonacci(num):
	if num <= 0:
		return 'Error. No ha introducido un número natural.'
	else:
		return 'El '+str(num)+'-ésimo número de la sucesión de Fibonacci es: '+str(nNumFibonacci(num))



# Ej5 - Cadena de [ y ]
@app.route('/cadena/<string:sec>')
def show_cadena(sec):
	if secuenciaBalanceada(list(sec)):
		return 'La secuencia '+sec+' está balanceada'
	else:
		return 'La secuencia '+sec+' no está balanceada'



# Ej6 - Expresiones regulares


# Palabra seguida de un espacio y una letra mayúscula
@app.route('/expresiones/palabramayus/<string:cadena>')
def show_palabra(cadena):
  if palabraSeguidaEspacioyMayus(cadena):
    return cadena+' es una palabra seguida de un espacio y una letra mayúscula'
  else:
    return cadena+' no es una palabra seguida de un espacio y una letra mayúscula'


# Correo electrónico
@app.route('/expresiones/correoelectronico/<string:cadena>')
def show_correo_electronico(cadena):
  if correoValido(cadena):
    return cadena+' es un correo electrónico válido'
  else:
    return cadena+' no es un correo electrónico válido'


# Número de tarjeta de crédito
@app.route('/expresiones/numerotarjeta/<string:cadena>')
def show_numero_tarjeta(cadena):
  if numeroTarjeta(cadena):
    return cadena+' es una tarjeta de crédito'
  else:
    return cadena+' no es una tarjeta de crédito'


# ---------------- Ejercicio 2 ---------------------
# Crear una página con alguna imagen, servidas ambas desde la carpeta static
# He situado una imagen a la carpeta static situada en la carpeta app


# ---------------- Ejercicio 3 ---------------------
# Página para el caso en que una URL no esté definida (error HTTP 404, not found) 
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# ---------------- Ejercicio extra ------------------
@app.route('/svg')
def show_random_svg():
  n = random.randint(0,3)

  if n == 0:
    return render_template('elipse.html')
  elif n == 1:
    return render_template('rectangulo.html')
  elif n == 2:
    return render_template('circulo.html')
  else:       
    return render_template('triangulo.html')
