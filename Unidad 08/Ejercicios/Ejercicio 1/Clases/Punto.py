# Preparacion 



import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "El punto está en el origen"
        elif self.x > 0 and self.y > 0:
            return "El punto está en el primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "El punto está en el segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "El punto está en el tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "El punto está en el cuarto cuadrante"
        elif self.x == 0 and self.y != 0:
            return "El punto está sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "El punto está sobre el eje X"
    
    def vector(self, otro_punto):
        vector_x = otro_punto.x - self.x
        vector_y = otro_punto.y - self.y
        return f"El vector resultante es ({vector_x}, {vector_y})"
    
    def distancia(self, otro_punto):
        distancia = math.sqrt((otro_punto.x - self.x)**2 + (otro_punto.y - self.y)**2)
        return f"La distancia entre los dos puntos es {distancia}"