class EtapaEnfriado():
    def __init__(self, nombre="Enfriado", estado=False, cantidad_piezas=0) -> None:
        self.nombre = nombre
        self.estado = estado
        self.cantidad_piezas = cantidad_piezas

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