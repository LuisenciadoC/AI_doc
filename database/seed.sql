------------------3. INSERTAR DATOS-----------------------------
USE GestionDocumental;
GO
---3.1 Datos rol----------------------------

INSERT INTO Rol(nombre_rol, descripcion)
VALUES
('Administrador', 'Control total del sistema'),
('Supervisor', 'Supervisa procesos documentales'),
('Empleado', 'Acceso básico al sistema'),
('Auditor', 'Consulta historial y trazabilidad');
GO

---3.2 Datos Area-------------------------

INSERT INTO Area (
    nombre_area,
    descripcion,
    estado)
VALUES
('Recursos Humanos','Gestiona procesos del personal',1),
('Ventas','Gestion comercial y ventas',1),
('Logistica','Gestion de almacenamiento y distribucion',1),
('Financiera', 'Gestion financiera', 1),
('Compras', 'Gestion de proveedores', 1),
('Contabilidad','Gestion financiera y contable',1);
GO

---3.3 Datos tipo de documento----------------

INSERT INTO Tipo_documento (
    nombre_tipo,
    descripcion)
VALUES
('Manual','Documentos guía del sistema'),
('Procedimiento','Describe procesos organizacionales'),
('Formato','Plantillas y registros'),
('Politica','Lineamientos organizacionales'),
('Instructivo', 'Guias operativas');
GO

---3.4 Datos estado de version---------------

INSERT INTO Estado_version (nombre_estado)
VALUES
('Borrador'),
('Revision'),
('Aprobado'),
('Rechazado'),
('Obsoleto');
GO

---3.5 Datos de documento--------------------

USE GestionDocumental;
GO

INSERT INTO Documento (titulo, descripcion, codigo_documento, fecha_creacion, id_area, id_tipo, estado)
VALUES
('Procedimiento de almacenamiento de productos',
'Se define el almacenamiento correcto sobre estibas certificadas, con límite de altura según fabricante. En caso de ausencia de especificación, se establece máximo de 40 cajas. Se aplica método FIFO.',
'DOC-001', GETDATE(), 1, 2, 3),

('Control de calidad en recepción de mercancía',
'Se realiza inspección física y documental verificando lote, vencimiento, integridad del empaque y condiciones de transporte antes de ingreso a bodega.',
'DOC-002', GETDATE(), 2, 2, 3),

('Gestión de inventarios en bodega',
'Se establece control en tiempo real mediante sistema ERP con conteos cíclicos semanales y auditorías mensuales de inventario.',
'DOC-003', GETDATE(), 3, 2, 3),

('Recepción de productos farmacéuticos',
'Incluye validación de órdenes de compra, verificación de cadena de frío y registro inmediato en sistema de inventario.',
'DOC-004', GETDATE(), 1, 2, 3),

('Protocolo de limpieza y desinfección',
'Se establecen rutinas diarias de limpieza con registro obligatorio por turno y uso de insumos autorizados por normativa sanitaria.',
'DOC-005', GETDATE(), 3, 1, 2),

('Gestión de devoluciones de clientes',
'Se evalúa estado del producto para determinar reingreso, destrucción o devolución al proveedor según condiciones.',
'DOC-006', GETDATE(), 2, 2, 3),

('Política de seguridad en almacén',
'Acceso restringido mediante credenciales y registro de ingreso/salida de personal autorizado.',
'DOC-007', GETDATE(), 1, 4, 3),

('Gestión de pedidos y despachos',
'Se realiza verificación doble entre sistema y físico antes de despacho para evitar errores logísticos.',
'DOC-008', GETDATE(), 2, 2, 3),

('Control de temperatura en almacenamiento',
'Monitoreo continuo mediante sensores digitales con alertas automáticas por desviaciones.',
'DOC-009', GETDATE(), 3, 1, 3),

('Auditoría interna de procesos',
'Revisión trimestral de cumplimiento documental y operativo con generación de planes de mejora.',
'DOC-010', GETDATE(), 4, 1, 3),

('Manejo de productos vencidos',
'Productos vencidos se segregan y eliminan bajo normativa sanitaria con trazabilidad completa.',
'DOC-011', GETDATE(), 1, 5, 4),

('Capacitación de personal operativo',
'Formación inicial en procesos logísticos, seguridad y manejo de inventarios con evaluación de desempeño.',
'DOC-012', GETDATE(), 4, 1, 3),

('Gestión de proveedores',
'Evaluación de proveedores basada en calidad, cumplimiento y tiempos de entrega.',
'DOC-013', GETDATE(), 5, 4, 3),

('Alistamiento de pedidos',
'Proceso de picking, verificación, embalaje y etiquetado con validación final antes de despacho.',
'DOC-014', GETDATE(), 2, 2, 3),

('Control documental interno',
'Gestión de versiones, responsables y actualización continua de documentos organizacionales.',
'DOC-015', GETDATE(), 4, 4, 3),

('Manejo de incidentes en bodega',
'Registro de incidentes con acciones correctivas y seguimiento de eventos.',
'DOC-016', GETDATE(), 3, 3, 2),

('Seguridad informática',
'Acceso controlado por credenciales individuales y auditoría periódica de accesos.',
'DOC-017', GETDATE(), 4, 4, 3),

('Transporte y distribución',
'Control de rutas, tiempos de entrega y condiciones de transporte según tipo de carga.',
'DOC-018', GETDATE(), 2, 2, 3),

('Almacenamiento de alto riesgo',
'Productos peligrosos se almacenan en zonas aisladas con señalización y protocolos especiales.',
'DOC-019', GETDATE(), 1, 1, 3),

('Mantenimiento de equipos',
'Registro de mantenimiento preventivo y correctivo con historial técnico completo.',
'DOC-020', GETDATE(), 3, 3, 3);
GO

USE GestionDocumental;
GO

-- Mayoría en APROBADO (3)
UPDATE Documento SET id_estado = 3 WHERE id_documento IN (1,2,4,5,7,8,10,12,14,16,18,20);

-- Borrador (1)
UPDATE Documento SET id_estado = 1 WHERE id_documento IN (19);

-- Revisión (2)
UPDATE Documento SET id_estado = 2 WHERE id_documento IN (3);

-- Rechazado (4)
UPDATE Documento SET id_estado = 4 WHERE id_documento IN (6,17);

-- Obsoleto (5)
UPDATE Documento SET id_estado = 5 WHERE id_documento IN (9,11,15,13);
GO