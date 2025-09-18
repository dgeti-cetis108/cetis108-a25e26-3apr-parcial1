"""
realiza un programa que determine si un número
ingresado es par o impar
"""
# entrada
print("Ingresa un número entero")
numero = int(input())
# proceso; operador para calcular residuo %
resultado = numero % 2
# salida
if resultado == 0:
    print("El número",numero,"es par")
else:
    print("El número",numero,"es impar")
