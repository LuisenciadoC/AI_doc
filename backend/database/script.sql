USE master;
GO

CREATE DATABASE gestion_documental;
GO

USE gestion_documental;
GO

CREATE TABLE usuarios (
    id INT PRIMARY KEY IDENTITY(1,1),
    nombre VARCHAR(100),
    correo VARCHAR(100),
    password VARCHAR(255)
);
GO

INSERT INTO usuarios(nombre, correo, password)
VALUES(
    'Luis',
    'admin@test.com',
    '123456'
);
GO