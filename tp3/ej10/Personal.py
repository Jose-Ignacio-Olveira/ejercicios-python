from abc import ABC

class Personal(ABC):
    def __init__(self,nombre,antiguedad,sector):
        self._nombre = nombre 
        self._antiguedad = antiguedad
        self._sector = sector
        self._horas_trabajadas= 0.0

    def set_horas_trabajadas(self, horas):
        self._horas_trabajadas = horas
        