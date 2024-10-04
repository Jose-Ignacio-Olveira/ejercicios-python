from Idioma import Idioma
class Frances(Idioma):
    def saludar(self) -> str:
        return "Bonjour"
    
    def despedirse(self) -> str:
        return "Au revoir"
    
    def perdon(self) -> str:
        return "Pardon"
    
    def pedir_cafe(self) -> str:
        return "Puis-je avoir un café?"
    
    def cuanto_cuesta(self) -> str:
        return "Combien ça coûte?"
    
    def donde_queda(self) -> str:
        return "Où est-ce?"
