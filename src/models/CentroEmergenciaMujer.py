class CentroEmergenciaMujer (object):
    def __init__(self, id, nombre, departamento, provincia, distrito, coordinador, telefono, latitud, longitud,  tipo, distancia):
        self.id = id
        self.nombre = nombre
        self.departamento = departamento
        self.provincia = provincia
        self.distrito = distrito
        self.coordinador = coordinador
        self.telefono= telefono
        self.latitud = float(latitud)
        self.longitud = float(longitud)
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
            source['coordinador'],
            source['telefono'],
            source['latitud'], 
            source['longitud'],   
            source['tipo'], 
            0)

