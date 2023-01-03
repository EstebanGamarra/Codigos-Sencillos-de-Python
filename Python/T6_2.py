#EJERCICIO 1
def año_bisiesto(valor):
    if ((valor%4==0) and((valor%100 == 0) or valor%400!=0)):
        band=1
    else:
        band=0
    return band
def bandera_check(bandera):
    if (bandera==1):
        print("Es un año bisiesto")
    elif(bandera==0):
        print("No es un año bisiesto")
año=int(input("Ingrese un año para saber si es bisiesto o no:"))
flag = año_bisiesto(año)
bandera_check(flag)
#EJERCICIO 2
"""divis = []
def divisores(nro):
    if nro > 0:
        for i in range (1,nro+1):
            if (nro%i==0):
                divis.append(i)
        print ("Los divisores del número son: ", divis)
    else:
        divis.append(0)
        print ("El número no tiene divisores")
print ("Ingrese un valor entero mayor a cero para encontrar sus divisores:")
nro = int(input())
divisores(nro)"""
#EJERCICIO 3
"""def factorial(numero):
    factor = 1
    error = "No existe el factorial del número"
    if numero < 0:
        return error
    elif numero > 0:
        for i in range (1,numero+1):
            factor = i*factor
        return factor
    else:
        return factor
numer = int(input("Escriba el número del cual quiere hallar el factorial: "))
print ("Su factorial es: ", factorial(numer))"""
#EJERCICIO 4
"""error1=0
error2=0
horas = int(input("Escriba las horas trabajadas:"))
horario = (input("Escriba horario nocturno o diurno N o D, por teclado:"))
horario = horario.upper()
dias = input("Escriba los dias que trabaja, entre comas:")
dias = dias.lower()
ldias = dias.split(",")
norm = 0
dom = 0
if (horas <= 0):
    error1=1
if (horario == 'N' or horario == 'D'):
    error2=0
else:
    error2=1
while (error1==1):
    horas = int(input("Escriba las horas trabajadas:"))
while (error2==1):
    horario = int(input("Escriba horario nocturno o diurno N o D, por teclado:"))
for i in range (0,len(ldias)):
    if (ldias[i]=="lunes" or ldias[i]=="martes" or ldias[i]=="miercoles" or ldias[i]=="jueves" or ldias[i]=="viernes" or ldias[i]=="miércoles"):
        norm = norm + 1
    elif (ldias[i] == "domingo"):
        dom = dom + 1
if (horario == 'N'):
    total = int(norm*horas*8 + horas*11)
    print("El jornal total en euros es de:", total)
elif (horario =='D'):
    total =int(norm*horas*8 + dom*horas*11)
    print("El jornal total en euros es de:", total)"""
#EJERCICIO 5
"""lista = []
print ("Ingrese 8 numeros enteros en la lista:") #A FINES PRÁCTICOS 8, EL EJERCICIO ORIGINAL PIDE 20
for i in range (0,8):
    lista.append(int(input()))
valor = max(lista)
posic = (lista.index(valor)+1)
texto = "El número mayor es el {} y se encuentra en la posición {}"
print (texto.format(valor,posic))
print (lista)"""