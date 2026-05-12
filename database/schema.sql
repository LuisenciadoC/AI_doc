------1. Creacion de BD-------
CREATE DATABASE GestionDocumental;
GO

USE GestionDocumental;
GO

------2. Cracion de tablas--------------

--------2.1 Tabla Rol---------

CREATE TABLE Rol (
	id_rol INT PRIMARY KEY IDENTITY(1,1),
	nombre_rol VARCHAR(50) NOT NULL UNIQUE,
	descripcion VARCHAR(MAX));
GO

----------2.2 Tabla area-------
CREATE TABLE Area(
	id_area INT PRIMARY KEY IDENTITY(1,1),
	nombre_area VARCHAR(100) not null,
	descripcion VARCHAR(MAX),
	estado bit not null default 1);
GO
----------2.3 Tabla de tipo de documento---------------------------

CREATE TABLE Tipo_documento(
	id_tipo INT PRIMARY KEY IDENTITY(1,1),
	nombre_tipo VARCHAR(100) not null UNIQUE,
	descripcion VARCHAR (max));
GO

------------2.4 Tabla de estado version-------------------------
CREATE TABLE Estado_version(
	id_estado INT PRIMARY KEY IDENTITY(1,1),
	nombre_estado VARCHAR(50) not null UNIQUE);
GO

---------2.5 Tabla de usuario----------------------------------

CREATE TABLE Usuario(
	id_usuario INT PRIMARY KEY IDENTITY(1,1),
	nombre VARCHAR(50) not null,
	correo VARCHAR(150) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    estado BIT NOT NULL DEFAULT 1,
    fecha_creacion DATETIME NOT NULL DEFAULT GETDATE(),
    id_rol INT NOT NULL,
    fecha_actualizacion DATETIME NULL DEFAULT GETDATE(),

    CONSTRAINT FK_Usuario_Rol
    FOREIGN KEY (id_rol)
    REFERENCES Rol(id_rol));
GO

--------------2.6 Tabla documento ---------------------
CREATE TABLE Documento (
    id_documento INT PRIMARY KEY IDENTITY(1,1),
    titulo VARCHAR(200) NOT NULL,
    descripcion VARCHAR(MAX),
    codigo_documento VARCHAR(50) NOT NULL UNIQUE,
    fecha_creacion DATETIME NOT NULL DEFAULT GETDATE(),
    id_area INT NOT NULL,
    id_tipo INT NOT NULL,
    estado BIT NOT NULL DEFAULT 1,
    fecha_actualizacion DATETIME NULL,

    CONSTRAINT FK_Documento_Area
    FOREIGN KEY (id_area)
    REFERENCES Area(id_area),

    CONSTRAINT FK_Documento_Tipo
    FOREIGN KEY (id_tipo)
    REFERENCES Tipo_documento(id_tipo));
GO

-------------2.7 Tabla versiones------------
CREATE TABLE Versiones (
    id_version INT PRIMARY KEY IDENTITY(1,1),
    numero_version INT NOT NULL,
    fecha_creacion DATETIME NOT NULL DEFAULT GETDATE(),
    fecha_aprobacion DATETIME NULL,
    es_vigente BIT NOT NULL DEFAULT 0,
    archivo_url VARCHAR(500),
    id_documento INT NOT NULL,
    id_usuario_creador INT NOT NULL,
    id_usuario_aprobador INT NULL,
    id_estado INT NOT NULL,
    fecha_actualizacion DATETIME NULL,

    CONSTRAINT FK_Version_Documento
    FOREIGN KEY (id_documento)
    REFERENCES Documento(id_documento),

    CONSTRAINT FK_Version_Usuario_Creador
    FOREIGN KEY (id_usuario_creador)
    REFERENCES Usuario(id_usuario),

    CONSTRAINT FK_Version_Usuario_Aprobador
    FOREIGN KEY (id_usuario_aprobador)
    REFERENCES Usuario(id_usuario),

    CONSTRAINT FK_Version_Estado
    FOREIGN KEY (id_estado)
    REFERENCES Estado_version(id_estado));
GO

------------------2.8 Tabla permisos-----------------
CREATE TABLE Permiso (
    id_permiso INT PRIMARY KEY IDENTITY(1,1),
    tipo_permiso VARCHAR(50) NOT NULL,
    id_usuario INT NOT NULL,
    id_documento INT NOT NULL,

    CONSTRAINT FK_Permiso_Usuario
    FOREIGN KEY (id_usuario)
    REFERENCES Usuario(id_usuario),

    CONSTRAINT FK_Permiso_Documento
    FOREIGN KEY (id_documento)
    REFERENCES Documento(id_documento));
GO

---------------------2.9 Tabla hstorial de cambio----------------------
CREATE TABLE Historial_cambio (
    id_historial INT PRIMARY KEY IDENTITY(1,1),
    accion VARCHAR(100) NOT NULL,
    descripcion VARCHAR(MAX),
    fecha DATETIME NOT NULL DEFAULT GETDATE(),
    id_version INT NOT NULL,
    id_usuario INT NOT NULL,

    CONSTRAINT FK_Historial_Version
    FOREIGN KEY (id_version)
    REFERENCES Versiones(id_version),

    CONSTRAINT FK_Historial_Usuario
    FOREIGN KEY (id_usuario)
    REFERENCES Usuario(id_usuario));
GO


USE GestionDocumental;
--Corregir columna estado para eliminar el estado en modo bit
ALTER TABLE Documento
DROP COLUMN estado;

ALTER TABLE Documento
ADD id_estado INT NOT NULL DEFAULT 1;

ALTER TABLE Documento
ADD CONSTRAINT FK_Documento_Estado
FOREIGN KEY (id_estado)
REFERENCES Estado_version(id_estado);