def encontrar_maximo(a, b, c):
    """Encuentra el máximo de tres números."""
    if a >= b and a >= c:
        maximo = a
    elif b >= a and b >= c:
        maximo = b
    else:
        maximo = c
    return maximo

def max():
    print("Encuentra el máximo de tres números.")
    a = float(input("Ingresa el primer número (a): "))
    b = float(input("Ingresa el segundo número (b): "))
    c = float(input("Ingresa el tercer número (c): "))

    maximo = encontrar_maximo(a, b, c)
    print(f"El máximo de los números {a}, {b} y {c} es: {maximo}")

# Ejemplo de uso
if __name__ == "__main__":
    max()
    