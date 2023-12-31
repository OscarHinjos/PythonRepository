# **6) Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. 
# ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?:**

# * ***Nombre*** ***Apellido*** ha sacado un ***Nota*** de nota.

# *Ayuda: Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: **cadena[::-1]** *

if __name__ == '__main__':
    cadena = "zeréP nauJ,01"
    cadena_vuelta = cadena[::-1]
    print(f"{cadena_vuelta[3:7]} {cadena_vuelta[8:]} ha sacado un {cadena_vuelta[0:2]} de nota")