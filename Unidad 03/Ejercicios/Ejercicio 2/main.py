# **2) Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente.**



if __name__ == '__main__': 
    num = float(input("Escribe un numero impar: "))
    while num % 2 == 0: 
        num = float(input("Escribe un numero impar: "))

    print("Gracias!")
