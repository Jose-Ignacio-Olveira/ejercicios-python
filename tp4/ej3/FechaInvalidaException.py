class FechaInvalidaException(Exception):
    def __init__(self, message="Fecha inválida. Verifique el día y el mes ingresado."):
        self.message = message
        super().__init__(self.message)
