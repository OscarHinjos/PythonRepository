# **5) Realiza una función llamada agregar_una_vez() que reciba una lista y un elemento. 
# La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. 
# Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:**


def agregar_una_vez(lista_elementos, elemento):
    try:
        if elemento in lista_elementos:
            raise ValueError("El elemento ya se encuentra en la lista")
        else: 
            lista_elementos.append(elemento)
    except ValueError as ve: 
        print(f"Error: {ve}")

if __name__ == '__main__': 
    elementos = [1, 5, -2]
    try:
        agregar_una_vez(elementos, 5)
    except ValueError as ve:
        print(f"Mensaje capturado: {ve}")

    print(elementos)  # Comprobación del resultado
