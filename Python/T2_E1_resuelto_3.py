precio_inicial = float(input("Ingrese el costo del producto:\n"))
iva = float(input("Ingrese el valor del IVA a aplicar al producto:\n"))
precio_final = (precio_inicial * iva) + precio_inicial
print("El precio final a pagar con IVA es: ", precio_final)