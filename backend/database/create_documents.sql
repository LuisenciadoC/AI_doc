USE gestion_documental;
GO

INSERT INTO documento (titulo, descripcion, codigo_documento, id_area, id_tipo)
VALUES 
('Procedimiento de almacenamiento', 'Guía para almacenamiento de productos', 'DOC-001', 1, 1),
('Control de calidad', 'Procedimiento de control de calidad en bodega', 'DOC-002', 1, 1),
('Gestión de inventarios', 'Manejo de inventarios y stock', 'DOC-003', 2, 1),
('Recepción de mercancía', 'Proceso de recepción de productos', 'DOC-004', 2, 1),
('Desinfección de área', 'Procedimiento de limpieza y desinfección', 'DOC-005', 3, 1);

SELECT * FROM documento;