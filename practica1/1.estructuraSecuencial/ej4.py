# 4. Dados dos números enteros obtener su suma, resta, multiplicación y división.

# Pide numeros a los usuarios.
n1 = int(input("Ingrese el numero 1: "))
n2 = int(input("Ingrese el numero 2: "))

# Realiza los calculos. 
suma = n1 + n2
resta = n1 - n2
producto = n1 * n2
division = n1 / n2

# Muestra los resultados de los calculos.
print("Resultados:")
print("\t",n1, " + ", n2, " = ", suma, "\n",
      "\t",n1, " - ", n2, " = ", resta, "\n",
      "\t",n1, " * ", n2, " = ", producto, "\n",
      "\t",n1, " / ", n2, " = ", division)
