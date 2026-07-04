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

    if espacios_disp == 0:
        print("No hay espacios disponibles.")
        return

    patente = input("Ingrese la patente: ")
    tipo = input("Ingrese el tipo de vehículo (Auto/Moto/Camión): ")
    hora = int(input("Ingrese la hora de ingreso: "))
    minuto = int(input("Ingrese el minuto de ingreso: "))

    patentes.append(patente)
    tipos_vehiculos.append(tipo)
    horas_entrada.append(hora)
    minutos_entrada.append(minuto)

    espacios_disp -= 1

    print("Vehículo ingresado correctamente.")


def retirar_vehiculo():
    pass


def mostrar_vehiculos():
    pass


def buscar_vehiculo():
    pass


def mostrar_estadisticas():
    pass


def mostrar_espacios():
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
