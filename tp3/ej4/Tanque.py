from Personaje import Personaje

class Tanque(Personaje):
    def __init__(self, nombre ):
        super().__init__(vida = 500  , nivelAtaque = 20, nivelDefensa=100)
        self.__nombre = nombre
        
    def get_nombre(self):
        return self.__nombre

    def atacar(self):
        if self.get_vida()<(self.get_vida()/2):
            return self._nivelAtaque * 2
        else:
            return self.get_nivelAtaque()
    
    def defender(self):
        if self.get_vida()<(self.get_vida()/2):
            return self.get_nivelDefensa() * 0.05
        else:
            return self.get_nivelDefensa() * 0.15
    