from flask import Flask, request
import logging  

app = Flask(__name__)

##Suprimir mensajes de informacion
log = logging.getLogger('werkzeug')
log.setLevel(logging.WARNING)

##Simulacion de una base de datos de usuarios
database = {
    "users": [
        {"username": "admin", "password": "admin123"},
        {"username": "user1", "password": "password12345"},
        {"username": "user89", "password": "mysupersecretpassword"}
    ]
}

@app.route('/vulnerable', methods=['GET'])
def vulnerable():
    user_input = request.args.get('input', '')

    if user_input == "' OR '1'='1 --":
        return "Acceso concedido", 200
    
    ##Obtiene los datos de la base de datos
    elif user_input == "' UNION SELECT username, password FROM users --":
        users_data = "\n".join([f"{user['username']} : {user['password']}" for user in database['users']])
        return f"Datos obtenidos:\n{users_data}", 200
    
    elif user_input == "' AND '1'='1 --":
        return "Acceso concedido", 200
    
    ##Falla a proposito para demostrar los errores
    elif user_input in ["' UNION SELECT NULL --", "'UNION SELECT * FROM nonexistent_table --"]:
        return "Error en la consulta", 400
    
    ##Elimina la base de datos
    elif user_input == "'; DROP TABLE users; --":
        del database["users"]
        return "Base de datos eliminada", 200
    
    return "Consulta no valida", 400

##Funcion para correr la aplicacion web
def run_app():
    app.run(port=5000)

if __name__ == '__main__':
    run_app()