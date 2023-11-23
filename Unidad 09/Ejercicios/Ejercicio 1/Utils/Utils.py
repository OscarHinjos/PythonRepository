try: 
    from Clases.Coche import Coche
    from Clases.Bicicleta import Bicicleta
    from Clases.Camioneta import Camioneta
    from Clases.Motocicleta import Motocicleta
except ImportError as e: 
    print("Error: No se pudo cargar alguna de las clases")




def menu():
    vehiculos = {
        1: "Coche",
        2: "Bicicleta",
        3: "Camioneta",
        4: "Motocicleta"
    }
    print("Qué vehículo quieres registrar:")
    for key, value in vehiculos.items():
        print(f"{key}) {value}")
    while True:
        opcion = int(input("Seleccione: "))
        if opcion in vehiculos:
            return opcion
        else:
            print("Has seleccionado un vehículo que no está en nuestro catálogo. Por favor, inténtalo de nuevo.")

def definir_vehiculo(tipo):
    color = input("Color del vehículo: ")
    ruedas = int(input("Ruedas del vehículo: "))

    if tipo in (1, 4):
        velocidad = float(input("Velocidad del vehículo (Km/h): "))
        cilindrada = int(input("Cilindrada del vehículo: "))
        if tipo == 1:
            return Coche(color, ruedas, velocidad, cilindrada)
        else:
            tipo_bici = input("Tipo de bicicleta (Urbana / Deportiva): ")
            return Motocicleta(color, ruedas, tipo_bici, velocidad, cilindrada)
    elif tipo == 2:
        tipo_bici = input("Tipo de bicicleta (Urbana / Deportiva): ")
        return Bicicleta(color, ruedas, tipo_bici)
    elif tipo == 3:
        velocidad = float(input("Velocidad del vehículo (Km/h): "))
        cilindrada = int(input("Cilindrada del vehículo: "))
        carga = float(input("Carga del vehículo (kg): "))
        return Camioneta(color, ruedas, velocidad, cilindrada, carga)
    else:
        print("No se ha detectado un vehículo, por favor, inténtalo de nuevo.")
        return None

def registrar_vehiculo(vehiculo, lista_vehiculos):
    if vehiculo:
        lista_vehiculos.append(vehiculo)
def mostrar_vehiculo(i, vehiculo):
    if vehiculo.clase_vehiculo == "Coche":
        print(f"""Coche {i}\nColor: {vehiculo.color}\nRuedas: {vehiculo.ruedas}\nVelocidad: {vehiculo.velocidad}\nCilindrada: {vehiculo.cilindrada}""")
    elif vehiculo.clase_vehiculo == "Bicileta":
        print(f"""Bicicleta {i}\nColor: {vehiculo.color}\nRuedas: {vehiculo.ruedas}\nTipo: {vehiculo.tipo}""")
    elif vehiculo.clase_vehiculo == "Camioneta":
        print(f"""Camioneta {i}\nColor: {vehiculo.color}\nRuedas: {vehiculo.ruedas}\nVelocidad: {vehiculo.velocidad}\nCilindrada: {vehiculo.cilindrada}\nCarga: {vehiculo.carga}""")
    elif vehiculo.clase_vehiculo == "Motocicleta":
        print(f"""Motocicleta {i}\nColor: {vehiculo.color}\nRuedas: {vehiculo.ruedas}\nTipo: {vehiculo.tipo}\nVelocidad: {vehiculo.velocidad}\nCilindrada: {vehiculo.cilindrada}""")

def catalogar(lista_vehiculos, mostrar_ruedas):
    if mostrar_ruedas > 0:
        contador_ruedas = sum(1 for vehiculo in lista_vehiculos if vehiculo.ruedas == mostrar_ruedas)
        print(f"Se han encontrado {contador_ruedas} vehículos con {mostrar_ruedas} ruedas")
        for i, vehiculo in enumerate(lista_vehiculos):
            if vehiculo.ruedas == mostrar_ruedas:
                mostrar_vehiculo(i, vehiculo)
    else:
        for i, vehiculo in enumerate(lista_vehiculos):
            mostrar_vehiculo(i, vehiculo)
