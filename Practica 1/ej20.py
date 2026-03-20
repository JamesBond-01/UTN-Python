def main():
    opcion = input("¿Desea ingresar un subconjunto? (C/F): ").upper()

    while opcion == 'C':
        suma = 0

        print("\nIngrese los 30 valores del subconjunto:")

        for i in range(30):
            num = int(input(f"Valor {i+1}: "))
            suma += num

        promedio = suma / 30
        print(f"Promedio del subconjunto: {promedio}")

        opcion = input("\n¿Desea ingresar otro subconjunto? (C/F): ").upper()

if __name__ == "__main__":
    main()