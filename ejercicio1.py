# Ejercicio 1
nombre = ""
cantidad = 0
total_sin_descuento = 0
total_con_descuento = 0

# 1. Validar nombre
nombre = input("Cliente: ")
while not nombre.isalpha():
    nombre = input("Cliente: ")

# 2. Validar cantidad
cantidad = input("Cantidad de productos: ")
while not cantidad.isdigit() or int(cantidad) == 0:
    cantidad = input("Cantidad de productos: ")
cantidad = int(cantidad)

# 3. Recorrer los productos con for
for i in range(cantidad):
    precio = input(f"Producto {i + 1} - Precio: ")
    while not precio.isdigit():
        precio = input(f"Producto {i + 1} - Precio: ")
    precio = int(precio)

    descuento = input("Descuento (S/N): ").lower()
    while descuento not in ("s", "n"):
        descuento = input("Descuento (S/N): ").lower()

    total_sin_descuento += precio
    if descuento == "s":
        total_con_descuento += precio * 0.9
    else:
        total_con_descuento += precio

# 4. Mostrar resultados
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
