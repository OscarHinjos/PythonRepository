# **2) Utilizando operadores lógicos, determina si una cadena de texto introducida por 
# el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiene con mostrar True o False):**

def validacion(texto): 
    return True if len(texto) >=3 and len(texto) < 10 else False

def texto_usuario(): 
    return input("Escribe una cadena de texto")

if __name__ == "__main__": 
    texto = texto_usuario()
    print(validacion(texto))