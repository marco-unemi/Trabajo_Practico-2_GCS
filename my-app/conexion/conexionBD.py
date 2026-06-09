# Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector
import os

def connectionBD():
    try:
        # connection = mysql.connector.connect(
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            passwd=os.getenv("DB_PASSWORD", "NuevaPassword123!"),
            database=os.getenv("DB_NAME", "crud_python"),
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci',
            raise_on_warnings=True,
            port=int(os.getenv("DB_PORT", "3306"))
        )
        if connection.is_connected():
            # print("Conexión exitosa a la BD")
            return connection

    except mysql.connector.Error as error:
        print(f"No se pudo conectar: {error}")
        return None
