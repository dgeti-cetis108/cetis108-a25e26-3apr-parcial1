"""
Realiza un programa que pida una palabra y
cuente las vocales que tiene la palabra
"""
# entrada
print("Escribe una palabra")
palabra = input()
vocales = "aeiouAEIOU"
contador = 0

# proceso
for i in range(len(palabra)):
    if palabra[i] in vocales:
        contador += 1

# salida
print("La palabra",palabra,"tiene",contador,"vocales.")