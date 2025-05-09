def trabajar_con_diccionarios():
    print("Trabajando con diccionarios:")
    # Crear un diccionario
    diccionario = {
        "nombre": "Juan",
        "edad": 25,
        "ciudad": "Madrid"
    }
    print(f"Diccionario inicial: {diccionario}")

    # Acceder a un valor
    print(f"Nombre: {diccionario['nombre']}")

    # Modificar un valor
    diccionario["edad"] = 26
    print(f"Diccionario después de modificar la edad: {diccionario}")

    # Agregar un nuevo par clave-valor
    diccionario["profesion"] = "Ingeniero"
    print(f"Diccionario después de agregar una profesión: {diccionario}")

    # Eliminar un par clave-valor
    del diccionario["ciudad"]
    print(f"Diccionario después de eliminar la ciudad: {diccionario}")

    # Recorrer el diccionario
    print("Recorriendo el diccionario:")
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")
    print("\n")


def trabajar_con_conjuntos():
    print("Trabajando con conjuntos:")
    # Crear un conjunto
    conjunto = {1, 2, 3, 4, 5}
    print(f"Conjunto inicial: {conjunto}")

    # Agregar un elemento
    conjunto.add(6)
    print(f"Conjunto después de agregar un elemento: {conjunto}")

    # Eliminar un elemento
    conjunto.discard(3)
    print(f"Conjunto después de eliminar el elemento 3: {conjunto}")

    # Operaciones de conjuntos
    otro_conjunto = {4, 5, 6, 7, 8}
    print(f"Unión de conjuntos: {conjunto | otro_conjunto}")
    print(f"Intersección de conjuntos: {conjunto & otro_conjunto}")
    print(f"Diferencia de conjuntos: {conjunto - otro_conjunto}")

    # Recorrer el conjunto
    print("Recorriendo el conjunto:")
    for elemento in conjunto:
        print(elemento, end=" ")
    print("\n")


if __name__ == "__main__":
    trabajar_con_diccionarios()
    trabajar_con_conjuntos()