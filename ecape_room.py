import json

print(input("Quieres iniciar el juego? (s/n): "))
print("Bienvenido al juego de escape de la habitación.")
print("Te encuentras en una habitación y tienes hacer 5 algoritmos para escapar.")
print("Escoge que algoritmo quieres ver en ejecucion:")
print("1. Factorial simple")
print("2. Fibonacci optimizado")
print ("3. Busqueda en directorio")
print("4. Division y conquista")
print("5. Backtracking")
print("6. Salir")

def factorial_simple(n):
    if n == 0:
        return 1
    else:
        return n * factorial_simple(n-1)
    

def fibonacci_recursividad(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursividad(n-1) + fibonacci_recursividad(n-2)


def busqueda_directorio():
    print("Puedes buscar una cancion en el directorio.")
    print("Introduce el nombre o autor de la cancion: ")
    cancion = input()
    
    def buscar_recursivo(data, cancion, index=0):
        if index >= len(data):
            return None
        if cancion in data[index]:
            return data[index]
        return buscar_recursivo(data, cancion, index + 1)
    
    try:
        with open("canciones.json", "r") as file:
            data = json.load(file)
            resultado = buscar_recursivo(data, cancion)
            if resultado:
                return resultado
            else:
                print("Cancion no encontrada.")
    except FileNotFoundError:
        print("El archivo canciones.json no se encuentra.")
    except json.JSONDecodeError:
        print("Error al leer el archivo JSON.")


opcion = int(input("Opcion: "))
if opcion == 1:
    print("Factorial simple")
    n = int(input("Introduce un número: "))
    print(factorial_simple(n))

elif opcion == 2:
    print("Fibonacci optimizado con resursividad")
    n = int(input("Introduce un número: "))
    print(fibonacci_recursividad(n))
elif opcion == 3:
    print("Busqueda en directorio")
    resultado = busqueda_directorio()
    if resultado:
        print("Cancion encontrada:", resultado)
elif opcion == 4:
    print("Division y conquista")
    import division_y_conquista
elif opcion == 5:
    print("Backtracking")
    import backtracking
elif opcion == 6:
    print("Salir")
else: 
    print("Opcion no valida")


