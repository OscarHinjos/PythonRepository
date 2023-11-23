# **3) Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:**
# * Guarda en una variable numero_magico el valor 12345679 (sin el 8)
# * Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9 (asegúrate que es un número)
# * Multiplica el numero_usuario por 9 en sí mismo
# * Multiplica el numero_magico por el numero_usuario en sí mismo
# * Finalmente muestra el valor final del numero_magico por pantalla



NUM_MAGICO = 12345679

def leer_numero():
    while True:
        numero_usuario = int(input("Escribe un numero ENTRE 1 y 9: "))
        if 1 <= numero_usuario <= 9:
            return numero_usuario
        else:
            print("Por favor, ingresa un número entre 1 y 9.")

if __name__ == '__main__':
    numero_usuario = leer_numero()

    num_usuario_nueve = numero_usuario * 9
    NUM_MAGICO *= numero_usuario  # Multiplicar el NUM_MAGICO por numero_usuario en sí mismo
    print(NUM_MAGICO)
