def main():
    print("Este programa contará la cantidad de veces que una palabra, del texto que usted ingrese, termina con"
          "la letra que elija.")
    texto = input("Ingrese un texto: ") + ' \0'
    letra = input("Ingrese la letra: ")

    #Contador para los índices del texto.
    i = 0
    #Contador de palabras que tienen esa letra al final.
    cant_palabras_letra = 0

    #Bucle para leer el texto entero.
    while texto[i] != '\0':
        #Si la posición siguiente es un espacio o algún separador, significa que es el final de una palabra.
        if texto[i] == letra and texto[i+1] in " ,.;:!?":
            cant_palabras_letra += 1
        i += 1

    print("Las palabras que terminan con la letra '", letra, "' son:", cant_palabras_letra)

if __name__ == "__main__":
    main()