cancel = 0
asignaturas = []
print ("Inserte la asignatura que desee en la lista: ")
eleccion = int(input("Presione 1 para agregar asignatura, 2 para eliminarla\no cualquier otro valor para terminar\n"))
while cancel == 0:
    if eleccion == 1:
        print ("Inserte la asignaturas que desee en la lista: ")
        asignaturas.append(input())
        print(asignaturas)
    elif eleccion == 2:
        print ("Inserte la asignatura que desee eliminar de la lista: ")
        stringg = input()
        asignaturas.remove(stringg)
        print(asignaturas)
    else:
        cancel = 1
        print("Su lista finalizada es: ")
        for i in range (0,len(asignaturas)):
            print (asignaturas[i])
        break
    eleccion = int(input("Vuelva a elegir la operación que desee realizar:"))



