# Ejercicio 4

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

forzadas_seguidas = 0
bloqueado = False

print("--- LA BÓVEDA ---")
agente = input("Nombre del agente: ")
while not agente.isalpha():
    print("Error: Solo se permiten letras.")
    agente = input("Nombre del agente: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado:
    if alarma:
        estado_alarma = "ON"
    else:
        estado_alarma = "OFF"
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3 | Alarma: {estado_alarma}")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
        else:
            print("Error: opción fuera de rango.")
        opcion = input("Opción: ")

    if opcion == "1":
        forzadas_seguidas += 1
        energia -= 20
        tiempo -= 2

        if forzadas_seguidas == 3:
            print("La cerradura se trabó. Se activó la alarma.")
            alarma = True
            forzadas_seguidas = 0
        elif energia < 40:
            print("Poca energía: hay riesgo de alarma.")
            numero = input("Elegí un número (1-3): ")
            while not numero.isdigit() or int(numero) < 1 or int(numero) > 3:
                if not numero.isdigit():
                    print("Error: ingrese un número válido.")
                else:
                    print("Error: opción fuera de rango.")
                numero = input("Elegí un número (1-3): ")

            if numero == "3":
                print("Saltaste el sensor. Alarma activada.")
                alarma = True
            else:
                cerraduras_abiertas += 1
                print("Cerradura abierta.")
        else:
            cerraduras_abiertas += 1
            print("Cerradura abierta.")

    elif opcion == "2":
        forzadas_seguidas = 0
        energia -= 10
        tiempo -= 3
        print(">> Hackeando el panel...")
        for i in range(4):
            codigo_parcial += "A"
            print(f"> Paso {i + 1}/4 - Código: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("El código alcanzó. Cerradura abierta.")

    elif opcion == "3":
        forzadas_seguidas = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        if alarma:
            energia -= 10
            print("Con la alarma sonando descansas mal.")
        print("Descansaste.")

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueado = True

if cerraduras_abiertas == 3:
    print(f"¡VICTORIA! {agente} abrió la bóveda.")
elif bloqueado:
    print("DERROTA. El sistema se bloqueó por la alarma.")
else:
    print("DERROTA. Te quedaste sin energía o sin tiempo.")
