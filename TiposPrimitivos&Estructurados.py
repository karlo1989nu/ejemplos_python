# Ejemplos de Tipos Primitivos
def tipos_primitivos():
    
    entero = 42
    real = 3.14
    caracter = 'A'
    booleano = True

    print("Estos son los tipos de primitivos que existen en Python:")
    print("1. Entero")
    print("2. Real")
    print("3. Caracter")
    print("4. Booleano")

    opcion = input("Selecciona el tipo de primitivo que quieres ver: ")
    
    if opcion == "1":
        print(f"Entero: {entero}, Dominio: Números enteros, Operadores: +, -, *, /, %, //, **")
    elif opcion == "2":
        print(f"Real: {real}, Dominio: Números reales, Operadores: +, -, *, /, %, **")
    elif opcion == "3":
        print(f"Caracter: '{caracter}', Dominio: Caracteres Unicode, Operadores: + (concatenación), * (repetición)")
    elif opcion == "4":
        print(f"Booleano: {booleano}, Dominio: True/False, Operadores: and, or, not")


# Ejemplos de Tipos Estructurados
def tipos_estructurados():
    print("\n=== Tipos Estructurados ===")
    
    # Arrays (listas en Python)
    array = [1, 2, 3, 4, 5]
    print(f"Array: {array}, Dominio: Colección de elementos, Operadores: + (concatenación), * (repetición), [] (índice)")
    
    # Diccionarios (estructuras clave-valor)
    diccionario = {"id": 1, "nombre": "Libro", "precio": 29.99}
    print(f"Diccionario: {diccionario}, Dominio: Clave-Valor, Operadores: [] (acceso), in (verificar clave)")
    
    # Tuplas (estructuras inmutables)
    tupla = (1, "Python", 3.14)
    print(f"Tupla: {tupla}, Dominio: Colección inmutable, Operadores: [] (índice), in (verificar elemento)")
    
    # Conjuntos
    conjunto = {1, 2, 3, 4}
    print(f"Conjunto: {conjunto}, Dominio: Elementos únicos, Operadores: | (unión), & (intersección), - (diferencia)")

# Enumerados (simulados con clases en Python)
from enum import Enum
class Colores(Enum):
    ROJO = 1
    VERDE = 2
    AZUL = 3

def enumerados():
    print("\n=== Enumerados ===")
    print(f"Enumerado: {list(Colores)}, Dominio: {', '.join([color.name for color in Colores])}, Operadores: ==, !=")

# Función principal
"""def main():
    tipos_primitivos()
    tipos_estructurados()
    enumerados()
"""


if __name__ == "__main__":
    tipos_primitivos()
    tipos_estructurados()
    enumerados()
  