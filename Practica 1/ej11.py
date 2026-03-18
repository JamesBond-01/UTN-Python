def main():
    print("Ingrese los números de la sucesión. Presione Enter sin ingresar un valor para terminar:")

    #Lee los dos primeros números.
    primero = input(">> ")
    if primero == "":
        return
    primero = int(primero)

    segundo = input(">> ")
    if segundo == "":
        return
    segundo = int(segundo)

    #Lee el resto de la sucesión hasta que ingresa un enter.
    siguiente = input(">> ")
    while siguiente != "":
        siguiente = int(siguiente)

        #Verifica si el valor del medio es un máximo relativo.
        if segundo > primero and segundo > siguiente:
            print("Máximo relativo:", segundo)

        #Desplaza los valores, tomando la posición siguiente respectiva a cada número.
        primero = segundo
        segundo = siguiente

        siguiente = input(">> ")

if __name__ == "__main__":
    main()