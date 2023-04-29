""" Ejercicio 9

Programa el cual permita ingresar los valores de temperatura del promedio de 3 días de la semana. Le programa debe calcular la temperatura promedio y luego mostrar los siguientes mensajes:
a) Si el promedio es mayor a 35° mostrar el mensaje “que días tan calurosa”
b) Si el promedio esta entre 15° y 35° mostrar el mensaje “Que clima tan delicioso”
c) Si el promedio es menor de 15° mostrar el mensaje “Que días tan fría”

"""

# Tu código debajo de esta línea

temp1 = float(input("Ingrese la temperatura promedio del primer día: "))
temp2 = float(input("Ingrese la temperatura promedio del segundo día: "))
temp3 = float(input("Ingrese la temperatura promedio del tercer día: "))

prom_temp = (temp1 + temp2 + temp3) / 3

if prom_temp > 35:
    print("Qué días tan calurosos.")
elif prom_temp >= 15:
    print("Qué clima tan delicioso.")
else:
    print("Qué días tan fríos.")