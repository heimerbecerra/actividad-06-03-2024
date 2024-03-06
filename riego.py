def riego_necesario(cultivo):
    if cultivo == "papa":
        return 5 # litros de agua por semana
    elif cultivo == "yuca":
        return 2 # litros de agua por semana
    elif cultivo == "zanahoria":
        return 8 # litros de agua por semana
    else:
        return "Cultivo no válido. Por favor, ingrese 'papa', 'yuca' o 'zanahoria'."

def obtener_cantidad(mensaje):
    while True:
        try:
            cantidad = int(input(mensaje))
            return cantidad
        except ValueError:
            print("Por favor, ingrese un número entero.")

def obtener_cultivo():
    while True:
        cultivo = input("Ingrese el cultivo que desea regar (papa, yuca o zanahoria): ").lower()
        if cultivo in ["papa", "yuca", "zanahoria"]:
            return cultivo
        else:
            print(riego_necesario(cultivo))

def dibujar_riego(cultivo, riego_total):
    print(f"{cultivo.capitalize()} Riego necesario:")
    for i in range(riego_total):
        print("|", end="")
    print("")
    for i in range(riego_total):
        print("*", end="")
    print("")

cultivo = obtener_cultivo()
cantidad = obtener_cantidad("Ingrese la cantidad de plantas de ese cultivo: ")
riego = riego_necesario(cultivo)

# Calcula el riego total
riego_total = riego * cantidad

# Dibuja el riego
dibujar_riego(cultivo, riego_total)

# Calcula el riego total para una semana
riego_semana = riego_total / 7

print(f"La cantidad de riego necesaria por semana para ese cultivo es: {riego_semana:.2f} litros por semana")