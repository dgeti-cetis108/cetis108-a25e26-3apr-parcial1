"""
Realiza un programa que genere una contraseña que incluya
letras (minúsculas y mayúsculas) y números, con una
logitud de 8 caracteres, cada caracter lo debes generar
aleatoriamente
"""

import random

minusculas = "abcdefghijklmnñopqrstuvwxyz"
mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numeros = "0123456789"
caracteres_validos = minusculas + mayusculas + numeros
contraseña = ""

print("Generando la contraseña segura 🔐")
print("...")
for i in range(9):
    posicion = random.randint(0, len(caracteres_validos))
    contraseña += caracteres_validos[posicion]

print("La contraseña segura es:", contraseña)