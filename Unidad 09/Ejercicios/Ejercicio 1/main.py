try:
    from Utils.Utils import *
except ImportError as e: 
    print("Error: No se pudo cargar algunas utilidades")


if __name__ == '__main__':
    lista_vehiculos = []

    vehiculos_introducir = int(input("¿Cuántos vehículos quieres introducir? "))
    for _ in range(vehiculos_introducir):
        registrar_vehiculo(definir_vehiculo(menu()), lista_vehiculos)

    mostrar_ruedas = input("¿Quieres mostrar un número específico de ruedas? (Sí/No): ").lower()
    while mostrar_ruedas not in ('si', 'no'):
        mostrar_ruedas = input("Selecciona una opción válida (Sí/No): ").lower()

    if mostrar_ruedas == 'si':
        ruedas_mostrar = int(input("¿Cuántas ruedas quieres mostrar (2 a 4)? "))
        while ruedas_mostrar not in range(2, 5):
            ruedas_mostrar = int(input("Selecciona un valor válido (2 a 4): "))
        catalogar(lista_vehiculos, ruedas_mostrar)
    else:
        catalogar(lista_vehiculos, 0)  # O simplemente catalogar(lista_vehiculos, 0) si no se muestran ruedas específicas
