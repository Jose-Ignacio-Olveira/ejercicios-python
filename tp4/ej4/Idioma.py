from abc import ABC, abstractmethod

class Idioma(ABC):
    @abstractmethod
    def saludar(self) -> str:
        pass

    @abstractmethod
    def despedirse(self) -> str:
        pass

    @abstractmethod
    def perdon(self) -> str:
        pass

    @abstractmethod
    def pedir_cafe(self) -> str:
        pass

    @abstractmethod
    def cuanto_cuesta(self) -> str:
        pass

    @abstractmethod
    def donde_queda(self) -> str:
        pass
