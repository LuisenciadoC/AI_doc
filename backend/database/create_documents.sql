--Insertar documentos de ejemplo en la tabla documento
USE gestion_documental;
GO

INSERT INTO documento (titulo, descripcion, codigo_documento, id_area, id_tipo)
VALUES 
('Procedimiento de almacenamiento', 'Guía para almacenamiento de productos', 'DOC-001', 1, 1),
('Control de calidad', 'Procedimiento de control de calidad en bodega', 'DOC-002', 1, 1),
('Gestión de inventarios', 'Manejo de inventarios y stock', 'DOC-003', 2, 1),
('Recepción de mercancía', 'Proceso de recepción de productos', 'DOC-004', 2, 1),
('Desinfección de área', 'Procedimiento de limpieza y desinfección', 'DOC-005', 3, 1);

USE gestion_documental;
SELECT * FROM documento;
GO

--Actualizar las fechas de creación para simular documentos con diferentes tiempos de antigüedad
USE gestion_documental;

UPDATE documento
SET fecha_creacion = DATEADD(DAY, -5, GETDATE())
WHERE codigo_documento = 'DOC-001';

UPDATE documento
SET fecha_creacion = DATEADD(DAY, -3, GETDATE())
WHERE codigo_documento = 'DOC-002';

UPDATE documento
SET fecha_creacion = DATEADD(HOUR, -40, GETDATE())
WHERE codigo_documento = 'DOC-003';

UPDATE documento
SET fecha_creacion = DATEADD(HOUR, -10, GETDATE())
WHERE codigo_documento = 'DOC-004';

UPDATE documento
SET fecha_creacion = DATEADD(HOUR, -1, GETDATE())
WHERE codigo_documento = 'DOC-005';
GO

UPDATE documento
SET fecha_creacion = DATEADD(HOUR, -50, GETDATE())
WHERE codigo_documento = 'DOC-006';
GO

SELECT 
    id_documento,
    titulo,
    codigo_documento,
    fecha_creacion,
    estado
FROM documento;
GO