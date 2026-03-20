import random

TAM_SUCESION = 350
MIN_NUM = -50
MAX_NUM = 50

def main():
    sucesion = [0] * TAM_SUCESION

    #Variables auxiliares para calcular promedio.
    suma_positivos = 0
    cant_positivos = 0

    #Suma de los valores negativos de la sucesión.
    suma_negativos = 0

    #Cantidad de valores nulos en la sucesión.
    cant_nulos = 0

    #Genera la sucesión con números aleatorios.
    for i in range(TAM_SUCESION):
        sucesion[i] = random.randint(MIN_NUM, MAX_NUM)

    #Muestra la sucesión y realiza los cálculos correspondientes.
    print(*sucesion)
    for i in range(TAM_SUCESION):
        #Calcula los valores de las cuentas auxiliares para luego obtener el promedio de los valores positivos.
        if sucesion[i] > 0:
            cant_positivos += 1
            suma_positivos += sucesion[i]
        #Calcula la suma de los valores negativos.
        elif sucesion[i] < 0:
            suma_negativos += sucesion[i]
        #Calcula la cantidad de valores nulos.
        else:
            cant_nulos += 1
    #Calcula el promedio de los valores positivos.
    promedio_positivos = suma_positivos / cant_positivos

    #Muestra los resultados obtenidos.
    print(f"Promedio de los números positivos: {promedio_positivos}")
    print(f"Suma de los números negativos: {suma_negativos}")
    print(f"Cantidad de valores nulos: {cant_nulos}")

if __name__ == "__main__":
    main()
