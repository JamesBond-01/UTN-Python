import random

total_facturas = 0
total_cat1 = 0
total_otras = 0

for i in range(50):
    importe = random.randint(1000, 10000)
    categoria = random.randint(1, 3)

    if categoria == 1:
        descuento = importe * 0.15
        total_cat1 += importe
    else:
        descuento = importe * 0.18
        total_otras += importe

    total_facturas += importe

    print(f"Factura {i}: importe={importe}, categoria={categoria}, descuento={descuento}")

print(f"Total facturas: {total_facturas}")
print(f"Total categoría 1: {total_cat1}")
print(f"Total otras categorías: {total_otras}")