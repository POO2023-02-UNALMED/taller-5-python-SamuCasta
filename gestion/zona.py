class Zona():
    def __init__(self, nombre="",zoo=None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales=[]
        
    def agregarAnimales(self,Newanimal):
        self._animales.append(Newanimal)
        
    def cantidadAnimales(self):
        return len(self._animales)
    def getAnimales(self): 
        return self._animales
    def getZoo(self): 
        return self._zoo
    def getNombre(self): 
        return self._nombre