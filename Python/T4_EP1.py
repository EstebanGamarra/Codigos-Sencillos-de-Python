def suma(s1,s2):
    print ("Su resultado es:",s2+s1)
    paso()
def resta(r1,r2):
    print ("Su resultado es:",r1-r2)
    paso()
def multiplicacion(m1,m2):
    print ("Su resultado es:",m1*m2)
    paso()
def division(d1,d2):
    print ("Su resultado es:",d1/d2)
    paso()
def int_teclado(numero):
    if numero == 1:
        ss1=int(input("Escriba el sumando:"))
        ss2=int(input("Escriba el sumador:"))
        suma(ss1,ss2)
    elif numero == 2:
        rr1=int(input("Escriba el minuendo:"))
        rr2=int(input("Escriba el sustraendo:"))
        resta(rr1,rr2)
    elif numero == 3:
        mm1=int(input("Escriba el multiplicando:"))
        mm2=int(input("Escriba el multiplicador:"))
        multiplicacion(mm1,mm2)
    elif numero == 4:
        dd1=int(input("Escriba el divindendo:"))
        dd2=int(input("Escriba el divisor:"))
        division(dd1,dd2)
    elif numero == 5:
        print ("***Se ha terminado el programa***")
    else:
         paso()
def paso():
    print("Elija una de 5 opciones, introduciendo el valor numérico adecuado:")
    print ("1. Sumar dos números")
    print ("2. Restar dos números")
    print ("3. Multiplicar dos números")
    print ("4. Dividir dos números")
    print ("5. Salir")
    numeroi = int(input())
    int_teclado(numeroi)
paso()



