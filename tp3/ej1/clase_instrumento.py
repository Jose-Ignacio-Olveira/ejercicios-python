class Instrumento:
    def __init__(self,nombre,marca,modelo, descripción, estado, precio):
        self.__nombre = nombre
        self.__marca = marca
        self.__modelo = modelo
        self.__descripción = descripción
        self.__estado = estado
        self.__precio = precio

    def get_nombre(self):
        return self.__nombre

    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def get_estado(self):
        return self.__estado
    
    def get_precio(self):
        return self.__precio
    
    def set_precio(self, nuevo_precio):
        self.__precio = nuevo_precio
        
    def hacer_sonido(self):
        return print("???")


