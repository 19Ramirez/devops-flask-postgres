from flask import Flask
import psycopg2

app = Flask(__name__)

VERSION = "3.0.0"

@app.route("/")
def inicio():
    try:
        conexion = psycopg2.connect(
            host="db",
            database="empresa",
            user="admin",
            password="admin123"
        )

        cursor = conexion.cursor()

        cursor.execute("SELECT version();")
        version = cursor.fetchone()

        cursor.execute("SELECT id, nombre FROM clientes;")
        clientes = cursor.fetchall()

        cursor.close()
        conexion.close()

        # Generar lista de clientes en HTML
        lista_clientes = "<ul>"
        for cliente in clientes:
            lista_clientes += f"<li>ID: {cliente[0]} - Nombre: {cliente[1]}</li>"
        lista_clientes += "</ul>"

        return f"""
        <h1>Aplicación Flask</h1>
        <h2>Versión {VERSION}</h2>
        <p>Conexión exitosa a PostgreSQL</p>
        <p>{version}</p>
        <h3>Lista de Clientes:</h3>
        {lista_clientes}
        """

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)