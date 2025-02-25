metros = float(input("Ingrese la distancia en metros: "))

centimetros = metros * 100  # 1 metro = 100 cm
kilometros = metros / 1000  # 1 metro = 0.001 km
pies = metros * 3.28084     # 1 metro = 3.28084 pies
pulgadas = metros * 39.3701 # 1 metro = 39.3701 pulgadas

print(f"La distancia en centímetros es: {centimetros:.2f} cm")
print(f"La distancia en kilómetros es: {kilometros:.4f} km")
print(f"La distancia en pies es: {pies:.2f} ft")
print(f"La distancia en pulgadas es: {pulgadas:.2f} in")
