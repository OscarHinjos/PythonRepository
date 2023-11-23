# **3) Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un orden de prioridad 
# (cuanto menor es el número de orden, más prioridad).**

# **¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?**



if __name__ == '__main__': 
    tareas = [ 
        [6, 'Distribución'],
        [2, 'Diseño'],
        [1, 'Concepción'],
        [7, 'Mantenimiento'],
        [4, 'Producción'],
        [3, 'Planificación'],
        [5, 'Pruebas']
    ]

    print("==Tareas desordenadas==")
    for tarea in tareas:
        print(tarea[0], tarea[1])

    tareas.sort() #Ordenamos la lista
    print("==Tareas ordenadas==")
    for tarea in tareas:
        print(tarea[0], tarea[1])
