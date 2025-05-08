def ejemplos_conversiones():
    # Conversión de flotante a entero
    numero_decimal = 12.56
    numero_entero = int(numero_decimal)
    print(f"Conversión de flotante a entero: {numero_decimal} -> {numero_entero}")

    # Conversión de entero a flotante
    numero_entero = 42
    numero_flotante = float(numero_entero)
    print(f"Conversión de entero a flotante: {numero_entero} -> {numero_flotante}")

    # Conversión de número a cadena
    numero = 123
    cadena = str(numero)
    print(f"Conversión de número a cadena: {numero} -> '{cadena}'")

    # Conversión de cadena a número
    cadena = "456"
    numero = int(cadena)
    print(f"Conversión de cadena a número: '{cadena}' -> {numero}")

    # Conversión de cadena a flotante
    cadena_decimal = "78.90"
    numero_decimal = float(cadena_decimal)
    print(f"Conversión de cadena a flotante: '{cadena_decimal}' -> {numero_decimal}")

    # Conversión de booleano a entero
    booleano = True
    entero_booleano = int(booleano)
    print(f"Conversión de booleano a entero: {booleano} -> {entero_booleano}")

    # Conversión de entero a booleano
    numero = 0
    booleano = bool(numero)
    print(f"Conversión de entero a booleano: {numero} -> {booleano}")

# Llamar a la función
if __name__ == "__main__":
    ejemplos_conversiones()