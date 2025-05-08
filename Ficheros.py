def escribir_fichero(nombre_fichero, contenido):
    """Escribe contenido en un fichero."""
    with open(nombre_fichero, 'w') as fichero:
        fichero.write(contenido)
    print(f"Contenido escrito en el fichero '{nombre_fichero}'.")

def leer_fichero(nombre_fichero):
    """Lee y muestra el contenido de un fichero."""
    try:
        with open(nombre_fichero, 'r') as fichero:
            print(f"\nContenido del fichero '{nombre_fichero}':")
            for linea in fichero:
                print(linea, end='')  # Mostrar línea por línea
    except FileNotFoundError:
        print(f"El fichero '{nombre_fichero}' no existe.")

def recorrer_fichero(nombre_fichero):
    """Recorre un fichero secuencialmente y muestra cada línea."""
    try:
        with open(nombre_fichero, 'r') as fichero:
            print(f"\nRecorriendo el fichero '{nombre_fichero}':")
            while True:
                linea = fichero.readline()
                if not linea:  # Simula feof (fin de fichero)
                    break
                print(linea, end='')
    except FileNotFoundError:
        print(f"El fichero '{nombre_fichero}' no existe.")

# Ejemplo de uso
if __name__ == "__main__":
    nombre_fichero = "ejemplo.txt"
    contenido = "Primera línea del fichero.\nSegunda línea del fichero.\nTercera línea del fichero."

    # Escribir en el fichero
    escribir_fichero(nombre_fichero, contenido)

    # Leer el fichero
    leer_fichero(nombre_fichero)

    # Recorrer el fichero secuencialmente
    recorrer_fichero(nombre_fichero)