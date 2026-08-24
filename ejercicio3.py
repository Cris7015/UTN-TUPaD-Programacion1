# Ejercicio 3
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Nombre del operador: ")
while not operador.isalpha():
    operador = input("Nombre del operador: ")

while True:
    print("1) Reservar 2) Cancelar 3) Ver agenda 4) Resumen 5) Cerrar")
    opcion = input("Opcion: ")
    if not opcion.isdigit():
        print("Error: ingrese un número válido.")
    elif int(opcion) < 1 or int(opcion) > 5:
        print("Error: opción fuera de rango.")
    elif opcion == "1":
        dia = input("Día (1.Lunes, 2.Martes): ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            dia = input("Día (1.Lunes, 2.Martes): ")
        paciente = input("Nombre del paciente: ") 
        while not paciente.isalpha():
            paciente = input("Nombre del paciente: ")
        if dia == "1":
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Este paciente ya tiene turno para el lunes")
            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado")
            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado")
            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado")
            elif lunes4 == "":
                print("Turno reservado")
                lunes4 = paciente
            else:
                print("No hay cupos disponibles para el lunes")
        else:
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Este paciente ya tiene turno para el martes")
            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado")
            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado")
            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado")
            else:
                print("No hay cupos disponibles para el martes")
    elif opcion == "2":
        dia = input("Día (1.Lunes, 2.Martes): ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            dia = input("Día (1.Lunes, 2.Martes): ")

        paciente = input("Nombre del paciente: ")
        while not paciente.isalpha():
            paciente = input("Nombre del paciente: ")

        if dia == "1":
            if lunes1 == paciente:
                lunes1 = ""
                print("Turno cancelado")
            elif lunes2 == paciente:
                lunes2 = ""
                print("Turno cancelado")
            elif lunes3 == paciente:
                lunes3 = ""
                print("Turno cancelado")
            elif lunes4 == paciente:
                lunes4 = ""
                print("Turno cancelado")
            else:
                print("Ese paciente no tiene turno el Lunes")
        else:
            if martes1 == paciente:
                martes1 = ""
                print("Turno cancelado")
            elif martes2 == paciente:
                martes2 = ""
                print("Turno cancelado")
            elif martes3 == paciente:
                martes3 = ""
                print("Turno cancelado")
            else:
                print("Ese paciente no tiene turno el Martes")
    elif opcion == "3":
        dia = input("Día (1.Lunes, 2.Martes): ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            dia = input("Dia (1.Lunes, 2.Martes): ")

        if dia == "1":
            print("Agenda del Lunes:")
            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {lunes1}")
            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {lunes2}")
            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {lunes3}")
            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print(f"Turno 4: {lunes4}")
        else:
            print("Agenda del Martes")
            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {martes1}")
            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {martes2}")
            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {martes3}")
    elif opcion == "4":
        ocupados_lunes = 0
        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1
        ocupados_martes = 0
        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1

        print(f"Lunes: {ocupados_lunes} ocupados, {4 - ocupados_lunes} disponibles")
        print(f"Martes: {ocupados_martes} ocupados, {3 - ocupados_martes} disponibles")

        if ocupados_lunes > ocupados_martes:
            print("El dia con mas turnos es el Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("El dia con mas turnos es el Martes")
        else:
            print("Igual")
    elif opcion == "5":
        break
