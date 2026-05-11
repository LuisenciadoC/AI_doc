USE gestion_documental;
GO

INSERT INTO documento
(
    titulo,
    descripcion,
    codigo_documento,
    fecha_creacion,
    id_area,
    id_tipo,
    estado
)
VALUES

(
    'Procedimiento de almacenamiento',
    'Los productos deben almacenarse siempre sobre estibas. El maximo permitido debe respetar la indicacion de la caja. Si la caja no indica limite, el maximo permitido es de 60 cajas. El estibado debe realizarse en bloque intercalado y no una caja directamente sobre otra.',
    'DOC-101',
    DATEADD(DAY, -10, GETDATE()),
    1,
    1,
    1
),

(
    'Recepcion de mercancia',
    'Al recibir mercancia se debe verificar el estado de las cajas, fechas de vencimiento, cantidades y lote. Todo producto golpeado o humedo debe reportarse inmediatamente.',
    'DOC-102',
    DATEADD(DAY, -8, GETDATE()),
    1,
    1,
    1
),

(
    'Control de inventarios',
    'El inventario debe validarse diariamente al finalizar la jornada. Las diferencias encontradas deben registrarse y notificarse al supervisor de area.',
    'DOC-103',
    DATEADD(DAY, -6, GETDATE()),
    2,
    1,
    1
),

(
    'Despacho de pedidos',
    'Los pedidos deben organizarse por ruta y validar cantidades antes de despacho. Ningun producto debe salir sin factura autorizada.',
    'DOC-104',
    DATEADD(DAY, -5, GETDATE()),
    2,
    1,
    1
),

(
    'Manejo de cadena de frio',
    'Los productos que requieren refrigeracion deben mantenerse entre 2 y 8 grados centigrados. La temperatura debe registrarse cada 2 horas.',
    'DOC-105',
    DATEADD(DAY, -4, GETDATE()),
    3,
    1,
    1
),

(
    'Limpieza y desinfeccion',
    'Las areas de almacenamiento deben limpiarse diariamente utilizando productos autorizados. Las estibas deben desinfectarse cada semana.',
    'DOC-106',
    DATEADD(DAY, -3, GETDATE()),
    3,
    1,
    1
),

(
    'Control de acceso a bodega',
    'Solo el personal autorizado puede ingresar a la bodega. Toda visita debe registrarse en la bitacora de ingreso.',
    'DOC-107',
    DATEADD(HOUR, -60, GETDATE()),
    1,
    1,
    1
),

(
    'Proceso de devoluciones',
    'Los productos devueltos deben separarse del inventario principal y revisarse antes de autorizar su reingreso.',
    'DOC-108',
    DATEADD(HOUR, -30, GETDATE()),
    2,
    1,
    1
),

(
    'Uso de elementos de proteccion',
    'Todo trabajador debe utilizar guantes, uniforme y elementos de proteccion personal dentro de la bodega.',
    'DOC-109',
    DATEADD(HOUR, -12, GETDATE()),
    3,
    1,
    1
),

(
    'Procedimiento de alistamiento',
    'El alistamiento debe realizarse siguiendo el orden de la factura y verificando lote, referencia y cantidad antes del empaque.',
    'DOC-110',
    DATEADD(HOUR, -2, GETDATE()),
    2,
    1,
    1
);

SELECT 
    id_documento,
    titulo,
    codigo_documento,
    fecha_creacion,
    estado
FROM documento;