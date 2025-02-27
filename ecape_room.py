import json

def factorial_simple(n):
    if n == 0:
        return 1
    else:
        return n * factorial_simple(n - 1)

def fibonacci_recursividad(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursividad(n - 1) + fibonacci_recursividad(n - 2)

def busqueda_directorio():
    
    cancion = input("Busca una canción o artista: ").strip()
    
    def buscar_recursivo(data, clave, index=0):
        if index >= len(data):
            return None
        
        if (clave.lower() in data[index]["nombre_cancion"].lower() or
            clave.lower() in data[index]["autor"].lower()):
            return data[index]
        return buscar_recursivo(data, clave, index + 1)
    
    try:
        with open("canciones.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            resultado = buscar_recursivo(data, cancion)
            if resultado:
                return resultado
            else:
                print("Canción no encontrada.")
                return None
    except FileNotFoundError:
        print("El archivo canciones.json no se encuentra.")
        return None
    except json.JSONDecodeError:
        print("Error al leer el archivo JSON.")
        return None

def busqueda_binaria(arr, x, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return busqueda_binaria(arr, x, low, mid - 1)
    else:
        return busqueda_binaria(arr, x, mid + 1, high)

def generar_permutaciones(s):
    result = []
    def permute(prefix, remaining):
        if len(remaining) == 0:
            result.append(prefix)
        else:
            for i in range(len(remaining)):
                permute(prefix + remaining[i], remaining[:i] + remaining[i+1:])
    permute("", s)
    return result



def opcion_factorial():
    try:
        n = int(input("Calcular factorial de: "))
        print("Resultado:", factorial_simple(n))
    except ValueError:
        print("Ingresa un número válido.")

def opcion_fibonacci():
    try:
        n = int(input("Calcular Fibonacci de: "))
        print("Término Fibonacci:", fibonacci_recursividad(n))
    except ValueError:
        print("Ingresa un número válido.")

def opcion_busqueda_directorio():
    resultado = busqueda_directorio()
    if resultado:
        print("Resultado:", resultado)

def opcion_busqueda_binaria():
    try:
        numeros = list(map(int, input("Introduce una lista de números ordenados separados por espacios: ").split()))
        x = int(input("Buscar número: "))
        index = busqueda_binaria(numeros, x, 0, len(numeros) - 1)
        if index != -1:
            print(f"Número encontrado en la posición {index}.")
        else:
            print("Número no encontrado.")
    except ValueError:
        print("Ingresa números válidos.")

def opcion_generar_permutaciones():
    s = input("Introduce una cadena: ")
    perms = generar_permutaciones(s)
    print("Permutaciones:")
    for p in perms:
        print(p)


def mostrar_menu_nivel(nivel):
    print(f"\n--- Nivel {nivel} ---")
    print("Escoge el algoritmo correcto para avanzar:")
    print("1. Factorial simple")
    print("2. Fibonacci recursivo")
    print("3. Busqueda en directorio")
    print("4. Búsqueda binaria recursiva")
    print("5. Generar permutaciones")
    print("6. Salir")


opciones = {
    1: opcion_factorial,
    2: opcion_fibonacci,
    3: opcion_busqueda_directorio,
    4: opcion_busqueda_binaria,
    5: opcion_generar_permutaciones
}


def main():
    iniciar = input("¿Quieres iniciar el juego? (s/n): ").lower()
    if iniciar != 's':
        print("Juego no iniciado. Saliendo...")
        return

    print("\nBienvenido al juego de escape de la habitación.")
    print("Cada nivel tiene un acertijo recursivo basado en el número de nivel.")
    print("Para avanzar, debes seleccionar la opción que corresponda al nivel actual.")

    for nivel in range(1, 6):
        while True:
            mostrar_menu_nivel(nivel)
            eleccion = input("Elección: ").strip()
            try:
                opcion = int(eleccion)
            except ValueError:
                print("Ingresa un número válido.")
                continue

            if opcion == 6:
                print("Saliendo del juego...")
                return

            if opcion == nivel:
                if opcion in opciones:
                    opciones[opcion]()
                else:
                    print("Opción no implementada.")
                print(f"¡Nivel {nivel} completado!")
                break
            else:
                print("Algoritmo incorrecto para este nivel. Intenta de nuevo.")
        if nivel < 5:
            input("Presiona Enter para continuar al siguiente nivel...")
    print("\n¡Felicidades! Has resuelto todos los acertijos y escapado de la habitación.")

if __name__ == "__main__":
    main()
