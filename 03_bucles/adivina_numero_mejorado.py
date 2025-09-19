"""
realiza un programa que permita al usuario intentar adivinar
un número del 1 al 100 que previamente fue generado pseudoaleatoriamente
primera parte: con intentos ilimitados hasta que adivine o desista
segunda parte: con intentos limitados (controlados de manera fija)
"""
import random

# entrada
numero_adivinar = random.randint(1,100)
print(numero_adivinar)
adivino = False
print("JUEGO ADIVINA NÚMERO")
print("Adivina un número del 1 al 100")
numero_ingresado = int(input())

# proceso
while not adivino:
    if numero_ingresado == 0:
        break
    elif numero_ingresado == numero_adivinar:
        adivino = True
    else:
        print("Casi lo consigues, ingresa otro número")
        numero_ingresado = int(input())

# salida
if adivino:
    print("Felicidades, lo lograste!")
else:
    print("Lástima que terminó, el festival de hoy!")