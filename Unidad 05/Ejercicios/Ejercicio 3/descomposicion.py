# **3) [Avanzado] Crea un script llamado descomposicion.py que realice las siguientes tareas:**
# * Debe tomar 1 argumento que será un número entero positivo.
# * En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.

# ** El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número:**

# ```
# > 3647
# ```
# ** El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo: **

# ```
# > 0007
#   0040
#   0600
#   3000
# ```
# *Pista: Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. Necesitarás jugar muy bien con los índices y
# realizar muchas conversiones entre tipos cadenas, números y viceversa*


import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python descomposicion.py [numero_entero]")
        print("Ejemplo: python descomposicion.py 3647")
    else:
        numero = sys.argv[1]
        
        if not numero.isdigit() or int(numero) <= 0:
            print("Error: Debes ingresar un número entero positivo.")
        else:
            numero = numero.zfill(4)  # Asegurando que tenga al menos 4 dígitos
            
            for i in range(len(numero)):
                resultado = int(numero[i]) * 10 ** (len(numero) - i - 1)
                print(f"{resultado:04d}")
