class Pieza:
    def __init__(self, minuto_llegada, estado) -> None:
        self.minuto_llegada = minuto_llegada
        self.estado = estado

    def set_estado(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado
    
    def get_minuto_llegada(self):
        return self.minuto_llegada