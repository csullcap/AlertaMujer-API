class CentroEmergenciaMujer (object):
    def __init__(self, id, nombre, departamento, provincia, distrito, direccion,coordinador, telefono, latitud, longitud,  tipo, distancia):
        self.id = id
        self.nombre = nombre
        self.departamento = departamento
        self.provincia = provincia
        self.distrito = distrito
        self.direccion = direccion
        self.coordinador = coordinador
        self.telefono= telefono
        self.latitud = latitud
        self.longitud = longitud
        self.tipo = tipo
        self.distancia = distancia

    def setDistancia(self,distancia):
        self.distancia=distancia
    
    @staticmethod
    def from_dict(id,source):
        return CentroEmergenciaMujer(
            id, 
            source['nombre'], 
            source['departamento'], 
            source['provincia'],
            source['distrito'],
            source['direccion'], 
            source['coordinador'],
            source['telefono'],
            source['latitud'], 
            source['longitud'],   
            source['tipo'], 
            0)

