class EtapaTerminado():
    def __init__(self) -> None:
        self.nombre = "Terminado"
        self.estado = False
        self.cola = []

    def set_estado(self, estado):
        self.estado = estado
        
    def get_estado(self):
        return self.estado
    
    def get_nombre(self):
        return self.nombre
    
    def set_cola(self, c):
        self.cola = c
        
    def get_cola(self)->list:
        return self.cola
    def __str__(self) -> str:
        return f"Estado: {'Ocupado' if self.get_estado() else 'Libre'}"