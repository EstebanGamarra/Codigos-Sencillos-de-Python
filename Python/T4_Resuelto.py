"""def primo(num):
    for i in range (2,num):
        if num%i==0:
            return False
    return True

#prog principal
numero=int(input("Número: "))
if primo(numero):
    print("Es primo")
else:
    print("No es primo")
"""
my_list = []
for i in range(6):
    my_list.append(int(input("Introduce un número ganador: ")))
my_list.sort()
print("Los números gnadores son " + str(my_list))