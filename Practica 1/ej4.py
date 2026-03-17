def contar_silabas(texto, silaba_usuario):
    cant_silabas = 0
    #Compara silaba por silaba, deslizándose de a un lugar.
    for i in range(1, len(texto)):
        #Concatena dos caracteres de posiciones consecutivas.
        silaba_texto = texto[i - 1] + texto[i]
        #Compara estas dos posiciones del texto con la escrita por el usuario. Suma 1 al contador si coinciden.
        if silaba_texto == silaba_usuario:
            cant_silabas += 1
    print("Cantidad de veces que aparece la silaba '", silaba_usuario, "' :", cant_silabas)

def main():
   texto = input("Ingrese el texto que usted quiera: ") + '.'
   silaba = input("A continuación, ingrese una sílaba cualquiera de SOLO DOS CARACTERES y se le informará cuántas "
                  "veces aparece en el texto ingresado: ")
   while len(silaba) != 2:
       silaba = input("Por favor, ingrese una silaba de sólo DOS caracteres: ")

   contar_silabas(texto.lower(), silaba.lower())

if __name__ == "__main__":
    main()