class Animal:
    totalAnimales=0
    Mamiferos = 0
    Aves = 0
    Reptiles = 0
    Peces = 0
    Anfibios = 0
    
    
    def __init__(self,nombre="",edad=0,habitat="",genero="M"):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        Animal.totalAnimales+=1
        
    def movimiento(self):
        return "desplazarse"
    
    def toString(self):
        return "Mi nombre es "+str(self._nombre)+", tengo una edad de " +str(self._edad)+", habito en "+self._habitat+" y mi genero es "+self._genero
    
    @classmethod
    
    def totalPorTipo(cls):
        return "Mamiferos : "+str(cls.Mamiferos)+"\n" + "Aves : "+str(cls.Aves)+"\n" + "Reptiles : "+str(cls.Reptiles)+"\n" + "Peces : "+str(cls.Peces)+"\n" + "Anfibios : "+str(cls.Anfibios)
    
    def getNombre(self):
        return self._nombre
    def setNombre(self,Nnombre): 
        self._nombre=Nnombre
        
    def getEdad(self):
        return self._edad
    def setNombre(self,Nedad): 
        self._edad=Nedad
        
    def getHabitat(self):
        return self._habitat
    def setNombre(self,Nhabitat): 
        self._habitat=Nhabitat
        
    def getGenero(self):
        return self._genero
    def setNombre(self,Ngenero): 
        self._genero=Ngenero