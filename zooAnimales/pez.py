from zooAnimales.animal import Animal

class Pez(Animal):
    lista = []
    salmones = 0
    bacalaos =0
    
    def __init__(self,nombre,edad,habitat,genero,colorEscamas,cantidadAletas):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Animal.Peces+=1
        Pez.lista.append(self)
        
    def movimiento(self):
        return "nadar"
        
    @classmethod
    
    def cantidadPeces(cls):
        return len(cls.lista)
    
    @classmethod
    
    def crearSalmon(cls,nombre1,edad1,genero1):
        cls.salmones +=1
        return Pez(nombre1,edad1,"oceano",genero1,"rojo",6)
    
    @classmethod
    
    def crearBacalao(cls,nombre1,edad1,genero1):
        cls.bacalaos +=1
        return Pez(nombre1,edad1,"oceano",genero1,"gris",6)
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def getCantidadAletas(self):
        return self._cantidadAletas