

distancia_total = 0
numero_de_etapas = int(input("Ingrese la cantidad de etapas: "))

for i in range(numero_de_etapas):
    distancia_etapa = float(input(f"Ingrese la distancia para la etapa {i+1}: "))
    distancia_total += distancia_etapa

print(f"La distancia total es: {distancia_total}")
print(f"La cantidad de etapas es: {numero_de_etapas}")
print(f"El promedio de distancia por etapa es: {distancia_total / numero_de_etapas:.2f}")
