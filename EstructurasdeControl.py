# Estructuras condicionales
def estructuras_condicionales():
    numero = int(input("Ingresa un número: "))

    # Uso de if-else
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")

    # Uso de if-elif-else
    if numero < 0:
        print("El número es negativo.")
    elif numero == 0:
        print("El número es cero.")
    else:
        print("El número es positivo.")

# Bucles
def bucles():
    print("\nBucle for:")
    for i in range(1, 6):
        print(f"Iteración {i} en el bucle for.")

    print("\nBucle while:")
    contador = 1
    while contador <= 5:
        print(f"Iteración {contador} en el bucle while.")
        contador += 1

# Llamar a las funciones
estructuras_condicionales()
bucles()