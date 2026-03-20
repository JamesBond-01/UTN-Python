#Constante que almacena el monto que se tiene en cuenta para los requisitos.
MAXIMA_RECAUDACION = 300000

def main():
    #Arreglo con todas las recaudaciones de cada sucursal.
    sucursal_facturacion = [0] * 10
    #Arreglo con las sucursales que recaudaron al menos $300000.
    sucursales_tope = [0] * 10
    #Variable donde se almacenará el índice de la sucursal con mayor recaudación, entre las que facturaron menos de
    #$300000.
    maximo = -1

    #Carga de datos de las facturaciones de las sucursales.
    print("A continuación, ingrese los montos de recaudación de cada sucursal.")
    for i in range(10):
        sucursal_facturacion[i] = int(input(f"Sucursal {i}: "))

    # Variable auxiliar para recorrer las posiciones del arreglo sucursales_tope
    j = 0

    #Calcula la recaudación máxima entre todas las sucursales que facturaron menos de $300000.
    #Almacena en un nuevo arreglo aquellas sucursales que recaudaron al menos $300000.
    for i in range(10):
        if sucursal_facturacion[i] < MAXIMA_RECAUDACION:
            if maximo == -1 or sucursal_facturacion[i] > sucursal_facturacion[maximo]:
                maximo = i
        else:
            sucursales_tope[j] = i
            j += 1

    #Muestra los resultados de los cálculos.
    if maximo == -1:
        print("No hay sucursales con facturación menor a $300000.")
    else:
        print(f"El monto máximo de todas las sucursales, con monto menor a $300000, es de ${sucursal_facturacion[maximo]}")

    print("Las siguientes sucursales fueron las que recaudaron al menos $300000:")
    for i in range(j):
        print(sucursales_tope[i])

if __name__ == "__main__":
    main()