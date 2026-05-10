from app.config.db import get_connection
# Importamos la conexión a SQL Server

class UserRepository:

    def get_by_email(self, correo):

        # Abrimos conexión con la base de datos
        connection = get_connection()

        # Cursor: permite ejecutar consultas SQL
        cursor = connection.cursor()

        # Consulta SQL parametrizada (evita SQL Injection)
        query = "SELECT * FROM usuarios WHERE correo = ?"

        # Ejecutamos la consulta con el parámetro seguro
        cursor.execute(query, (correo,))

        # Obtenemos un solo resultado
        row = cursor.fetchone()

        # Si existe el usuario, lo convertimos a diccionario
        if row:
            return {
                "id_usuario": row[0],
                "nombre": row[1],
                "correo": row[2],
                "contraseña": row[3],
                "id_rol": row[4]
            }

        # Si no existe, devolvemos None
        return None