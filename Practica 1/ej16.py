def main():
    #Variables que almacenan la cantidad total vendida de cada artículo.
    cant_total_a = 0
    cant_total_b = 0

    #Variables que contienen el precio unitario de ambos artículos.
    precio_a = float(input("Ingrese precio unitario del artículo A: "))
    precio_b = float(input("Ingrese precio unitario del artículo B: "))

    #Variables que acumulan el monto total recaudado de las ventas de cada artículo, con descuento incluído donde
    #corresponda.
    importe_total_a = 0
    importe_total_b = 0

    #Variable para que el usuario decida cargar otra venta o cancelar la operación.
    cargar_venta = 'y'

    #Carga de ventas.
    print("Ingrese los siguientes datos de la venta:")
    while cargar_venta == 'y':
        cod_art = input("Ingrese código del artículo (A o B): ").upper()
        #Verificación del ingreso del código del artículo.
        while cod_art != 'A' and cod_art != 'B':
            cod_art = input("Error. Ingrese un valor correcto (A o B): ").upper()
        cant_art = int(input("Ingrese la cantidad vendida: "))

        #Evaluación de la cantidad vendida y recaudada por cada artículo.
        if cod_art == 'A':
            importe_venta = cant_art * precio_a
            if cant_art > 10:
                importe_venta = importe_venta - (importe_venta * 0.20)
            cant_total_a += cant_art
            importe_total_a += importe_venta
        else:
            importe_venta = cant_art * precio_b
            if cant_art > 10:
                importe_venta = importe_venta - (importe_venta * 0.20)
            cant_total_b += cant_art
            importe_total_b += importe_venta

        cargar_venta = input("Desea ingresar otra venta? [y/n]: ").lower()

    #Muestra de los resultados.
    print(f"La cantidad total vendida del articulo A es: {cant_total_a}. El importe total de todas las ventas, es de "
          f"${importe_total_a}")
    print(f"La cantidad total vendida del articulo B es: {cant_total_b}. El importe total de todas las ventas, es de "
          f"${importe_total_b}")


if __name__ == "__main__":
    main()