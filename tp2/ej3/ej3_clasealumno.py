class Alumno:  
    def __init__(self):
        self.__nombre = ""
        self.__apellido = ""
        self.__dni = 0
    
    @classmethod
    def iniciar_con_nom_ape(cls,nombre, apellido):
        alumno = cls.__new__(cls)
        alumno.__nombre = nombre
        alumno.__apellido = apellido
        return alumno
    
    
    def iniciar(self):
        self.__nombre = "Natalia"
        self.__apellido ="Natalia"
        self.__dni ="0"
        return self
    
    def setNombre(self, Nombre):
        self.__nombre = Nombre
    
    def setApellido(self, Apellido):
        self.__apellido = Apellido
        
    def setDni(self, Dni):
        self.__dni = Dni
        
    def getNombreYapellido(self):
        return f'{self.__nombre}, {self.__apellido}'
    
    def getDni(self):
        return self.__dni
        