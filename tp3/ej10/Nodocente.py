from Personal import Personal
import random

class Nodocente(Personal):
    
    def __init__(self, nombre,antiguedad,sector,jornada):
        super().__init__(nombre,antiguedad,sector)
        self.__jornada=jornada
    
    def set_horas_trabajadas (self):
        if self.__categoria == "simple":
            if random.randint(1,100) <= 95:
                self._horas_trabajadas = random.randint(10,20)
        if self.__categoria == "Semiexclusiva":
            if random.randint(1,100) <= 75:
                self._horas_trabajadas= random.randint(20,30)
    
    def get_categoria(self):
        