USE gestion_documental;
GO

CREATE TABLE version_documento (
    id_version INT IDENTITY(1,1) PRIMARY KEY,

    numero_version VARCHAR(10) NOT NULL,
    titulo VARCHAR(200) NOT NULL,
    descripcion TEXT NULL,
    codigo_documento VARCHAR(50) NOT NULL,
    fecha_creacion DATETIME NOT NULL DEFAULT GETDATE(),
    es_vigente BIT NOT NULL DEFAULT 1,
    estado BIT NOT NULL DEFAULT 1,
    archivo_url VARCHAR(500) NULL,
    id_documento INT NOT NULL,

    FOREIGN KEY (id_documento)
    REFERENCES documento(id_documento)
);