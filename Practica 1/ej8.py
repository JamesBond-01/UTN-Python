#Divide recursivamente el exponente en 2, aplicando que:
#Si el exponente es par: 2^n = (2^(n/2))^2
#Si el exponente es impar: 2^n = 2 x (2^(n-1))
def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente % 2 == 0:
        mitad = potencia(base, exponente // 2)
        return mitad * mitad
    else:
        return base * potencia(base, exponente - 1)

def main():
    #Es una serie geométrica, porque se suman las cantidades de cada casillero.
    total = potencia(2, 64) - 1
    print("El inventor del ajedrez debería haber cobrado", total, "granos.")

if __name__ == "__main__":
    main()