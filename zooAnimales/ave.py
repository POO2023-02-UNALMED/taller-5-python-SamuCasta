from zooAnimales.animal import Animal

class Ave(Animal):
    Aves=0
    lista = []
    halcones = 0
    aguilas =0
    
    def __init__(self,nombre,edad,habitat,genero,colorPlumas):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPlumas = colorPlumas
        Ave.Aves+=1
        Ave.lista.append(self)
        
    def movimiento(self):
        return "volar"
        
    @classmethod
    
    def cantidadAves(cls):
        return len(cls.lista)
    
    @classmethod
    
    def crearHalcon(cls,nombre1,edad1,genero1):
        cls.halcones +=1
        return Ave(nombre1,edad1,"montanas",genero1,"cafe glorioso")
    
    @classmethod
    
    def crearAguila(cls,nombre1,edad1,genero1):
        cls.aguilas +=1
        return Ave(nombre1,edad1,"montanas",genero1,"blanco y amarillo")
    
    def getColorPlumas(self):
        return self._colorPlumas