# **2) Localiza el error en el siguiente bloque de código. 
# Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:**


if __name__ == '__main__': 
    try: 
        lista = [1, 2, 3, 4, 5]
        lista[10] # No hay posicion 10
    except IndexError: 
        print("Has elegido un indice que no se encuentra en la lista")