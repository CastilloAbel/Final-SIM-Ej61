class EtapaEnfriado():
    def __init__(self) -> None:
        self.nombre = "Enfriado"
        self.estado = False
        self.cantidad_piezas = 0

    def set_estado(self, estado):
        self.estado = estado

    def agregar_pieza(self):
        self.cantidad_piezas += 1

    def eliminar_pieza(self):
        self.cantidad_piezas -= 1
    
    def get_estado(self):
        return self.estado
    
    def get_piezas(self):
        return self.cantidad_piezas
    
    def get_nombre(self):
        return self.nombre
    
    def __str__(self) -> str:
        return f"Estado: {'Ocupado' if self.get_estado() else 'Libre'}"