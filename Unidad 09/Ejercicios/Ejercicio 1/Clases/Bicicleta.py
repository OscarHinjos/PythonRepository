from .Vehiculo import *

class Bicicleta(Vehiculo): 
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
        self.clase_vehiculo = "Bicileta"