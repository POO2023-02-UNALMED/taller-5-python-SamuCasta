from zooAnimales.animal import Animal

class Mamifero(Animal):
    lista = []
    caballos = 0
    leones=0
    
    def __init__(self,nombre,edad,habitat,genero,pelaje,patas):
        super().__init__(nombre,edad,habitat,genero)
        self._pelaje = pelaje
        self._patas = patas
        Animal.Mamiferos+=1
        Mamifero.lista.append(self)
        
    @classmethod
    
    def cantidadMamiferos(cls):
        return len(cls.lista)
    
    @classmethod
    
    def crearCaballo(cls,nombre1,edad1,genero1):
        cls.caballos +=1
        return Mamifero(nombre1,edad1,"pradera",genero1,True,4)
    
    @classmethod
    
    def crearLeon(cls,nombre1,edad1,genero1):
        cls.leones +=1
        return Mamifero(nombre1,edad1,"selva",genero1,True,4)
    
    def getPatas(self):
        return self._patas
    
    def isPelaje(self):
        return self._pelaje