# **6) Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:**
# * Todos los números del 0 al 10 [0, 1, 2, ..., 10]
# * Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
# * Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
# * Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
# * Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

# *Pista: Utiliza el tercer parámetro de la función range(inicio, fin, salto).*


if __name__ == '__main__': 
    lista1 = list(range(0,11))
    lista2 = list(range(-10,1))
    lista3 = list(range(0,21,2))
    lista4 = list(range(-21,-1,2))
    lista5 = list(range(0,51,5))
