# Constantes

TARIFA_MOTO = 500
TARIFA_AUTO = 1000
TARIFA_CAMION = 1500

CAPACIDAD = 50

# Variables globales

espacios_disp = CAPACIDAD

total_recaudado = 0
total_vehiculos_atendidos = 0

cantidad_autos = 0
cantidad_motos = 0
cantidad_camiones = 0

# Listas

patentes = []
tipos_vehiculos = []
horas_entrada = []
minutos_entrada = []


# Funciones

def mostrar_menu():
    print("\n===== GESTIÓN DE ESTACIONAMIENTO =====")
    print("1. Ingresar vehículo")
    print("2. Retirar vehículo")
    print("3. Mostrar vehículos")
    print("4. Buscar vehículo")
    print("5. Mostrar estadísticas")
    print("6. Mostrar espacios disponibles")
    print("7. Salir")


def ingresar_vehiculo():
    global espacios_disp
    global total_vehiculos_atendidos
    global cantidad_autos
    global cantidad_motos
    global cantidad_camiones

    if espacios_disp == 0:
        print("No hay espacios disponibles.")
        return

    patente = input("Ingrese la patente: ")

    for p in patentes:
        if p == patente:
            print("Error: la patente ya está registrada.")
            return

    print("\nTipo de vehículo")
    print("1. Moto")
    print("2. Auto")
    print("3. Camión")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        tipo = "Moto"
        cantidad_motos += 1

    elif opcion == 2:
        tipo = "Auto"
        cantidad_autos += 1

    elif opcion == 3:
        tipo = "Camión"
        cantidad_camiones += 1

    else:
        print("Tipo de vehículo inválido.")
        return

    hora = int(input("Ingrese la hora de ingreso: "))

    while hora < 0 or hora > 23:
        print("Hora inválida.")
        hora = int(input("Ingrese nuevamente la hora: "))

    minuto = int(input("Ingrese el minuto de ingreso: "))

    while minuto < 0 or minuto > 59:
        print("Minuto inválido.")
        minuto = int(input("Ingrese nuevamente el minuto: "))

    patentes.append(patente)
    tipos_vehiculos.append(tipo)
    horas_entrada.append(hora)
    minutos_entrada.append(minuto)

    espacios_disp -= 1
    total_vehiculos_atendidos += 1

    print("Vehículo ingresado correctamente.")


def retirar_vehiculo():
    pass


def mostrar_vehiculos():
    if len(patentes) == 0:
        print("No hay vehículos estacionados.")
        return

    print("\n===== VEHÍCULOS ESTACIONADOS =====")

    for i in range(len(patentes)):
        print(f"Patente: {patentes[i]}")
        print(f"Tipo: {tipos_vehiculos[i]}")
        
        # El formato :02d muestra la hora y los minutos con dos dígitos
        print(f"Hora de ingreso: {horas_entrada[i]:02d}:{minutos_entrada[i]:02d}")

        print("-----------------------------")


def buscar_vehiculo():

    patente_buscada = input("Ingrese la patente a buscar: ")

    for i in range(len(patentes)):

        if patentes[i] == patente_buscada:

            print("\nVehículo encontrado.")
            print(f"Patente: {patentes[i]}")
            print(f"Tipo: {tipos_vehiculos[i]}")
            print(f"Hora de ingreso: {horas_entrada[i]}:{minutos_entrada[i]:02d}")

            return

    print("Vehículo no encontrado.")


def mostrar_estadisticas():
    pass


def mostrar_espacios():
    ocupados = CAPACIDAD - espacios_disp

    print("\n===== ESPACIOS DEL ESTACIONAMIENTO =====")
    print(f"Capacidad total: {CAPACIDAD}")
    print(f"Espacios ocupados: {ocupados}")
    print(f"Espacios disponibles: {espacios_disp}")

# Función principal

def main():

    opcion = 0

    while opcion != 7:

        mostrar_menu()

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            ingresar_vehiculo()

        elif opcion == 2:
            retirar_vehiculo()

        elif opcion == 3:
            mostrar_vehiculos()

        elif opcion == 4:
            buscar_vehiculo()

        elif opcion == 5:
            mostrar_estadisticas()

        elif opcion == 6:
            mostrar_espacios()

        elif opcion == 7:
            print("Saliendo del sistema...")

        else:
            print("Opción inválida. Intente nuevamente.")
main()
