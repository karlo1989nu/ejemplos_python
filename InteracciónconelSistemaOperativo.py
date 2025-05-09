import os

def operaciones_archivos():
    print("Operaciones con archivos:")
    # Crear un archivo y escribir en él
    with open("archivo_prueba.txt", "w") as archivo:
        archivo.write("Este es un archivo de prueba.\nSegunda línea del archivo.")
    print("Archivo 'archivo_prueba.txt' creado y escrito.")

    # Leer el contenido del archivo
    with open("archivo_prueba.txt", "r") as archivo:
        contenido = archivo.read()
    print(f"Contenido del archivo:\n{contenido}")

    # Eliminar el archivo
    os.remove("archivo_prueba.txt")
    print("Archivo 'archivo_prueba.txt' eliminado.\n")

def operaciones_directorios():
    print("Operaciones con directorios:")
    # Obtener el directorio actual
    directorio_actual = os.getcwd()
    print(f"Directorio actual: {directorio_actual}")

    # Crear un nuevo directorio
    nuevo_directorio = "directorio_prueba"
    os.mkdir(nuevo_directorio)
    print(f"Directorio '{nuevo_directorio}' creado.")

    # Cambiar al nuevo directorio
    os.chdir(nuevo_directorio)
    print(f"Cambiado al directorio: {os.getcwd()}")

    # Volver al directorio anterior y eliminar el nuevo directorio
    os.chdir(directorio_actual)
    os.rmdir(nuevo_directorio)
    print(f"Directorio '{nuevo_directorio}' eliminado.\n")

def ejecutar_comandos():
    print("Ejecución de comandos del sistema:")
    # Listar archivos y directorios (comando dependiente del sistema operativo)
    comando = "dir" if os.name == "nt" else "ls"
    os.system(comando)

if __name__ == "__main__":
    operaciones_archivos()
    operaciones_directorios()
    ejecutar_comandos()