# **4) Localiza el error en el siguiente bloque de código.
# Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:**


if __name__ == '__main__': 
    try:
        resultado = 15 + "20"
    except TypeError as e:
        print(f"Error: {e}. No se puede realizar la operación entre un número y una cadena de texto.")
        print("Por favor, asegúrate de realizar operaciones con tipos de datos compatibles.")
