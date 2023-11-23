# **1) Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:** 
# * Mostrar una suma de los dos números
# * Mostrar una resta de los dos números (el primero menos el segundo)
# * Mostrar una multiplicación de los dos números
# * En caso de no introducir una opción válida, el programa informará de que no es correcta.



def divi(num1, num2): 
    return num1 / num2 if num2 != 0 else "No se puede divivir entre 0"
def mult(num1, num2): 
    return num1 * num2

def resta(num1, num2): 
    return num1 - num2

def suma(num1, num2): 
    return num1 + num2

def leer_teclado(): 
    num1 = int(input("Escribe un numero: "))
    num2 = int(input("Escribe un numero: "))
    return num1, num2


if __name__ == '__main__': 
    num1 , num2 = leer_teclado()
    print(f"La suma de {num1} + {num2} es: {suma(num1, num2)}")
    print(f"La resta de {num1} - {num2} es {resta(num1, num2)}")
    print(f"La multiplicacion de {num1} x {num2} es: {mult(num1, num2)}")
    if(num2 == 0):
        print(f"{divi(num1, num2)}")
    else:
        print(f"La division de: {num1} / {num2} es: {divi(num1, num2)}")