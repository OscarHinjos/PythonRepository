from .Bicicleta import *


class Motocicleta(Bicicleta): 
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        self.clase_vehiculo = "Motocicleta"