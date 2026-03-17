def main():
    texto = input("Ingrese el texto que quiera: ").upper() + '*'
    letra = ''

    #Contadores
    i = 0
    letra_a = 0
    letra_e = 0
    letra_i = 0
    letra_o = 0
    letra_u = 0

    while letra != '*':
        letra = texto[i]
        match letra:
            case 'A': letra_a += 1
            case 'E': letra_e += 1
            case 'I': letra_i += 1
            case 'O': letra_o += 1
            case 'U': letra_u += 1
        i += 1

    print("Estos son los resultados de las vocales en el texto ingresado:"
          "\nA:", letra_a,
          "\nE:", letra_e,
          "\nI:", letra_i,
          "\nO:", letra_o,
          "\nU:", letra_u)

if __name__ == "__main__":
    main()