#primer ejercicio (resuelto)
n = int(input("Introduce un número entero: "))
if n % 2 == 0:
    print ("El número: " + str(n) + " es par")
else:
    print ("El número: " + str(n) + " es impar")
#primer ejercicio propuesto
"""na = int(input("Introduzca su primer número: "))
nb = int(input("Introduzca su segundo número: "))
if na > nb: 
    print ("El primer número es mayor")
elif na == nb:
    print ("Los números son iguales")
else: 
    print ("El segundo número es mayor")"""
#segundo ejercicio propuesto
"""x = int(input("Introduzca su edad: "))
if x >= 18:
    print("Usted es mayor de edad")
elif x<0:
    print ("Valor inválido")
else:
    print ("Usted no es mayor de edad")"""
#tercer ejercicio propuesto
"""contraseña = input("Introduzca su contraseña: ")
check = input("Vuelva a introducir su contraseña: ")
if contraseña.upper() == check.upper():
    print ("Contraseña correcta")
else:
    print ("Contraseña incorrecta")"""
#cuarto ejercicio propuesto
"""
edad = int(input("Ingerese la edad del cliente:"))
print ("Los costos son según la edad:\n►Menos de 4 años: No paga")
print ("►4 a 18 años: 10.000 Gs\n►Mayores de 18 años: 15.000 Gs")
if edad<4:
    print ("El cliente no debe pagar")
elif edad>4 and edad<=18:
    print ("El cliente debe pagar: 10.000 Gs.")
elif edad>18:
    print ("El cliente debe pagar 15.000 Gs.")
else:
    print ("Valor de edad no válido")
"""