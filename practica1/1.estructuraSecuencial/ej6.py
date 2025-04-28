# 6. Dadas las medidas de dos ángulos de un triángulo determinar la medida del tercero e informar el resultado.

# Pide las medidas del primer angulo.
angulo1 = float(input("Ingrese la medida del primer angulo (°): "))

# Verifica que el primer angulo sea un valor valido.
if(angulo1 > 0 and angulo1 < 180):
    # Si el primer angulo es válido, pide la medida del segundo angulo.
    angulo2 = float(input("Ingrese la medida del segundo angulo(°): "))
    
    # Verifica que el segundo angulo sea valido y ademas, que los dos valores sean posibles para que exista
    # un triangulo.
    if((angulo2 > 0 and angulo2 < 180) and (angulo1 + angulo2 < 180)):

        # Calcula la medida del tercer angulo.
        # Teniendo en cuenta que la suma de los angulos internos de un triangulo es igual a 180, entonces, el tercer angulo se
        # calcula como una resta entre 180 y la suma de los dos angulos restantes.
        angulo3 = 180 - (angulo1 + angulo2)

        # Muestra el resultado
        print("El tercer angulo mide",angulo3,"°")
    else:
        print("Error en el angulo 2: medida no válida, o la suma de ambos angulos hace que sea imposible crear un triangulo.")
else:
    print("Error en el angulo 1: medida no válida.")
