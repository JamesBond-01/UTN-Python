#Como este programa se basa en hacer calculos con numeros de solo 3 dígitos, estas constantes especifican los valores
#maximos que puede tomar la variable para recorrer.
NUM_MIN = 100
NUM_MAX = 999

#Funcion que separa el número en centenas, decenas y unidades, para luego realizarle los cálculos correspondientes.
#Muestra en pantalla los números que cumplen con la condición especificada.
def calcular_numeros():
    i = NUM_MIN
    while i <= NUM_MAX:
        centena_i = i // 100
        decena_i = (i % 100) // 10
        unidad_i = (i % 100) % 10
        if (pow(centena_i, 3) + pow(decena_i, 3) + pow(unidad_i, 3)) == i:
            print(i)
        i += 1


def main():
    print("Bienvenido/a. Este programa mostrará todos los números de tres dígitos, cuya suma al cubo de sus dígitos sea"
          "igual al número:")
    calcular_numeros()

if __name__ == "__main__":
    main()