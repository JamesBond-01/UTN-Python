def main():
    #Poblacion de los dos paises.
    poblacion_pais_a = 52000000
    poblacion_pais_b = 85000000
    #Porcentajes de crecimiento anual de la población de cada país.
    porcentaje_pais_a = 0.06
    porcentaje_pais_b = 0.04
    #Contador de años transcurridos desde el comienzo del análisis hasta que la población del país A supere la del B.
    contador_anios = 0

    #Cálculo anual del crecimiento poblacional de cada país, hasta que la población del país A supere la del B.
    while poblacion_pais_a <= poblacion_pais_b:
        contador_anios += 1
        poblacion_pais_a = int(poblacion_pais_a + (poblacion_pais_a * porcentaje_pais_a))
        poblacion_pais_b = int(poblacion_pais_b + (poblacion_pais_b * porcentaje_pais_b))
        print("Años transcurridos:", contador_anios, "Poblacion país A:", poblacion_pais_a, "Población país B:", poblacion_pais_b)

    print("El pais A superó al B, en ",contador_anios, "años")

if __name__ == "__main__":
    main()