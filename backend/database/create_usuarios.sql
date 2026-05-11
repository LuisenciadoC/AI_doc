--Insertar usuarios de ejemplo en la tabla usuarios
USE gestion_documental;
GO

INSERT INTO usuarios (nombre, correo, password, id_rol)
VALUES 
('Diana', 'diana@Helse.com', '12345', 1),
('Luis', 'luis@Helse.com', '12345', 1),
('Juan', 'juan@Helse.com', '12345', 1);
GO


--Actualizar los correos de los usuarios para reflejar el nuevo dominio y establecer una contraseña común
USE gestion_documental;
GO

UPDATE usuarios
SET correo = REPLACE(correo, '@empresa.com', '@Helse.com'),
    password = '12345';

SELECT * FROM usuarios;
GO