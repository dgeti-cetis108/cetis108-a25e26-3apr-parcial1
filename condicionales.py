"""
Escribe un algoritmo que pregunte al usuario su edad y,
dependiendo de la edad le muestre alguno de los mensajes
siguientes:
1-11: eres un(a) niño(a)
12-17: eres un(a) adolescente
18-25: eres un(a) joven
26-59: eres un(a) adulto
60-75: eres un(a) adulto mayor
>75: felicitaciones has tenido una larga vida

utiliza la condicional if para resolver este algoritmo.
descomponer el problema: pregunta solo la edad
abstracción: desechas el nombre, apellidos, estatura, etc.
patrones: reutiliza el código que ya tengas
algoritmo: escribe en lenguaje natural el algoritmo
programación: convierte a python el algoritmo
    entrada -> proceso -> salida
"""
# declarar variable para almacenar la edad
edad = 0

# pedir al usuario su edad
print("¿Cuántos años tienes?")
edad = int(input()) # casting: trata un valor como otro tipo

# evaluar la edad y emitir el mensaje adecuado
if edad<1:
    print("número incorrecto, debe ser mayor o igual a 1")
elif edad<=11:
    # mostrar mensaje
    print("eres un(a) niño(a)")
elif edad<=17:
    print("eres un(a) adolescente")
elif edad<=25:
    print("eres un(a) joven")
elif edad<=59:
    print("eres un(a) adulto")
elif edad<=75:
    print("eres un(a) adulto mayor")
else:
    print("felicitaciones has tenido una larga vida")
