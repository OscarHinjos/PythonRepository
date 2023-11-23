# **3) Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente**:

# * Si el primer número es mayor que el segundo, debe devolver 1.
# * Si el primer número es menor que el segundo, debe devolver -1.
# * Si ambos números son iguales, debe devolver un 0.



def relacion(num1, num2): 
    if num1 > num2 : return 1
    elif num1 < num2 : return -1
    else : return 0

if __name__ == '__main__': 
    print(relacion(1, 2))