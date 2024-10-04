from clase_familia import Familia
from clase_persona import Persona

class Censo:
    
    def __init__(self,ciudad):
        self.__ciudad =ciudad
        self.__familias = []
    
    def get_ciudad(self):
        return self.__ciudad
    
    def set_ciudad(self,ciudad):
        self.__ciudad = ciudad
    
    def agregar_familia(self,familia):
        self.__familias.append(familia)
    
    def cantidad_familias(self):
        return int(len(self.__familias))
    
    def cantidad_personas_censo(self):
        suma = 0
        for i in self.__familias:
            cant = i.cantidad_personas()
            suma = suma + cant
        return suma
    
    def promedio_edad(self):
        suma_p = 0
        for i in self.__familias:
            for j in i.get_integrantes():
                suma_p = suma_p + j.get_edad()
        promedio = suma_p / self.cantidad_personas_censo()
        return promedio
    
    def cantidad_trabajadores(self):
        suma_t = 0
        for i in self.__familias:
            for j in i.get_integrantes():
                if j.get_trabaja()==True:
                    suma_t += 1
        return suma_t
        
        
    
    