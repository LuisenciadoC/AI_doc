--Crear la tabla documento en la base de datos gestion_documental
USE gestion_documental;
GO

CREATE TABLE documento (
    id_documento INT IDENTITY(1,1) PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    descripcion TEXT NULL,
    codigo_documento VARCHAR(50) NOT NULL UNIQUE,
    fecha_creacion DATETIME NOT NULL DEFAULT GETDATE(),
    id_area INT NOT NULL,
    id_tipo INT NOT NULL
);
GO

--Agregar columna estado para indicar si el documento está activo o inactivo (Soft delete)
USE gestion_documental;

ALTER TABLE documento
ADD estado BIT NOT NULL DEFAULT 1;
GO