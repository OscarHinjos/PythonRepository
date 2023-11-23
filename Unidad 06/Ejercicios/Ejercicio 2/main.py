# **2) Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio: **

import math
PI = math.pi

def area_circulO(radio): 
    return PI*math.pow(radio, 2)

if __name__ == '__main__': 
    print(area_circulO(5))