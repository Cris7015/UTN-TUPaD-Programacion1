# Ejercicio 2
usuario = "alumno"
clave = "python123"
intentos = 0
acceso_concedido = False

while intentos < 3 and not acceso_concedido:
    usuario_inicio = input(f"Intento {intentos + 1}/3 - Usuario: ")
    clave_inicio = input("Clave: ")

    if usuario_inicio == usuario and clave_inicio == clave:
        print("Acceso concedido.")
        acceso_concedido = True

    else:
        print("Error: credenciales inválidas.")
        intentos += 1

while acceso_concedido:
    print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
    opcion = input("Opción: ")
    if not opcion.isdigit():
        print("Error: ingrese un número válido.")
    elif int(opcion) < 1 or int(opcion) > 4:
        print("Error: opción fuera de rango.")
    elif opcion == "1":
        print("Inscripto")
    elif opcion == "2":
        clave_nueva = input("Nueva clave: ")
        while len(clave_nueva) < 6:
            print("Error: mínimo 6 caracteres.")
            clave_nueva = input("Nueva clave: ")
        confirmacion = input("Confirmar clave: ")
        if confirmacion == clave_nueva:
            clave = clave_nueva
            print("Clave actualizada.")
        else:
            print("Error: las claves no coinciden.")
    elif opcion == "3":
        print("Sos el mejor alumno de la UTN")
    elif opcion == "4":
        break

if acceso_concedido == False:
    print("Cuenta bloqueada")
else:
    print("Hasta luego")
