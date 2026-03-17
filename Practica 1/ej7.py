def main():
    numero_m = int(input("Ingrese el primer número natural: "))
    numero_n = int(input("Ingrese el segundo número natural: "))

    #Valida que los dos números ingresados sean naturales.
    while numero_m < 1 or numero_n < 1:
        if numero_m < 1:
            numero_m = int(input("Por favor, ingrese un número que sea natural: "))
        else:
            numero_n = int(input("Por favor, ingrese un número que sea natural: "))

    #Pensado con la misma idea que el algoritmo de Gauss. Se suman el primer término con el último,
    #se multiplica por la cantidad total de números (numero_n en este caso) y se divide por 2, porque estaría duplicando
    #la suma.
    suma = numero_n * ((numero_m + 1) + (numero_m + numero_n)) // 2
    print("El resultado de la suma de los", numero_n, "números posteriores a", numero_m, "es", suma)

if __name__ == "__main__":
    main()