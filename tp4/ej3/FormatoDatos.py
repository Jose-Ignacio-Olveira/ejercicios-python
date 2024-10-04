from abc import ABC, abstractmethod

class FormatoDatos(ABC):
    @abstractmethod
    def formatear_moneda(self, cantidad: float) -> str:
        pass

    @abstractmethod
    def formatear_fecha(self, dia: int, mes: int, anio: int) -> str:
        pass
