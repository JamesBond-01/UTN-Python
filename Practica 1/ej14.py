def encontrar_coma(cadena):
    for i in range(len(cadena)):
        if cadena[i] == ',':
            return i
    return -1

def main():
    cadena = input("Ingrese un texto cualquiera: ")
    pos_coma = encontrar_coma(cadena)
    if pos_coma == -1:
        print("No se ha encontrado ninguna coma a lo largo de la cadena.")
    else:
        print(f"Se ha encontrado la primer coma en la posición {pos_coma} del texto.")

if __name__ == "__main__":
    main()