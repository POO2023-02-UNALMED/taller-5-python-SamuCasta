from zooAnimales.animal import Animal

class Anfibio(Animal):
    lista = []
    ranas = 0
    salamandras =0
    
    def __init__(self,nombre,edad,habitat,genero,colorPiel,venenoso):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Animal.Anfibios+=1
        Anfibio.lista.append(self)
        
    def movimiento(self):
        return "saltar"
        
    @classmethod
    
    def cantidadAnfibios(cls):
        return len(cls.lista)
    
    @classmethod
    
    def crearRana(cls,nombre1,edad1,genero1):
        cls.ranas +=1
        return Anfibio(nombre1,edad1,"selva",genero1,"rojo",True)
    
    @classmethod
    
    def crearSalamandra(cls,nombre1,edad1,genero1):
        cls.salamandras +=1
        return Anfibio(nombre1,edad1,"selva",genero1,"negro y amarillo",False)
    
    def getColorPiel(self):
        self._colorPiel
        
    def isVenenoso(self):
        self._venenoso