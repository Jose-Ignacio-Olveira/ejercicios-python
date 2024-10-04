class Persona:
    def __init__(self, edad:int, sexo:str, trabaja:bool, estudia:bool):
        self.__edad = edad
        self.__sexo = sexo
        self.__trabaja = trabaja
        self.__estudia = estudia
    
    def get_edad(self):
        return self.__edad
    
    def set_edad(self,edad):
        self.__edad = edad
        
    def get_sexo(self):
        return self.__sexo
    
    def set_sexo(self,sexo):
        self.__sexo = sexo
        
    def get_trabaja(self):
        return self.__trabaja
    
    def set_trabaja(self,trabaja):
        self.__trabaja=trabaja
            
    def get_estudia(self):
        return self.__estudia
    
    def set_estudia(self,estudia):
        self.__estudia=estudia
    
    def permiso_trabajo(self):
        if self.__edad < 16 :
            return print("Esta persona no está autorizada a trabajar. (es menor de 16 años)")
        else:
            return print("Esta persona está autorizada a trabajar. (es mayor de 16 años)")
        
    def permiso_conducir(self):
        if self.__edad < 17 :
            return print("Esta persona no tiene permitido manejar un vehículo. (es menor de 17 años)")
        else:
            return print("Esta persona está autorizada a conducir un vehículo. (es mayor de 17 años)")
        
