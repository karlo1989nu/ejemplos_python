def trabajar_con_listas():
    print("Trabajando con listas:")
    # Crear una lista
    lista = [10, 20, 30, 40, 50]
    print(f"Lista inicial: {lista}")

    # Modificar un elemento
    lista[1] = 25
    print(f"Lista después de modificar el segundo elemento: {lista}")

    # Agregar un elemento
    lista.append(60)
    print(f"Lista después de agregar un elemento: {lista}")

    # Eliminar un elemento
    lista.remove(30)
    print(f"Lista después de eliminar el elemento 30: {lista}")

    # Recorrer la lista
    print("Recorriendo la lista:")
    for elemento in lista:
        print(elemento, end=" ")
    print("\n")


def trabajar_con_tuplas():
    print("Trabajando con tuplas:")
    # Crear una tupla
    tupla = (10, 20, 30, 40, 50)
    print(f"Tupla inicial: {tupla}")

    # Acceder a elementos
    print(f"Primer elemento de la tupla: {tupla[0]}")
    print(f"Último elemento de la tupla: {tupla[-1]}")

    # Intentar modificar un elemento (esto generará un error)
    try:
        tupla[1] = 25
    except TypeError as e:
        print(f"Error al intentar modificar la tupla: {e}")

    # Recorrer la tupla
    print("Recorriendo la tupla:")
    for elemento in tupla:
        print(elemento, end=" ")
    print("\n")


if __name__ == "__main__":
    trabajar_con_listas()
    trabajar_con_tuplas()