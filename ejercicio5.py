# Ejercicio 5
vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
daño_ataque_pesado = 15
daño_base_enemigo = 12
turno_gladiador = True

print("--- BIENVENIDO A LA ARENA ---")
nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")
print("=== INICIO DEL COMBATE === ")
while vida_gladiador > 0 and vida_enemigo > 0:
    print(f"{nombre} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones_vida}")
    print("Elige acción: ")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion = input("Opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        if not opcion.isdigit():
            print("Error: Ingrese un número válido.")
        else:
            print("Error: Opción fuera de rango.")
        opcion = input("Opción: ")
    if opcion == "1":
        if vida_enemigo < 20:
            daño_final = daño_ataque_pesado * 1.5
        else:
            daño_final = daño_ataque_pesado
        vida_enemigo -= daño_final
        print(f"¡Atacaste al enemigo por {daño_final} puntos de daño!")
    elif opcion == "2":
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")
    elif opcion == "3":
        if pociones_vida > 0:
            vida_gladiador += 30
            pociones_vida -= 1
            print(f"¡Te curaste! Ahora tu vida es de {vida_gladiador}")
        else:
            print("¡No quedan pociones!")

    if vida_enemigo > 0:
        vida_gladiador -= daño_base_enemigo
        print(f"¡El enemigo te atacó por {daño_base_enemigo} puntos de daño!")
if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
