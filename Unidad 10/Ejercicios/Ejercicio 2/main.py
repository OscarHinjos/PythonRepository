# **2) Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:**

# * Borrar los elementos duplicados
# * Ordenar la lista de mayor a menor
# * Eliminar todos los números impares
# * Realizar una suma de todos los números que quedan
# * Añadir como primer elemento de la lista la suma realizada
# * Devolver la lista modificada
# * Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista, tal que así:
# ```python
# nueva_lista = modificar(lista)
# print( nueva_lista[0] == sum(nueva_lista[1:]) )
# > True
# ```

# *Nota: La función sum(lista) devuelve una suma de los elementos de una lista*

def modificar(lista): 
    # Copia la lista original para no modificarla directamente
    lista_modificada = lista[:]

    # Eliminar elementos duplicados
    lista_modificada = list(set(lista_modificada))

    # Ordenar la lista de mayor a menor
    lista_modificada.sort(reverse=True)

    # Eliminar todos los números impares
    lista_modificada = [num for num in lista_modificada if num % 2 == 0]

    # Realizar la suma de los números restantes
    suma = sum(lista_modificada)

    # Añadir la suma como primer elemento de la lista
    lista_modificada.insert(0, suma)

    return lista_modificada

if __name__ == '__main__': 
    lista_numeros = [1, 1, 2, 4, 5, 6, 7, 8, 2, 0, 7, 99]
    nueva_lista = modificar(lista_numeros)
    print(nueva_lista[0] == sum(nueva_lista[1:]))
