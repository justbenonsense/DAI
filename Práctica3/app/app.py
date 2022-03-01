#./app/app.py
from flask import Flask, render_template, request, flash, url_for, session, redirect, jsonify
from ejercicios.ejercicios import *
from model import *  
from pymongo import MongoClient

client = MongoClient("mongo", 27017) # Conectar al servicio (docker) "mongo" en su puerto estandar
db2 = client.SampleCollections        # Elegimos la base de datos de ejemplo

app = Flask(__name__)

app.secret_key = 'my_secret_key'

# ---------------- Página principal ---------------------
@app.route('/')
def index():
    return render_template('index.html')


# ---------------- Login ---------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']
      
      if is_user_db(username): 
        if right_user_db(username,password):
          name = db[username]['name']
          session['username'] = username
          session['password'] = password
          session['urls'] = []
          session['names'] = []
          flash('¡Bienvenid@, '+ name + '!')
          return redirect(url_for('index'))
        else:
          error = "Contraseña incorrecta."
      else:
          error = 'Usuario incorrecto. Regístrese.'
          return render_template('signup.html', error=error)

  return render_template('login.html', error=error)


# ---------------- Logout ---------------------
@app.route('/logout')
def logout():
  error = None
  if 'username' in session:
    session.clear()
    flash('Sesión cerrada')
          
  return redirect(url_for('index'))


# ---------------- Signup ---------------------
@app.route('/signup', methods=['GET', 'POST'])
def signup():
  error = None
  if request.method == 'POST':
      username = request.form['username']
      name = request.form['name']
      surname = request.form['surname']
      email = request.form['email']
      password = request.form['password']

      if sign_up_db(username, name, surname, email, password):
         
          flash('Nuevo usuario '+request.form['username']+' registrado correctamente. Inicie sesión.')
          return redirect(url_for('index'))
      else:
          error = 'Ese usuario ya está registrado. Introduzca otro.'
  
  return render_template('signup.html',error=error)

# ---------------- Perfil ---------------------
@app.route('/perfil')
def perfil():
  
  if 'username' in session:
    username = session['username']
    name = db[username]['name']
    surname = db[username]['surname']
    email = db[username]['email']
  else:
    return render_template('perfil.html')
  
  store_visted_urls(request.url, 'Cambiar contraseña')

  return render_template('perfil.html', username=username, name=name, surname=surname, email=email)


# ---------------- Darse de baja ---------------------
@app.route('/delete', methods=['GET', 'POST'])
def delete():
  
  if 'username' in session:
    username=session['username']
    delete_username_db(username)
    session.clear()
    flash('Usuario '+username+' eliminado correctamente.')

  return redirect(url_for('index'))

# ---------------- Cambiar nombre ---------------------
@app.route('/change_name', methods=['GET', 'POST'])
def change_name():
  error = None
  if request.method == 'POST':
    username=session['username']
    password=request.form['password']
    new_name=request.form['new_name']
    new_surname=request.form['new_surname']

    if password == db[username]['password']:

      if modify_name_db(username,new_name,new_surname):
        flash("El nombre ha sido modificado.")
        return redirect(url_for('index'))
    else:
      error = 'Contraseña incorrecta.'
  
  store_visted_urls(request.url, 'Cambiar nombre')
  return render_template('new_name.html', error=error)

# ---------------- Cambiar email ---------------------
@app.route('/change_email', methods=['GET', 'POST'])
def change_email():
  error = None
  if request.method == 'POST':
    username=session['username']
    password=request.form['password']
    new_email=request.form['new_email']

    if password == db[username]['password']:

      if modify_email_db(username,new_email):
        flash("El correo electrónico ha sido modificado.")
        return redirect(url_for('index'))
    else:
      error = 'Contraseña incorrecta.'
  
  store_visted_urls(request.url, 'Cambiar email')
  return render_template('new_email.html', error=error)


