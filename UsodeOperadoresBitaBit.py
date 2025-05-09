def operaciones_bit_a_bit():
    # Solicitar dos números enteros al usuario
    a = int(input("Ingresa el primer número (a): "))
    b = int(input("Ingresa el segundo número (b): "))

    print(f"\nOperaciones bit a bit entre {a} y {b}:")

    # Operación AND bit a bit
    print(f"{a} & {b} (AND bit a bit): {a & b}")

    # Operación OR bit a bit
    print(f"{a} | {b} (OR bit a bit): {a | b}")

    # Operación XOR bit a bit
    print(f"{a} ^ {b} (XOR bit a bit): {a ^ b}")

    # Operación NOT bit a bit (complemento)
    print(f"~{a} (NOT bit a bit de a): {~a}")
    print(f"~{b} (NOT bit a bit de b): {~b}")

    # Desplazamiento a la izquierda
    print(f"{a} << 1 (a desplazado 1 bit a la izquierda): {a << 1}")
    print(f"{b} << 1 (b desplazado 1 bit a la izquierda): {b << 1}")

    # Desplazamiento a la derecha
    print(f"{a} >> 1 (a desplazado 1 bit a la derecha): {a >> 1}")
    print(f"{b} >> 1 (b desplazado 1 bit a la derecha): {b >> 1}")

# Llamar a la función
if __name__ == "__main__":
    operaciones_bit_a_bit()