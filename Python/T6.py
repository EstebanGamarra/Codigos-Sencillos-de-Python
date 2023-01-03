#EJERCICIO 1
"""contraseña = input('Introduce la contraseña:')
#Error: [ corchetes por ( paréntesis
  if contraseña in ('sesamo'): 
    print('Pasa')
#Error: faltan dos puntos :
else: 
    print('No pasa') """
#EJERCICIO 2
"""base = int(input('Introduce la base imponible  de la factura:'))
#Error: iva no está definido, por lo que no podemos pasar como parámetro a nuestra subrutina 
iva=10
#Error: la definición de subrutina tiene que definirse antes de su llamado, no despúes
def aplica_iva(base, iva):
    base = base*iva
    return base
print (aplica_iva(base,iva))"""
#EJERCICIO 3
age = int(input("¿Cuál es tu edad?"))
"""Error: no tiene sentido preguntar si solo tiene 18 años, debemos incluir un rango.
además, si pusiesemos una edad menor a 18 el programa imprimiría "mayor de edad" lo cual
es incorrecto.
Error: si se quizo hacer la comparación en primer lugar con 18 años, se tuvo que utilizar
el operando == de comparación, no el operando = de asignación a una variable. Además
falta un typecast a variable tipo int para poder realizar la operación lógica """
if age < 18:
    print ("Eres menor de edad.")
else:
    print("Eres mayor de edad.")
#EJERCICIO 4
"""while True:
#Error: falta esperar el input del usuario
    frase = input("Introduce algo:")
    if frase == "salir":
        break
    print (frase)"""
#Error: <> se debe cambiar por ==, es decir, si se introduce salir, el programa termina
"""Error: otra forma de escribir esto sería cambiar <> por != que es 
el operando *distinto a*, poner en dicho if el print
y hacer un else donde vaya el break"""