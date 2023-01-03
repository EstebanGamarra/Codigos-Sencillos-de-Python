#ejercicio resuelto 1
for i in range(1,11):
    for j in range(1,11):
        print(i*j, end = "\t")
    print ("")

#ejercicio resuelto 2
"""n = int (input("Introduce un número entero positivo: "))
for i in range (1, n+1, 2):
    print (i, end =", ")
"""
#ejercicio resuelto 3
"""while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        break
    print (frase)
"""
#ejercicio propuesto 1
"""n = 0
positivos = 0
negativos = 0
ceros = 0
print ("Ingrese 10 números:")
while n<10:
    var = int(input()) 
    n += 1
    if var > 0:
        positivos += 1
    elif var == 0:
        ceros += 1
    else:
        negativos += 1
print ("Positivos: ", positivos)
print ("Negativos: ", negativos)
print ("Ceros: ", ceros)"""
#ejercicio propuesto 2
"""
print ("Números pares entre 1 y 25: ")
for i in range (1,26):
    if i % 2 == 0:
         print (i)"""
#ejercicio propuesto 3
"""numero = 10
while numero >= 0:
    numero = int(input("Escriba un número: "))
    if numero >= 0:
        print ("El cuadrado es: ", numero**2)
    else:
        break"""
#ejercicio propuesto 4
""""
print ("Escribir la nota de los alumnos:")
alumno = "Nota del alumno N°{}: "
aprobado = 0
reprobado = 0
for n in range (1,6):
    print (alumno.format(n))
    nota = int(input())
    if nota > 1:
        aprobado += 1
    else:
        reprobado += 1
print ("N° de alumnos aprobados:", aprobado)
print ("N° de alumnos reprobados:", reprobado)"""