# ---------------- Cambiar contraseña ---------------------
@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
  error = None
  if request.method == 'POST':
    username=session['username']
    password=request.form['password']
    new_password1=request.form['new_password1']
    new_password2=request.form['new_password2']
    
    if new_password1 == new_password2:

      if modify_password_db(username,password,new_password1):
        flash("La contraseña ha sido modificada.")
        return redirect(url_for('index'))
      else:
        error = 'Contraseña incorrecta.'
    else:
        error = 'Las contraseñas introducidas no coinciden.'
  
  store_visted_urls(request.url, 'Cambiar contraseña')
  return render_template('new_password.html', error=error)


# ---------------- Historial reciente ---------------------
def store_visted_urls(url, name):
    if 'urls' in session:
        session['urls']=[url]+session['urls']
        session['names']=[name]+session['names']
        if len(session['urls']) > 3:
            session['urls'].pop(3)
            session['names'].pop(3)
        session.modified = True


# ---------------- Ejercicios Práctica 1 ---------------------
# Ej1 - Adivina el número
@app.route('/adivina', methods=['GET', 'POST'])
def adivina():
  store_visted_urls(request.url, 'Adivina')
  global num,intentos
  mostrar = -1
  error=None

  if request.method == 'POST':
    modo=request.form["modo"]
    
    if "Comenzar" == modo or "comenzar" == modo:
      num = random.randint(1,100)	# Constante con el número a adivinar
      intentos = 0
      mostrar = 0
      flash("Comienza el juego! Dispone de 10 intentos para ganar.")
    
    elif "No" == modo or "no" == modo:
      error = None
    else:
      if "Continuar" == modo or "continuar" == modo:

        if request.form["entrada"]:
          entrada=request.form["entrada"]
          entrada=int(entrada)
          intentos = intentos + 1
          disp = 10 - intentos
          if disp >= 0:
            message = "Dispone de "+str(disp)+" intentos adicionales para ganar."
            flash(message)

          if intentos < 11:
            if entrada < 1 or entrada > 100:
              mostrar=0
              error = "El número debe estar en el intervalo [1,100]."
            else:
              if entrada > num:
                mostrar = 1
              elif entrada < num:
                mostrar = 2
              elif entrada == num:
                mostrar = 3
          else:
            error = "Empiece de nuevo el juego..."
            mostrar=4
          
          return render_template('adivina.html', mostrar=mostrar, error=error, solucion=num)
        else:
          error = "Introduzca un modo de juego válido..."
      else:
        error = "Introduzca un modo de juego válido..."
      

  return render_template('adivina.html', error=error, mostrar=mostrar)

# Ej2 - Ordenación
@app.route('/ordenacion', methods=['GET', 'POST'])
def ordenacion():
  store_visted_urls(request.url, 'Ordenacion')
  error=None
  if request.method == 'POST':
    entrada=request.form["entrada"]
    entrada=list(map(int,entrada.split(",")))

    metodo=request.form["metodo"]

    if "burbuja" == metodo:
      return render_template('ordenacion.html', mostrar=True, metodo=metodo, sol=burbuja(entrada)[0], tiempo=burbuja(entrada)[1])
    elif "selección" == metodo or "seleccion" == metodo:
      return render_template('ordenacion.html', mostrar=True, metodo=metodo, sol=seleccion(entrada)[0], tiempo=seleccion(entrada)[1])
    elif "inserción" == metodo or "insercion" == metodo:
      return render_template('ordenacion.html', mostrar=True, metodo=metodo, sol=insercion(entrada)[0], tiempo=insercion(entrada)[1])
    else:
      error="El método de ordenación no es correcto"
  
  return render_template('ordenacion.html', mostrar=False, error=error)

# Ej3 - Criba de Eratóstenes
@app.route('/criba_eratostenes', methods=['GET', 'POST'])
def criba():
    store_visted_urls(request.url, 'Criba')
    error= None
    if request.method == 'POST':
        num = request.form["numero"]
        num = int(num)
        if num > 1:
          return render_template('criba.html', mostrar=True, num=num, primos=cribaEratostenes(num))
        else:
          error="El número no es natural mayor que 1."

    return render_template('criba.html', mostrar=False, error=error)


