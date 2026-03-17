import os

#Cantidad de parciales por alumno.
CANT_PARCIALES = 5

#Funcion para limpiar pantalla.
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

#Funcion para cargar, por cada alumno, las notas de los 5 parciales. También verifica la validez del valor ingresado.
#Recibe un array vacío de las notas de cada uno y la cantidad alumnos cargados.
#Devuelve el array de las notas con valores cargados.
def carga_notas(listado_notas, cant_alumnos):
    for i in range(cant_alumnos):
        limpiar_pantalla()
        print("Alumno", i + 1)

        for j in range(CANT_PARCIALES):
            nota = int(input(f"Nota del parcial {j+1}: "))

            while nota < 0 or nota > 10:
                nota = int(input("Ingrese un valor entre 0 y 10: "))

            listado_notas[i][j] = nota

    return listado_notas

#Funcion en la cual, a cada alumno le calcula su condición final de la materia.
#Recibe el arreglo de notas con valores previamente cargados y la cantidad de alumnos.
#Devuelve un nuevo arreglo con las condiciones de cada alumno, de modo que cada posición de este arreglo coincide
#con el número de legajo del alumno.
def calcular_condiciones(listado_notas, cant_alumnos):
    condiciones = [""] * cant_alumnos

    for i in range(cant_alumnos):
        #Contador para definir su condición, basada en el valor final del mismo.
        examenes_aprobados = 0
        #Cuenta los exámenes del alumno con nota mayor a 5 puntos.
        for j in range(CANT_PARCIALES):
            if listado_notas[i][j] >= 5:
                examenes_aprobados += 1

        #Evalúa su condición basada en cuántos exámenes tuvo nota más que 5.
        if examenes_aprobados >= 4:
            condiciones[i] = "Regular"
        elif examenes_aprobados == 3:
            condiciones[i] = "Recuperatorio"
        else:
            condiciones[i] = "Recursar"

    return condiciones

#Función que demuestra, por cada alumno, su condición final.
def mostrar_condiciones(condiciones):
    for i in range(len(condiciones)):
        print("Alumno", i + 1, ":", condiciones[i])

def main():
    cant_alumnos = int(input("Ingrese cantidad de alumnos: "))

    #Array donde se ingresaran las notas de cada alumno.
    listado_notas = [[0]*CANT_PARCIALES for _ in range(cant_alumnos)]

    carga_notas(listado_notas, cant_alumnos)

    condiciones = calcular_condiciones(listado_notas, cant_alumnos)

    mostrar_condiciones(condiciones)

if __name__ == "__main__":
    main()