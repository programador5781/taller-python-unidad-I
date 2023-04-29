""" Ejercicio 11

Programa que permita calcular el valor final a pagar en una súper tienda en donde se aplican los siguientes descuentos:
a) Por compras entre 10000 y 20000 el 10%
b) Por compras entre 20001 y 50000 el 30%
c) Por compras superiores a 50000 el 50%
12.

"""

# Tu código debajo de esta línea

# Pedimos al usuario que ingrese el valor total de la compra
precioPago = float(input("Ingrese el valor de la compra: "))

# Calculamos el descuento correspondiente
if precioPago >= 10000 and precioPago <= 20000:
    descPago = precioPago * 0.1
elif precioPago > 20000 and precioPago <= 50000:
    descPago = precioPago * 0.3
elif precioPago > 50000:
    descPago = precioPago * 0.5
else:
    descPago = 0

# Calculamos el valor final a pagar
precio_final = precioPago - descPago

# Mostramos el resultado al usuario
print("El valor final a pagar por la compra es: $", precio_final)