# Ej4 - Sucesión de Fibonacci
@app.route('/fibonacci', methods=['GET', 'POST'])
def fibonacci():
  store_visted_urls(request.url, 'Fibonacci')
  error = None
  if request.method == 'POST':
        num = request.form["numero"]
        num = int(num)
        if num > 0:
          return render_template('fibonacci.html', mostrar=True, num=num, res=nNumFibonacci(num))
        else:
          error="El número no es natural."

  return render_template('fibonacci.html', mostrar=False, error=error)


# Ej5 - Secuencia de [ y ]
@app.route('/secuencia_balanceada', methods=['GET', 'POST'])
def secuencia_balanceada():
  store_visted_urls(request.url, 'Secuencia Balanceada')

  if request.method == 'POST':
    sec=request.form["secuencia"]
    if secuenciaBalanceada(sec):         
      balanceado = True
    else:
      balanceado = False
    return render_template('secuencia_balanceada.html', mostrar=True, balanceado=balanceado)

  return render_template('secuencia_balanceada.html', mostrar=False)


# Ej6 - Expresiones regulares
@app.route('/expresion_regular', methods=['GET', 'POST'])
def expresion_regular():
  store_visted_urls(request.url, 'Expresion regular')

  error=None
  if request.method == 'POST':
    entrada=request.form["entrada"]
    metodo=request.form["metodo"]

    if "palabra" == metodo:
      return render_template('expresion_regular.html', mostrar=True, metodo=metodo, sol=palabraSeguidaEspacioyMayus(entrada))
    elif "email" == metodo:
      return render_template('expresion_regular.html', mostrar=True, metodo=metodo, sol=correoValido(entrada))
    elif "tarjeta" == metodo:
      return render_template('expresion_regular.html', mostrar=True, metodo=metodo, sol=numeroTarjeta(entrada))
    else:
      error="El método no es correcto"
  
  return render_template('expresion_regular.html', mostrar=False, error=error)



# ---------------- Ejercicio 3 ---------------------
# Página para el caso en que una URL no esté definida (error HTTP 404, not found) 
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# ---------------- Ejercicio extra ------------------
@app.route('/svg')
def show_random_svg():
  store_visted_urls(request.url, 'Expresion regular')
  n = random.randint(0,3)

  if n == 0:
    return render_template('elipse.html')
  elif n == 1:
    return render_template('rectangulo.html')
  elif n == 2:
    return render_template('circulo.html')
  else:       
    return render_template('triangulo.html')


# ------------------------------------------------------------
# ---------------- BASE DE DATOS MONGO -----------------------
# ------------------------------------------------------------


# ---------------- Mongo ------------------
@app.route('/mongo/pag/<n>', methods=['GET','POST'])
def mongo(n):
  episodios = db2.samples_friends.find().sort([('season', 1), ('episode',1)])
  lista_pagina = []
  num = 0
  cont = 0
  n = int(n)
  size = 0

  for episodio in episodios:
    num = num + 1

  pag = 5
  elementos = num / pag
  elementos = int(elementos)

  if num % pag != 0:
    elementos = elementos + 1

  episodios = db2.samples_friends.find().sort([('season', 1), ('episode',1)])

  for episodio in episodios:
    cont = cont + 1

    if cont <= elementos*n and cont > elementos*(n-1):
      lista_pagina.append(episodio)

  size = cont
  if request.method == 'POST':
    if "buscar" in request.form:
      return redirect(url_for('mongo_buscar'))
    if "insertar" in request.form:
      return redirect(url_for('mongo_insertar'))
    if "modificar" in request.form:
      return redirect(url_for('mongo_modificar'))
    if "eliminar" in request.form:
      return redirect(url_for('mongo_eliminar'))
  
  return render_template('lista.html', episodios=lista_pagina)



