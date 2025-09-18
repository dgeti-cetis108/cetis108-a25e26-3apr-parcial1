"""
realiza un programa que dado un número fijo del 1 al 10, pregunte
al usuario que adivine cual es dicho número fijo;
si el número ingresado es mayor o menor debes mencionarlo
"""
# entrada
numero_adivinar = 7
print("Adivina el número del 1 al 10")
numero_usuario = int(input())

# proceso / salida
if numero_usuario == numero_adivinar:
    print("Felicitaciones coronaste")
else:
    print("Sigue intentando")
