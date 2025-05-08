# Procedimiento sin parámetros
def saludo():
    print("Hola, este es un procedimiento sin parámetros.")

# Procedimiento con parámetros
def saludo_personalizado(nombre, apellido):
    print(f"Hola, {nombre}. Este es un procedimiento con parámetros.")
    print(f"Gracias, {nombre} {apellido}")


# Función sin parámetros
def obtener_pi():
    return 3.14159

# Función con parámetros
def suma(a, b):
    return a + b

# Ejemplo de parámetros por valor
def duplicar_valor(numero):
    numero *= 2
    print(f"Valor dentro de la función (duplicado): {numero}")

# Ejemplo de parámetros por referencia
def agregar_elemento(lista):
    lista.append("Nuevo elemento")
    print(f"Lista dentro de la función: {lista}")

# Llamadas a los procedimientos y funciones
print("Procedimientos:")
saludo()
saludo_personalizado("Carlos", "Fernández")

print("\nFunciones:")
pi = obtener_pi()
print(f"El valor de pi es: {pi}")
resultado_suma = suma(5, 7)
print(f"La suma de 5 y 7 es: {resultado_suma}")

print("\nParámetros por valor:")
numero = 10
print(f"Valor antes de la función: {numero}")
duplicar_valor(numero)
print(f"Valor después de la función: {numero}")

print("\nParámetros por referencia:")
mi_lista = [1, 2, 3]
print(f"Lista antes de la función: {mi_lista}")
agregar_elemento(mi_lista)
print(f"Lista después de la función: {mi_lista}")