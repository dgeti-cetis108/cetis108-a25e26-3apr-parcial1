"""
realiza un programa que pida tres números enteros
y muestre el número mayor.
PC = entrada -> proceso -> salida
"""
# Entrada
print("Escribe un número del 1 al 10")
numero1 = int(input())
print("Escribe otro número del 1 al 10")
numero2 = int(input())
print("Escribe otro número del 1 al 10")
numero3 = int(input())
numero_mayor = 0

# Proceso  3 1 6, 1 3 6, 6 2 1, 1 6 3, 6 1 6
if numero1 > numero2:
    if numero1 > numero3:
        numero_mayor = numero1
    else:
        numero_mayor = numero3
elif numero2 > numero3:
    numero_mayor = numero2
else:
    numero_mayor = numero3

# Salida
print("El número mayor ingresado es:", numero_mayor)
