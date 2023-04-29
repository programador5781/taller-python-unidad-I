""" Ejercicio 12

Programa para determinar si un deportista es aceptado en el equipo de baloncesto de Bogotá. 
Las condiciones para ser aceptado son: 
a) La edad debe ser menor o igual a 18 años 
b) La estatura debe ser mayor a 180 cm 
c) El peso debe ser menor o igual a 80 kg Si el aspirante cumple las 3 condiciones

"""

# Tu código debajo de esta línea


# Pedimos al usuario que ingrese la edad, estatura y peso del aspirante
edadCandidato = int(input("Ingrese edad del candidato: "))
estaturaCandidato = float(input("Ingrese estatura del candidato  (en cm): "))
pesoCandidato = float(input("Ingrese peso del candidato (en kg): "))

# Verificamos si el aspirante cumple las condiciones
if edadCandidato <= 18 and estaturaCandidato > 180 and pesoCandidato <= 80:
    print("El candidato fue seleccionado para el equipo de baloncesto de Bogotá.")
else:
    print("El candidato no fue aceptado en el equipo de baloncesto de Bogotá, ya que no cumple con los requisitos necesarios.")
