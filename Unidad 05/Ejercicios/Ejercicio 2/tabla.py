# **2) Crea un script llamado tabla.py que realice las siguientes tareas:**
# * Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.
# * El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.
# * En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.
# * El script contendrá un bucle for que itere el número de veces del primer argumento.
# * Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.
# * Dentro del segundo for ejecuta una instrucción ** print(" * ", end='')**, (end='' evita el salto de línea).
# * Ejecuta el código y observa el resultado.

# ** Ahora intenta deducir dónde y cómo añadir otra instruccion print para dibujar una tabla.**


import sys

if __name__ == '__main__':
    # Verificando la cantidad de argumentos
    if len(sys.argv) != 3:
        print("Uso: python tabla.py [filas] [columnas]")
        print("Ejemplo: python tabla.py 3 5")
    else:
        filas = int(sys.argv[1])
        columnas = int(sys.argv[2])

        # Verificando si los argumentos son números enteros positivos del 1 al 9
        if not (1 <= filas <= 9 and 1 <= columnas <= 9):
            print("Error: Los argumentos deben ser números enteros del 1 al 9.")
        else:
            # Creando la tabla
            for i in range(filas):
                for j in range(columnas):
                    print(" * ", end='')
                print()  # Salto de línea después de cada fila
