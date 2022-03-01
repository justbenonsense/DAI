#./app/model.py
from pickleshare import *

import re

db = PickleShareDB('BD')


# ---------------- Añadimos usuario ---------------------
def sign_up_db(username,name,surname,email,password):

    if username in db.keys():
        return False
    else:
        db[username] = dict()
        db[username]['name'] = name
        db[username]['surname'] = surname
        db[username]['email'] = email
        db[username]['password'] = password
        db[username] = db[username]
        return True
 
    return False


# ---------------- Comprobamos si es usuario ---------------------
def is_user_db(username):

    if username in db.keys():
        return True
    
    return False

    

# ---------------- Comprobamos si la contraseña es correcta ---------------------
def right_user_db(username,password):
    
    if db[username]['password'] == password:
        return True
    
    return False
 

# ---------------- Cambiamos nombre del usuario ---------------------
def modify_name_db(username,new_name,new_surname):

    db[username]['name'] = new_name
    db[username]['surname'] = new_surname
    return True

# ---------------- Cambiamos email del usuario ---------------------
def modify_email_db(username,new_email):

    db[username]['email'] = new_email
    return True


# ---------------- Cambiamos contraseña del usuario --------------------
def modify_password_db(username,password,new_password):

    if username in db.keys() and db[username]['password'] == password:
        db[username]['password'] = new_password
        return True
    return False 


# ---------------- Eliminamos usuario --------------------
def delete_username_db(username):

    if username in db.keys():
        db[username].clear()
        del db[username]
        return True
    return False 

