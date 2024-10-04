import locale
from FormatoDatos import FormatoDatos
locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')

class FormatoArgentina(FormatoDatos):
    def formatear_moneda(self, cantidad: float) -> str:
        return locale.currency(cantidad, grouping=True)

    def formatear_fecha(self, dia: int, mes: int, anio: int) -> str:
        return f"{dia:02d}/{mes:02d}/{anio}"
