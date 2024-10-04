import locale
from FormatoDatos import FormatoDatos
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

class FormatoEEUU(FormatoDatos):
    def formatear_moneda(self, cantidad: float) -> str:
        return locale.currency(cantidad, grouping=True)

    def formatear_fecha(self, dia: int, mes: int, anio: int) -> str:
        return f"{mes:02d}/{dia:02d}/{anio}"
