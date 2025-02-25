import math

def calcular_formula_cuadratica(a, b, c):
    if a == 0:
        return "El coeficiente 'a' no puede ser 0 en una ecuación cuadrática."
    
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "La ecuación no tiene soluciones reales."
    
    raiz_discriminante = math.sqrt(discriminante)
    x1 = (-b + raiz_discriminante) / (2 * a)
    x2 = (-b - raiz_discriminante) / (2 * a)
    
    return x1, x2

a, b, c = 1, -3, 2  # Profe puede cambiar estos valores para probar
resultado = calcular_formula_cuadratica(a, b, c)
print("Las soluciones son:", resultado)
