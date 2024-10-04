
from Personaje import Personaje

class Asesino(Personaje):
    def __init__(self, nombre ):
        super().__init__(vida = 300  , nivelAtaque = 50 , nivelDefensa=100)
        self.__nombre = nombre
    
    def get_nombre(self):
        return self.__nombre

    def atacar(self):
        return self.get_nivelAtaque() * 2
    
    def defender(self):
        if self.get_vida()<(self.get_vida()/2):
            return self.get_nivelDefensa()
        else:
            return self.get_nivelDefensa() * 0.05