class Zoologico:
    def __init__ (self,nombre="",ubicacion="",zonas=None):
        self._nombre= nombre
        self._ubicacion=ubicacion
        if zonas is None:
            zonas = []
        self._zonas = zonas
        
    def agregarZonas(self,NuevaZona):
        self._zonas.append(NuevaZona)
        
    def cantidadTotalAnimales(self):
        TotalAnimales: 0
        for area in self._zonas:
            TotalAnimales +=area.cantidadAnimales()
        return TotalAnimales
    
    def getZonas(self):
        return self._zonas
    def getNombre(self):
        return self._nombre
    def getUbicacion(self):
        return self._ubicacion