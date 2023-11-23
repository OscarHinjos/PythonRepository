# **1) Utilizando todo lo que sabes sobre cadenas, listas, sus métodos internos... Transforma este texto:**

# ```
# un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el 
# viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro
# ```

# ```
# Un día que el viento soplaba con fuerza...
# - Mira como se mueve aquella banderola -dijo un monje.
# - Lo que se mueve es el viento -respondió otro monje.
# - Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.
# ```
# **Lo único prohibido es modificar directamente el texto**

if __name__ == '__main__': 
    texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

    
    frases = texto.split('#')

   
    frases = [f.capitalize() for f in frases]

    for i in range(1, len(frases)):
        frases[i] = "- " + frases[i]

    texto_transformado = '\n'.join(frases)

    print(texto_transformado)
