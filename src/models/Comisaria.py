class Comisaria (object):
    def __init__( self, id, codigo, departamento, distrito, divpol_divopus, latitud, longitud, macroregion, nombre, provincia, regionpolicial, rural, sectorial, tipo, tipocomisaria, zonal, distancia):
        self.id=id
        self.codigo = codigo 
        self.nombre = nombre
        self.departamento = departamento
        self.provincia = provincia
        self.distrito = distrito
        self.regionpolicial = regionpolicial
        self.divpol_divopus = divpol_divopus
        self.macroregion = macroregion
        self.tipocomisaria = tipocomisaria  
        self.sectorial = sectorial
        self.zonal = zonal
        self.rural = rural
        self.latitud = latitud
        self.longitud = longitud
        self.tipo = tipo
        self.distancia=distancia

    def setDistancia(self,distancia):
        self.distancia=distancia
    
    @staticmethod
    def from_dict(id,source):
        return Comisaria (
            id, 
            source['codigo'], 
            source['departamento'], 
            source['distrito'], 
            source['divpol_divopus'], 
            source['latitud'], 
            source['longitud'], 
            source['macroregion'], 
            source['nombre'], 
            source['provincia'], 
            source['regionpolicial'], 
            source['rural'], 
            source['sectorial'], 
            source['tipo'], 
            source['tipocomisaria'], 
            source['zonal'],
            0)


