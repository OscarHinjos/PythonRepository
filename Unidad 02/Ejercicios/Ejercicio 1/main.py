# **1) Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):**
# * Si los dos números son iguales
# * Si los dos números son diferentes
# * Si el primero es mayor que el segundo
# * Si el segundo es mayor o igual que el primero


def mayor_menor(num1, num2): 
    if num1 > num2: 
        return True
    else: 
        return False

def diff_igual(num1, num2):
    return num1 == num2

def leer_teclado(): 
    num1 = int(input("Escribe un número: "))
    num2 = int(input("Escribe otro número: "))
    return num1, num2

if __name__ == '__main__': 
    num1, num2 = leer_teclado()
    print("¿Los dos números son iguales?", diff_igual(num1, num2))
    print("¿Los dos números son diferentes?", not diff_igual(num1, num2))
    print("¿El primero es mayor que el segundo?", mayor_menor(num1, num2))
    print("¿El segundo es mayor o igual que el primero?", not mayor_menor(num1, num2))
