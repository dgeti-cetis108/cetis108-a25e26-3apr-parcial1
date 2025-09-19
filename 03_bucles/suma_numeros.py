"""
Realiza un programa que pida un número N
y calcula la suma de todos los números
de 1 hasta N
"""
# entrada
print("Ingresa un número entero")
numero = int(input())
resultado = 0

# proceso
for i in range(1, numero + 1):
    resultado += i

# salida
print("El resultado es:", resultado)
