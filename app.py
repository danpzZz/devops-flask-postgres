import os
import psycopg2
from flask import Flask

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "Sistema de Productos")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

DB_NAME = os.getenv("DB_NAME", "empresa")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "admin123")
DB_HOST = os.getenv("DB_HOST", "db")


@app.route("/")
def inicio():
    try:
        conexion = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        conexion.close()

        return f"""
        <h1>{APP_NAME}</h1>
        <h2>Versión {APP_VERSION}</h2>
        <p>Conexión exitosa a PostgreSQL</p>
        """

    except Exception as e:
        return f"Error: {e}"


@app.route("/productos")
def productos():

    conexion = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    cursor = conexion.cursor()

    cursor.execute(
        "SELECT id,nombre,precio,stock FROM productos"
    )

    datos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return str(datos)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)