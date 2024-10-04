class Familia:
    
    def __init__(self,apellidoF):
        self.__apellido= apellidoF
        self.__integrantes = []
    
    def get_apellidoF(self):
        return self.__apellido
    
    def set_apellidoF(self,apellido):
        self.__apellido= apellido
    
    def get_integrantes(self):
        return self.__integrantes
    
    def agregar_integrante(self,integrante):
        self.__integrantes.append(integrante)
    
    def cantidad_personas(self):
        return int(len(self.__integrantes))