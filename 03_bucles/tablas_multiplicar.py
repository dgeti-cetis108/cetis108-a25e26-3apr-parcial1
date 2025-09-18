"""
Realiza un programa que pida un número del 1 al 10
e imprime la tabla de multiplicación de dicho número
las instrucciones para bucles ó ciclos en python
pueden ser for o while, cuando conozcan el total 
de iteraciones de un ciclo utiliza for de lo
contrario utiliza while, cuando depende de una
condición que debe cumplirse para culminar el ciclo
"""
# entrada
print("Ingresa un número del 1 al 10")
numero = int(input())

# proceso/salida
print("Tabla del", numero)
for i in range(1,11):
    print(numero,"x",i,"=",numero*i) # 5x1=5
