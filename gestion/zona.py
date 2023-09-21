class Zona:
    def __init__(self,nombre="",zoo=None,animales=[]):
        self._nombre=nombre
        self._zoo= zoo
        self._animales= animales
        
    def agregarAnimales(self,NuevoAnimal):
        self.animales.append(NuevoAnimal)
        
    def cantidadAnimales(self):
        return len(self._animales)
    
    def getNombre(self):
        return self._nombre
    def getZoo(self):
        return self._zoo
    def getAnimales(self):
        return self._animales