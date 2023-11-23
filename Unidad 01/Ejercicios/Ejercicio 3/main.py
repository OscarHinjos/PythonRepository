# **4) A partir del ejercicio anterior, vamos a suponer que cada número es una nota, y lo que queremos es obtener la nota media. El problema es que cada nota tiene un valor porcentual: **

# * La primera nota vale un 15% del total
# * La segunda nota vale un 35% del total
# * La tercera nota vale un 50% del total

# **Desarrolla un programa para calcular perfectamente la nota final.**

numero_1 = 9
numero_2 = 3
numero_3 = 6


media = numero_1 * 0.15 + numero_2 * 0.35 + numero_3 * 0.50
print("La nota media es", media)