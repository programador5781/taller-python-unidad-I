""" Ejercicio 2 
 Desarrolle el algoritmo de la empresa XYZ, que permita calcular la nómina semanal de 5 obreros, con la siguiente características:
• Valor Hora 1000 pesos.
• Digitar el Número de Horas Trabajadas por semana por cada Obrero
• Calcular el valor a pagar por cada obrero
• Calcular el Valor Total Pagados a Todos los Obreros. """

# Tu código debajo de esta línea

valor_hora = 1000  # valor por hora
num_obreros = 5  # número de obreros

total_pagar = 0  # acumulador para el valor total a pagar a todos los obreros

for i in range(num_obreros):
    horas_trabajadas = int(input(f"Ingrese las horas trabajadas por el obrero {i+1}: "))
    valor_pagar = horas_trabajadas * valor_hora
    total_pagar += valor_pagar
    print(f"El obrero {i+1} debe recibir {valor_pagar} pesos por su trabajo.")

print(f"El valor total a pagar a los {num_obreros} obreros es de {total_pagar} pesos.")
