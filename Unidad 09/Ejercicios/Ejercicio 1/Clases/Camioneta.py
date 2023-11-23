from .Coche import *

class Camioneta(Coche): 
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
        self.clase_vehiculo = "Camioneta"
