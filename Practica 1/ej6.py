def main():
    cant_naturales = int(input("Ingrese la cantidad de los primeros N números naturales que quiera calcular su "
                               "promedio: "))
    #Gauss
    promedio = (cant_naturales + 1) / 2
    print("El promedio de los primeros", cant_naturales, "números naturales es", promedio)

if __name__ == "__main__":
    main()