# **1) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se 
# bloquee y además explica en un mensaje al usuario la causa y/o solución:**


if __name__ == '__main__': 
    try:
        resultado = 10/0
    except ZeroDivisionError:
        print("No puedes dividir entre 0")
        
