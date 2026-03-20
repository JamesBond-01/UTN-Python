import random

#Constantes para la cantidad mínima y máxima de elementos de cada subconjunto.
CANT_VALORES_MIN = 1
CANT_VALORES_MAX= 15
#Constantes para la los valores mínimos y máximos de cada subconjunto.
MIN_NUM = -100
MAX_NUM = 100

def calcula_promedio(conjunto):
    suma_total = 0
    cant = 0
    for i in range(len(conjunto)):
        suma_total += conjunto[i]
        cant += 1
    if cant == 0:
        return 0
    return suma_total/cant

def main():
    conjunto = []

    #Genera los subconjuntos.
    for i in range(20):
        size = random.randint(CANT_VALORES_MIN, CANT_VALORES_MAX)
        subconjunto = [0] * size

        for j in range(size):
            subconjunto[j] = random.randint(MIN_NUM, MAX_NUM)

        conjunto.append(subconjunto)
        print(f"Subconjunto {i}: {subconjunto}")

    #Calcula los promedios de cada subconjunto.
    for i in range(20):
        promedio_subconjunto = calcula_promedio(conjunto[i])
        print(f"Promedio del subconjunto {i}: {promedio_subconjunto}")

if __name__ == "__main__":
    main()