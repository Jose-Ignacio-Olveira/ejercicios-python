class Persona:

    def __init__(self,nombre, apellido, fecha_nacimiento):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento= fecha_nacimiento
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre=nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def set_apellido(self,apellido):
        self.__apellido=apellido
    
    def get_fecha(self):
        return self.__fecha_nacimiento
    
    def set_fecha(self,fecha):
        self.__fecha_nacimiento=fecha
        
    def toString(self):
        return print(f'{"NOMBRE: "}{self.__nombre}{" APELLIDO: "}{self.__apellido}{" FECHA DE NACIMIENTO: "}{self.__fecha_nacimiento}')
    
    
    