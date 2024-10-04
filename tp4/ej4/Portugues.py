from Idioma import Idioma
class Portugues(Idioma):
    def saludar(self) -> str:
        return "Olá"
    
    def despedirse(self) -> str:
        return "Adeus"
    
    def perdon(self) -> str:
        return "Desculpa"
    
    def pedir_cafe(self) -> str:
        return "Posso tomar um café?"
    
    def cuanto_cuesta(self) -> str:
        return "Quanto custa?"
    
    def donde_queda(self) -> str:
        return "Onde fica?"
