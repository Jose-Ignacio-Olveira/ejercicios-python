from abc import ABC
class Personaje(ABC):
    def __init__(self,vida,nivelAtaque,nivelDefensa):
        self._vida = vida
        self._nivelAtaque = nivelAtaque
        self._nivelDefensa = nivelDefensa
    
    def get_vida (self):
        return int(self.__vida)
    
    def set_vida(self,vida):
        self.__vida=vida
        
    def get_nivelAtaque(self):
        return int(self._nivelAtaque)
    
    def get_nivelDefensa(self):
        return int(self.__nivelDefensa)
    
    def atacar(self):
        return self._nivelAtaque
    
    def defender(self):
        pass
    
    
    

