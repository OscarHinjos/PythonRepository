# **3) Localiza el error en el siguiente bloque de código.  
# Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:**


if __name__ == '__main__': 
    try:
        colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
        colores['blanco']
    except KeyError: 
        print("Has seleccionado un valor que no se encuentra dentro de colores")