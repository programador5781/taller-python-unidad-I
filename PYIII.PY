""" Ejercicio 3 

Digitar un Numero Entero Positivo y dividirlo en 5 dígitos,
EL Primer y Último Digito Se eleva al Cuadrado. """

# Tu código debajo de esta línea

numIngresado = input("Ingrese un número entero positivo: ")
while not numIngresado.isdigit():
    numIngresado = input("El número ingresado no corresponde a un entero positivo, por favor ingrese un nuevo número: ")

numIngresado = int(numIngresado)

if numIngresado< 0:
    print("El número ingresado no es positivo.")
else:
    dig = []
    while numIngresado > 0:
        dig.append(numIngresado % 10)
        numIngresado //= 10

    while len(dig) < 5:
        dig.append(0)

    digitoP = dig[-1]
    digitoU = dig[0]

    digitoPcuadrado = digitoP ** 2
    digitoUcuadrado = digitoU ** 2

    print(f"El primer dígito es {digitoP} y su cuadrado es {digitoPcuadrado}.")
    print(f"El último dígito es {digitoU} y su cuadrado es {digitoUcuadrado}.")