# ---------------- Búsqueda en la base de datos ------------------
@app.route('/mongo/buscar', methods=['GET','POST'])
def mongo_buscar():
  if request.method == 'POST':
    atributos = ["id","url","name","season","number","airdate","airtime","runtime"]
    filtros = []

    for i in range(len(atributos)):
      if len(request.form[atributos[i]]) != 0:
        if atributos[i] == "id" or atributos[i] == "season" or atributos[i] == "number" or atributos[i] == "runtime":
          filtro = float(request.form[atributos[i]])
          filtros.append({atributos[i]:filtro})
        else:
          filtro = request.form[atributos[i]]
          filtros.append({atributos[i]:{"$regex":filtro,"$options":'i'}})
    
    if len(filtros) == 0:
      episodios = db2.samples_friends.find() 
    else:
      episodios = db2.samples_friends.find({"$and":filtros}) 
    
    episodios_filtrados = []
      
    for episodio in episodios:
      episodios_filtrados.append(episodio)

    if len(episodios_filtrados)==0:
      flash("No se ha encontrado ningún episodio con los filtros seleccionados.")
    else:
      return render_template('buscar_mongodb.html',mostrar=True,episodios=episodios_filtrados)
  
  return render_template('buscar_mongodb.html',mostrar=False)

# ---------------- Inserción en la base de datos ------------------
@app.route('/mongo/insertar', methods=['GET','POST'])
def mongo_insertar():
  if request.method == 'POST':
    identificador = request.form['id']
    identificador = float(identificador)

    if db2.samples_friends.find_one({"id":identificador}) != None:
      flash("Ya existe un episodio con ese id.")
      return render_template('insertar_mongodb.html')
    else:
      name = request.form['name']
      url = request.form['url']
      season = request.form['season']
      number = request.form['number']
      airdate = request.form['airdate']
      airtime = request.form['airtime']
      airstamp = request.form['airstamp']
      runtime = request.form['runtime']
      summary = request.form['summary']
      image = None

      if number:
        number = float(number)
      if season:
        season = float(season)
      if runtime:
        runtime = float(runtime)

      episodio = {"id":identificador,"name":name,"url":url,"season":season,"number":number,"airdate":airdate,
      "airtime":airtime,"airstamp":airstamp,"runtime":runtime,"summary":summary,"image":image}

      db2.samples_friends.insert_one(episodio)

      flash("Episodio insertado correctamente")
      return redirect(url_for('mongo', n=1)) 

  return render_template('insertar_mongodb.html')

# ---------------- Modificación en la base de datos ------------------
@app.route('/mongo/modificar', methods=['GET','POST'])
def mongo_modificar():
  if request.method == 'POST':
    identificador = request.form['id']
    identificador = float(identificador)

    if db2.samples_friends.find_one({"id":identificador}) != None:
      atributos = ["name","url","season","number","airdate","airtime","airstamp","runtime","summary"]
      atributos_numericos = ["season","number","runtime"]

      for i in range(len(atributos)):
        if len(request.form[atributos[i]]) != 0:
          if atributos[i] in atributos_numericos:
            db2.samples_friends.update(
            {"id":identificador}, {"$set":{atributos[i]:float(request.form[atributos[i]])}})
          else:
            db2.samples_friends.update(
            {"id":identificador}, {"$set":{atributos[i]:request.form[atributos[i]]}})

      flash("Episdodio modificado correctamente")
      return redirect(url_for('mongo', n=1)) 
    else:
      flash("No existe ningún episodio con el id especificado")
      return render_template('modificar_mongodb.html')
    
  return render_template('modificar_mongodb.html')


