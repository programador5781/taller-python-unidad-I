""" Ejercicio 10

Calcular Si el Numero entero Positivo, que pueda ser Mayor que 100 o Cualquier 
Numero Positivo que sea Múltiplo de 3

"""

# Tu código debajo de esta línea

num = int(input("Digite un número entero positivo: "))

if num > 100:
    print(f"{num} es mayor que 100.")
elif num % 3 == 0:
    print(f"{num} es múltiplo de 3.")
else:
    print(f"{num} es menor que 100 y no es múltiplo de 3.")