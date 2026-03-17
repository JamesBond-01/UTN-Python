def main():
    #Variable dónde se almacenará la sucesión de números, ingresada manualmente por el usuario.
    sucesion = ""
    #Variable dónde el usuario ingresa un término de la sucesión.
    numero = '0'

    print("Ingrese los números que quiera. Presione enter sin ingresar un valor para terminar.")
    #Carga de datos la sucesión. No se sabe cuantos términos tiene, as que el usuario carga la cantidad que quiera.
    while numero != '':
        numero = input(">> ")
        #Dependiendo si es el comienzo/final de la sucesión o no, se le agrega una coma entre términos.
        if sucesion == "" or numero == '':
            sucesion = sucesion + numero
        else:
            sucesion = sucesion + ',' + numero

    print("Sucesión ingresada:", sucesion)

    #Variable para tomar de a términos individuales de la sucesión.
    termino = ""
    i = 0
    while sucesion[i] != '':
        #Toma de a términos, teniendo en cuenta la separación por coma de la sucesión.
        while sucesion[i] != ',':
            termino = termino + sucesion[i]
            i += 1

    print(termino)

if __name__ == "__main__":
    main()