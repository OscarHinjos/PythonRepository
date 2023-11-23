try:
    from Clases.Punto import Punto
    from Clases.Rectangulo import Rectangulo
except ImportError as e:
    print(f"Error al importar: {e}")

if __name__ == '__main__':
    # Aquí puedes utilizar tus clases importadas
    punto1 = Punto(3, 4)
    punto2 = Punto(-2, 5)

    print(punto1)  # Salida: (3,4)
    print(punto1.cuadrante())  # Salida: El punto está en el primer cuadrante
    print(punto1.vector(punto2))  # Salida: El vector resultante es (-5, 1)
    punto1.distancia(punto2)  # Calcula y muestra la distancia entre los puntos

    # También puedes utilizar la clase Rectangulo si está definida en Clases.py
    mi_rectangulo = Rectangulo((2, 3), (7, 5))
    print(f"Base del rectángulo: {mi_rectangulo.base()}")
    print(f"Altura del rectángulo: {mi_rectangulo.altura()}")
    print(f"Área del rectángulo: {mi_rectangulo.area()}")
