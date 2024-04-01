from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

# Configurar la ubicación de las plantillas
app.template_folder = '/app'

# Configuración de la base de datos
db_config = {
    'host': 'mysql_db',  # Nombre del servicio del contenedor MySQL en la red de Docker Compose
    'port': '3306',
    'user': 'root',
    'password': 'root',
    'database': 'devops_app'  # Conectar automáticamente a la base de datos devops_app
}

def create_database(cursor, db_name):
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")

def get_databases(cursor):
    cursor.execute("SHOW DATABASES")
    return [row[0] for row in cursor.fetchall()]

def get_welcome_data(cursor):
    cursor.execute("SELECT * FROM welcome")
    return cursor.fetchall()

@app.route('/')
def index():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        message = "Bienvenidos a devops_app!"

        cursor.close()
        connection.close()

        return render_template('index.html', message=message)
    except Exception as e:
        return str(e)

@app.route('/welcome')

def welcome():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        welcome_data = get_welcome_data(cursor)

        cursor.close()
        connection.close()

        return jsonify(welcome_data)
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
