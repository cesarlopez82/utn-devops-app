from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Configurar la conexión a la base de datos
db_connection = mysql.connector.connect(
    host="db_server",
    user="root",
    password="root",
    database="devops_app"
)
db_cursor = db_connection.cursor()

# Endpoint para consultar la base de datos y obtener el resultado como JSON
@app.route('/prueba1')
def prueba1():
    query = "SELECT * FROM welcome WHERE description = 'prueba 1'"
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    return jsonify(result)

# Endpoint para consultar la base de datos y obtener el resultado como JSON
@app.route('/prueba2')
def prueba2():
    query = "SELECT * FROM welcome WHERE description = 'prueba 2'"
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