# ---------------- Eliminación en la base de datos ------------------
@app.route('/mongo/eliminar', methods=['GET','POST'])
def mongo_eliminar():
  if request.method == 'POST':
    name = request.form['name']
    borrados = db2.samples_friends.delete_many( {"name":name} ) 

    if borrados.deleted_count == 0:
      flash("No hay ningún episodio con ese nombre.")
      return render_template('eliminar_mongodb.html')
    else:
      flash("Episodio eliminado correctamente")
      return redirect(url_for('mongo', n=1)) 

  return render_template('eliminar_mongodb.html')


# ------------------------------------------------------------
# ------------------------ API REST --------------------------
# ------------------------------------------------------------

@app.route('/api/episodios', methods=['GET','POST'])
def api_1():
  if request.method == 'GET':
    filtros_numericos = ["id","season","number","runtime"]
    filtros = []

    for key in request.values.keys():
      if key in filtros_numericos:
        filtros.append({key:float(request.values.get(key))})
      else:
        filtros.append({key:{"$regex":request.values.get(key),"$options":'i'}})
    
    if len(filtros) != 0:
      episodios = db2.samples_friends.find({"$and":filtros}).sort('id')
    else:
      episodios = db2.samples_friends.find().sort('id')

    lista_episodios = [{i:episodio[i] for i in ("name","id","url","season","number","airdate","airtime","airstamp","runtime","summary") if i in episodio} for episodio in episodios]

    if len(lista_episodios) == 0:
      return jsonify({'error':'No se ha encontrado ninguna entrada con dichos filtros'}), 404
    return jsonify(lista_episodios)
  
  if request.method == 'POST':
    identificador = request.form.get('id')

    if identificador != None:
      identificador = float(identificador)

      if db2.samples_friends.find_one({"id":identificador}) != None:
        return jsonify({'error':'Ya existe un episodio con ese id'}), 400
      else:
        datos_episodio = {}
        filtros_numericos = ["id","season","number","runtime"]
        
        for key in request.values.keys():
          if key in filtros_numericos:
            datos_episodio[key] = float(request.values.get(key))
          else:
            datos_episodio[key] = request.values.get(key)

        new_id = db2.samples_friends.insert_one(datos_episodio).inserted_id
        episodio = db2.samples_friends.find_one({"id":identificador}, {"_id": new_id})

        return jsonify({**episodio, "_id": str(new_id)})
    else:
      return jsonify({'error':'El nuevo episodio debe tener id'}), 400


@app.route('/api/episodios/<identificador>', methods=['GET','PUT','DELETE'])
def api_2(identificador):
  try:
    resultado = db2.samples_friends.find_one({'id':float(identificador)})
  except:
    return jsonify({'error':'Not found'}), 404
  
  if resultado == None:
    return jsonify({'error':'No existe ningún episodio con ese id'}), 404

  identificador = float(identificador)

  if request.method == 'GET':
    episodio = db2.samples_friends.find_one({'id':(identificador)})
    episodio = {i:episodio[i] for i in ("name","url","season","number","airdate","airtime","airstamp","runtime","summary") if i in episodio}
    episodio['id'] = (identificador)
    return jsonify(episodio)

  if request.method == 'DELETE':
    db2.samples_friends.delete_one({'id':(identificador)}) 
    return jsonify({"id": (identificador)})
  
  if request.method == 'PUT':
    filtros_numericos = ["season","number","runtime"]
    
    for key in request.values.keys():
      if key == "id":
        return jsonify({'error':'No se puede modificar el id'}), 400
      elif key in filtros_numericos:
        db2.samples_friends.update_one(
            {"id":identificador},
            {"$set":{key:float(request.values.get(key))}}
          )
      else:
        db2.samples_friends.update_one(
            {"id":identificador},
            {"$set":{key:request.values.get(key)}}
          )
    
    episodio = db2.samples_friends.find_one({"id":identificador})
    episodio = {i:episodio[i] for i in ("name","url","season","number","airdate","airtime","airstamp","runtime","summary") if i in episodio}
    episodio['id'] = (identificador)
    return jsonify(episodio)