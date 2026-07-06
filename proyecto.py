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

    patente = input("Ingrese la patente: ").strip().upper()

    while patente == "":
        print("Error: la patente no puede estar vacía.")
        patente = input("Ingrese nuevamente la patente: ").strip().upper()

    if patente in patentes:
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

    while True:
        try:
            hora = int(input("Ingrese la hora de ingreso, sin minutos: "))

            if hora < 0 or hora > 23:
                print("Hora inválida. Debe estar entre 0 y 23.")
            else:
                break

        except ValueError:
            print("Error: ingrese primero la hora y luego los minutos. Ejemplo: hora 20 y después minuto 00.")

    while True:
        try:
            minuto = int(input("Ingrese el minuto de ingreso: "))

            if minuto < 0 or minuto > 59:
                print("Minuto inválido. Debe estar entre 0 y 59.")
            else:
                break

        except ValueError:
            print("Error: ingrese solo los minutos. Ejemplo: 00, 15, 30 o 45.")
            
    patentes.append(patente)
    tipos_vehiculos.append(tipo)
    horas_entrada.append(hora)
    minutos_entrada.append(minuto)

    espacios_disp -= 1
    total_vehiculos_atendidos += 1

    print("Vehículo ingresado correctamente.")


def retirar_vehiculo():
    global espacios_disp
    global total_recaudado

    if len(patentes) == 0:
        print("No hay vehículos registrados para retirar.")
        return

    patente = input("Ingrese la patente del vehículo a retirar: ").strip().upper()

    while patente == "":
        print("Error: la patente no puede estar vacía.")
        patente = input("Ingrese nuevamente la patente: ").strip().upper()

    posicion = -1

    for i in range(len(patentes)):
        if patentes[i] == patente:
            posicion = i
            break

    if posicion == -1:
        print("Error: la patente no está registrada.")
        return

    while True:
        try:
            hora_salida = int(input("Ingrese la hora de salida, sin minutos: "))
    
            if hora_salida < 0 or hora_salida > 23:
                print("Hora inválida. Debe estar entre 0 y 23.")
            else:
                break

        except ValueError:
            print("Error: ingrese primero la hora y luego los minutos. Ejemplo: hora 20 y después minuto 00.")


    while True:
        try:
            minuto_salida = int(input("Ingrese el minuto de salida: "))

            if minuto_salida < 0 or minuto_salida > 59:
                print("Minuto inválido. Debe estar entre 0 y 59.")
            else:
                break

        except ValueError:
            print("Error: ingrese solo los minutos. Ejemplo: 00, 15, 30 o 45.")
    
    hora_entrada = horas_entrada[posicion]
    minuto_entrada = minutos_entrada[posicion]

    minutos_entrada_total = hora_entrada * 60 + minuto_entrada
    minutos_salida_total = hora_salida * 60 + minuto_salida

    tiempo_permanencia = minutos_salida_total - minutos_entrada_total

    if tiempo_permanencia <= 0:
        print("Error: la hora de salida debe ser mayor que la hora de entrada.")
        return

    tipo = tipos_vehiculos[posicion]

    if tipo == "Moto":
        tarifa = TARIFA_MOTO
    elif tipo == "Auto":
        tarifa = TARIFA_AUTO
    else:
        tarifa = TARIFA_CAMION

    horas_cobradas = tiempo_permanencia // 60

    if tiempo_permanencia % 60 != 0:
        horas_cobradas += 1

    importe = horas_cobradas * tarifa

    total_recaudado += importe
    espacios_disp += 1

    print("\n===== RETIRO DE VEHÍCULO =====")
    print(f"Patente: {patentes[posicion]}")
    print(f"Tipo: {tipo}")
    print(f"Hora de entrada: {hora_entrada:02d}:{minuto_entrada:02d}")
    print(f"Hora de salida: {hora_salida:02d}:{minuto_salida:02d}")
    print(f"Tiempo de permanencia: {tiempo_permanencia} minutos")
    print(f"Horas cobradas: {horas_cobradas}")
    print(f"Importe a pagar: ${importe}")

    patentes.pop(posicion)
    tipos_vehiculos.pop(posicion)
    horas_entrada.pop(posicion)
    minutos_entrada.pop(posicion)

    print("Vehículo retirado correctamente.")


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

    patente_buscada = input("Ingrese la patente a buscar: ").strip().upper()

    while patente_buscada == "":
        print("Error: la patente no puede estar vacía.")
        patente_buscada = input("Ingrese nuevamente la patente: ").strip().upper()

    for i in range(len(patentes)):

        if patentes[i] == patente_buscada:

            print("\nVehículo encontrado.")
            print(f"Patente: {patentes[i]}")
            print(f"Tipo: {tipos_vehiculos[i]}")
            print(f"Hora de ingreso: {horas_entrada[i]:02d}:{minutos_entrada[i]:02d}")

            return

    print("Vehículo no encontrado.")


def mostrar_estadisticas():

    print("\n===== ESTADÍSTICAS DEL ESTACIONAMIENTO =====")

    print(f"Total recaudado: ${total_recaudado}")
    print(f"Total de vehículos atendidos: {total_vehiculos_atendidos}")

    print(f"Cantidad de motos: {cantidad_motos}")
    print(f"Cantidad de autos: {cantidad_autos}")
    print(f"Cantidad de camiones: {cantidad_camiones}")

    print(f"Espacios disponibles: {espacios_disp}")


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

        try:
            opcion = int(input("Seleccione una opción: "))

        except ValueError:
            print("Error: debe ingresar un número.")
            continue

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
