a = int(input("Ingresa el primer valor: "))
b = int(input("Ingresa el segundo valor: "))


# Operadores aritméticos
def aritméticos():
    operacion = int(input("Selecciona la operación a realizar utilizando el número correspondiente a la operación: 1. + 2. - 3. * 4. / 5. // 6. % 7.**"))

    if operacion == 1:
        print(f"Suma: {a} + {b} = {a + b}")
    elif operacion == 2:
        print(f"Resta: {a} - {b} = {a - b}")
    elif operacion == 3:
        print(f"Multiplicación: {a} * {b} = {a * b}")
    elif operacion == 4:
        print(f"División: {a} / {b} = {a / b}")
    elif operacion == 5:
        print(f"División entera: {a} // {b} = {a // b}")
    elif operacion == 6:
        print(f"Módulo: {a} % {b} = {a % b}")
    elif operacion == 7:
        print(f"Potencia: {a} ** {b} = {a ** b}")

# Operadores lógicos

def logicos():
    x = True
    y = False

    print("\nOperadores Lógicos:")
    print(f"x AND y: {x and y}")
    print(f"x OR y: {x or y}")
    print(f"NOT x: {not x}")

# Combinación de operadores aritméticos y lógicos

def combinado():
    resultado = (a + b > 10) and (a - b < 10)
    print("\nCombinación de Operadores:")
    print(f"(a + b > 10) AND (a - b < 10): {resultado}")

if __name__ == "__main__":
    aritméticos()
    logicos()
    combinado()