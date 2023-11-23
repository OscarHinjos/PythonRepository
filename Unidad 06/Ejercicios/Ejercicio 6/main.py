# **6) Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. 
# La primera con los números pares, y la segunda con los números impares:**



def separar(lista_numeros):
    lista_pares = []
    lista_impares = []

    for n in lista_numeros: 
        if n % 2 == 0: lista_pares.append(n)
        else: lista_impares.append(n)
    
    return lista_pares, lista_impares

if __name__ == '__main__': 
    list_pares, lista_impares = separar([1,2,3,4,5,6,7,8,9,10])
    print(list_pares)
    print(lista_impares)