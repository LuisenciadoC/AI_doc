from app.config.db import get_connection
# Importamos la conexión a SQL Server

class UserRepository:

    # Crear usuario
    def create_user(
        self,
        nombre,
        correo,
        contrasena,
        id_rol
    ):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO usuario
        (
            nombre,
            correo,
            contrasena,
            estado,
            fecha_creacion,
            id_rol
        )
        VALUES (?, ?, ?, ?, GETDATE(), ?)
        """

        cursor.execute(
            query,
            (
                nombre,
                correo,
                contrasena,
                1,
                id_rol
            )
        )

        conn.commit()
    
    def get_by_email(self, correo):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT *
        FROM usuario
        WHERE correo = ?
        """

        cursor.execute(query, (correo,))

        row = cursor.fetchone()

        if row:

            return {
                "id_usuario": row[0],
                "nombre": row[1],
                "correo": row[2],
                "contrasena": row[3],
                "estado": row[4],
                "fecha_creacion": row[5],
                "id_rol": row[6],
                "fecha_actualizacion": row[7]
            }

        return None