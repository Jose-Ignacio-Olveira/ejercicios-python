from clase_instrumento import Instrumento

class instrumento_de_cuerdas(Instrumento):
    def __init__(self,nombre):
        super().__init__(nombre,)
        self.__cuerdas = 