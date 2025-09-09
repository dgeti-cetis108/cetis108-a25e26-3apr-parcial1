# Escribe un programa que declare al menos cinco
# variables con nombres válidos y significativos,
# y asigna diferentes tipos de datos a cada una
# (entero, cadena, lista, etc.).

# string nombre; C#
# en python las variables toman tipo de dato de 
# forma dinamica, una vez que le asignas un valor
nombre = "Hector" # string
edad = 16         # int
estatura = 1.75   # float (número decimal)
esta_inscrito = True # booleano

# imprime el tipo de dato de cada variable antes declarada
print("la variable nombre es de tipo", type(nombre))
print("la variable edad es de tipo", type(edad))
print("la variable estatura es de tipo", type(estatura))
print("la variable esta_inscrito es de tipo", type(esta_inscrito))


# Intenta declarar variables con nombres no válidos 
# (por ejemplo, que comiencen con números o contengan
# caracteres especiales) y observa los errores que genera Python.
# 1cancion = "para ti para mi" # error: no debe iniciar con número
# canci*nes = 26 # error: no lleva caracteres especiales
# mi nombre = "bidkar" # error: no lleva espacios
# True = 1234 # error: no utilizar palabras reservadas