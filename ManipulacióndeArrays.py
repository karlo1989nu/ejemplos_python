from array import array

def manipular_arrays():
    # Crear un array de enteros
    numeros = array('i', [10, 20, 30, 40, 50])
    print(f"Array inicial: {numeros.tolist()}")

    # Acceso a elementos
    print(f"Primer elemento: {numeros[0]}")
    print(f"Último elemento: {numeros[-1]}")

    # Modificación de elementos
    numeros[1] = 25
    print(f"Array después de modificar el segundo elemento: {numeros.tolist()}")

    # Agregar elementos
    numeros.append(60)
    print(f"Array después de agregar un elemento: {numeros.tolist()}")

    # Eliminar elementos
    numeros.remove(30)
    print(f"Array después de eliminar el elemento 30: {numeros.tolist()}")

    # Recorrer el array
    print("Recorriendo el array:")
    for numero in numeros:
        print(numero, end=" ")
    print()

# Llamar a la función
if __name__ == "__main__":
    manipular_arrays()