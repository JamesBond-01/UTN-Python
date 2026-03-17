def main():
    print("Ingrese letra por letra su nombre. Para finalizar, ingrese un '.'")
    letra = ''
    contador = 0
    while letra != '.':
        letra = input(">> ")
        contador += 1
    print("El largo de su nombre es de", contador, "letras.")

if __name__ == "__main__":
    main()
