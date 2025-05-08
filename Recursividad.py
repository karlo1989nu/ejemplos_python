# Función recursiva para calcular el factorial
def factorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:  # Llamada recursiva
        return n * factorial(n - 1)

# Ejemplo de uso
numero = int(input("Ingresa un número para calcular su factorial: "))
if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    print(f"El factorial de {numero} es: {factorial(numero)}")