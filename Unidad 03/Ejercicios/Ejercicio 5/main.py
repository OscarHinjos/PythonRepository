# **5) Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso.
# Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:**


def verificar_lista(num, list_numeros): 
    if num in list_numeros: 
        return "El numero se encuentra en la lista"
    return "El numero no se encuentra en la lista"

def pedir_numero(): 
    num = int(input("Escribe un número. ENTRE 1 y 9 : "))
    while num < 0 or num > 9: 
        num = int(input("Escribe un número. ENTRE 1 y 9 : "))
    return num

if __name__ == '__main__': 
    numeros = [1, 3, 6, 9]
    num_usu = pedir_numero()
    print(verificar_lista(num_usu, numeros))
    