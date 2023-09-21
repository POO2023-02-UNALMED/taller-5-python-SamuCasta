from zooAnimales.animal import Animal

class Reptil(Animal):
    lista = []
    iguanas = 0
    serpientes =0
    
    def __init__(self,nombre,edad,habitat,genero,colorEscamas,largoCola):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Animal.Reptiles+=1
        Reptil.lista.append(self)
        
    def movimiento(self):
        return "reptar"
        
    @classmethod
    
    def cantidadReptiles(cls):
        return len(cls.lista)
    
    @classmethod
    
    def crearIguana(cls,nombre1,edad1,genero1):
        cls.iguanas +=1
        return Reptil(nombre1,edad1,"humedal",genero1,"verde",3)
    
    @classmethod
    
    def crearSerpiente(cls,nombre1,edad1,genero1):
        cls.serpientes +=1
        return Reptil(nombre1,edad1,"jungla",genero1,"blanco",1)
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def getLargoCola(self):
        return self._largoCola