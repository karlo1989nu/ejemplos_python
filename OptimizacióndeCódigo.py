# Ejemplo de optimización con memoización
def fibonacci_memoizado(n, memo={}):
    """Calcula el n-ésimo número de Fibonacci utilizando memoización."""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoizado(n - 1, memo) + fibonacci_memoizado(n - 2, memo)
    return memo[n]

# Ejemplo de optimización eliminando bucles innecesarios
def suma_pares(lista):
    """Suma solo los números pares de una lista."""
    return sum(x for x in lista if x % 2 == 0)

# Ejemplo de uso eficiente de estructuras de datos
def contar_ocurrencias(lista):
    """Cuenta las ocurrencias de cada elemento en una lista utilizando un diccionario."""
    from collections import Counter
    return Counter(lista)

if __name__ == "__main__":
    # Optimización con memoización
    print("Fibonacci optimizado con memoización:")
    for i in range(10):
        print(f"Fibonacci({i}) = {fibonacci_memoizado(i)}")

    # Optimización eliminando bucles innecesarios
    print("\nSuma de números pares:")
    lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Lista: {lista_numeros}")
    print(f"Suma de pares: {suma_pares(lista_numeros)}")

    # Uso eficiente de estructuras de datos
    print("\nConteo de ocurrencias en una lista:")
    lista_elementos = ["manzana", "pera", "manzana", "naranja", "pera", "manzana"]
    print(f"Lista: {lista_elementos}")
    print(f"Conteo: {contar_ocurrencias(lista_elementos)}")