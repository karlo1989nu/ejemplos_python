# Funciones para manipular cadenas
def manipular_cadenas():
    cadena = input("Ingresa una cadena de texto: ")

    # Longitud de la cadena
    print(f"\nLongitud de la cadena: {len(cadena)}")

    # Convertir a mayúsculas y minúsculas
    print(f"En mayúsculas: {cadena.upper()}")
    print(f"En minúsculas: {cadena.lower()}")

    # Reemplazar caracteres
    caracter_a_reemplazar = input("Ingresa el carácter a reemplazar: ")
    nuevo_caracter = input("Ingresa el nuevo carácter: ")
    print(f"Cadena después del reemplazo: {cadena.replace(caracter_a_reemplazar, nuevo_caracter)}")

    # Dividir la cadena en palabras
    palabras = cadena.split()
    print(f"Palabras en la cadena: {palabras}")

    # Invertir la cadena
    print(f"Cadena invertida: {cadena[::-1]}")

    # Verificar si una subcadena está presente
    subcadena = input("Ingresa una subcadena para buscar: ")
    if subcadena in cadena:
        print(f"La subcadena '{subcadena}' está presente en la cadena.")
    else:
        print(f"La subcadena '{subcadena}' no está presente en la cadena.")

# Llamar a la función
if __name__ == "__main__":
    manipular_cadenas()