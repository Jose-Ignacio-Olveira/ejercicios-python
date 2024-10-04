from clase_persona import Persona

class Empresa:
    def __init__(self,nombre,direccion):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__empleados = []
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
    
    def get_direccion(self):
        return self.__direccion
    
    def set_direccion(self, direccion):
        self.__direccion = direccion
    
    def agregar_empleado(self, empleado):
        self.__empleados.append(empleado)
    
    def cantidad_empleados(self):
        return len(self.__empleados)
    
    def datos_empleados(self):
        for i in self.__empleados:
            print(f'{"Nombre: "}{i.get_nombre()}')
            print(f'{"Apellido: " }{i.get_apellido()}')
            print(f'{"Sexo: "}{i.get_sexo()}')
            print("-----------------------------------")
    
