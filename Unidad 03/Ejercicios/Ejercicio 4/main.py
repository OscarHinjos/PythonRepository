# **4) Realiza un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética:**

def leer_numero(num_introducir): 
    list = []
    for num in range(num_introducir): 
        num = float(input("Escribe tu nota: "))
        list.append(num)

    return list

if __name__ == "__main__": 
    num_introducir = int(input("¿Cuantos notas quieres introducir? "))
    list_notas = leer_numero(num_introducir)
    media = sum(list_notas)/ num_introducir
    # Leer notas
    for i,n in enumerate(list_notas): 
        print(f"Nota {i+1}: {n}", end=" ")

    print(f"\nLa media de tus notas es: {media}")