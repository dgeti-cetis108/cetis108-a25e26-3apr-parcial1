"""
Realiza un programa que imprima todas las tablas
"""

print("TABLAS DE MULTIPLICAR")

for a in range(1, 11):
    print("Tabla del", a)
    print("-----------------------")
    for b in range(1, 11):
        print(a, "x", b, "=", a * b)
    print("")
