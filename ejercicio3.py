num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

print("La suma es:", suma)
print("La resta es:", resta)
print("La multiplicación es:", multiplicacion)

if num2 != 0:
    division = num1 / num2
    print("La división es:", division)
else:
    print("La división no se puede realizar (división por cero).")
