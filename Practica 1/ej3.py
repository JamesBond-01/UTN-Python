def obtener_factoriales(cant_factoriales):
    print("Lista de factoriales desde 0! hasta ", cant_factoriales, "! :")
    print("0 ! = 1")
    fact = 1
    for i in range(1, cant_factoriales + 1):
        fact *= i
        print(i, "! =", fact)

def main():
    cant_factoriales = int(input("Ingrese la cantidad de factoriales de números que desee calcular: "))
    obtener_factoriales(cant_factoriales)

if __name__ == "__main__":
    main()