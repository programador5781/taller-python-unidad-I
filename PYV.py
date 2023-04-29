"""Ejercicio 5 

La presión, el volumen y la temperatura de una masa de aire se relacionan por 
la formula: masa = (presión * volumen)/(0.37 * (temperatura + 460))
"""

# Tu código debajo de esta línea

presion = float(input("Ingrese la presión en kilopascales: "))
volumen = float(input("Ingrese el volumen en metros cúbicos: "))
temperatura = float(input("Ingrese la temperatura en grados Celsius: "))

temperatura_kelvin = temperatura + 273.15  # Convertir a Kelvin
masa = (presion * volumen) / (0.37 * (temperatura_kelvin + 460))

print(f"La masa de aire es {masa:.2f} kg.")