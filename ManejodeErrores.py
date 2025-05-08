def manejo_excepciones():
    try:
        # Ejemplo de división por cero
        numerador = int(input("Ingresa el numerador: "))
        denominador = int(input("Ingresa el denominador: "))
        resultado = numerador / denominador
        print(f"El resultado de la división es: {resultado}")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except ValueError:
        print("Error: Debes ingresar un número válido.")
    finally:
        print("Bloque finally: Este bloque se ejecuta siempre, independientemente de si hubo una excepción o no.")

def lanzar_excepcion():
    try:
        # Ejemplo de lanzamiento manual de una excepción
        edad = int(input("Ingresa tu edad: "))
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        print(f"Tu edad es: {edad}")
    except ValueError as e:
        print(f"Error capturado: {e}")
    finally:
        print("Bloque finally: Fin del manejo de excepciones.")

# Llamar a las funciones
if __name__ == "__main__":
    print("Ejemplo 1: Manejo de excepciones básicas")
    manejo_excepciones()

    print("\nEjemplo 2: Lanzamiento y captura de excepciones")
    lanzar_excepcion()
    