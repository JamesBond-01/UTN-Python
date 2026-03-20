import os

HORAS_NORMALES = 140
SUELDO_IMPUESTO = 100000

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def calcular_sueldo(tarifa, horas):
    if horas <= HORAS_NORMALES:
        sueldo = tarifa * horas
    else:
        horas_extra = horas - HORAS_NORMALES
        sueldo = (tarifa * HORAS_NORMALES) + (horas_extra * tarifa * 1.5)
    return sueldo

def calcular_impuesto(sueldo):
    impuesto = 0
    if sueldo > SUELDO_IMPUESTO:
        impuesto = (sueldo - SUELDO_IMPUESTO) * 0.20
    return impuesto

def main():
    tarifa_normales = float(input("Ingrese la tarifa de las horas normales: $"))
    cargar_empleado = 'y'
    while cargar_empleado == 'y':
        id_empleado = input("Ingrese el código de identificación del empleado: ")
        horas_empleado = int(input(f"Ingrese las horas trabajadas por el empleado {id_empleado}: "))

        #Asigna el sueldo e impuesto correspondiente.
        sueldo_empleado = calcular_sueldo(tarifa_normales, horas_empleado)
        impuesto_empleado = calcular_impuesto(sueldo_empleado)
        total_cobrar = sueldo_empleado - impuesto_empleado

        print(f"El empleado {id_empleado} deberá cobrar un total de ${total_cobrar}")
        cargar_empleado = input("Desea cargar otro empleado? [y/n]: ")
        limpiar_pantalla()

if __name__ == "__main__":
    main()
