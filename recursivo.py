class RutaTuristica:
    def __init__(self, nombre, categoria, costo, tiempo, temporada, accesibilidad):
        self.nombre = nombre
        self.categoria = categoria
        self.costo = costo
        self.tiempo = tiempo
        self.temporada = temporada 
        self.accesibilidad = accesibilidad 

def encontrar_rutas(actual, destinos, presupuesto, tiempo_disponible, temporada, preferencias, ruta_actual, mejor_ruta):
    
    if presupuesto < 0 or tiempo_disponible < 0:
        return mejor_ruta  
    
    
    if sum(lugar.costo for lugar in ruta_actual) <= presupuesto and sum(lugar.tiempo for lugar in ruta_actual) <= tiempo_disponible:
        if len(ruta_actual) > len(mejor_ruta[0]):
            mejor_ruta[0] = ruta_actual[:]
    
    for destino in destinos:
        if destino not in ruta_actual and destino.categoria in preferencias and (temporada in destino.temporada or not destino.temporada):
            ruta_actual.append(destino)
            encontrar_rutas(destino, destinos, presupuesto - destino.costo, tiempo_disponible - destino.tiempo, temporada, preferencias, ruta_actual, mejor_ruta)
            ruta_actual.pop()
    
    return mejor_ruta[0]


print("Bienvenido a Rutas Turísticas Personalizadas")
presupuesto = int(input("Ingrese su presupuesto disponible: "))
tiempo_disponible = int(input("Ingrese el tiempo disponible en días: "))
temporada = input("Ingrese la temporada del año (verano, invierno, primavera, otoño): ")
print("Seleccione sus preferencias de viaje (separe por comas: aventura, gastronomía, cultura)")
preferencias = input().split(",")
preferencias = [p.strip() for p in preferencias]


destinos = [
    RutaTuristica("Parque Tayrona", "aventura", 100, 2, ["verano"], True),
    RutaTuristica("Cartagena Gastronómica", "gastronomía", 150, 3, ["invierno"], True),
    RutaTuristica("Villa de Leyva", "cultura", 120, 4, ["primavera"], True),
    RutaTuristica("Caño Cristales", "aventura", 200, 5, ["otoño"], False)
]

mejor_ruta = encontrar_rutas(None, destinos, presupuesto, tiempo_disponible, temporada, preferencias, [], [[]])


if mejor_ruta:
    print("\nMejor ruta encontrada:")
    for lugar in mejor_ruta:
        print(f"{lugar.nombre} - {lugar.categoria} - Costo: {lugar.costo}, Tiempo: {lugar.tiempo}")
else:
    print("\nNo se encontró una ruta que cumpla con sus restricciones. Intente ajustar sus preferencias.")
