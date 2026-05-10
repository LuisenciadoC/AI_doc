class Version:
    def __init__(self, id_version, numero_version, fecha_creacion, fecha_aprovacion, es_vigente, 
                 archivo_url, id_documento, id_usuario_creador, id_usuario_aprovador, id_estado):
        self.id_version = id_version
        self.numero_version = numero_version
        self.fecha_creacion = fecha_creacion
        self.fecha_aprovacion = fecha_aprovacion
        self.es_vigente = es_vigente
        self.archivo_url = archivo_url
        self.id_documento = id_documento
        self.id_usuario_creador = id_usuario_creador
        self.id_usuario_aprovador = id_usuario_aprovador
        self.id_estado = id_estado