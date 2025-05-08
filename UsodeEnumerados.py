from enum import Enum

# Definir un enumerado para los días de la semana
class DiasSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

# Función para mostrar el uso del enumerado
def mostrar_dia(dia):
    if dia in DiasSemana:
        print(f"El día seleccionado es: {dia.name} (valor: {dia.value})")
    else:
        print("El valor ingresado no corresponde a un día válido.")

# Ejemplo de uso
if __name__ == "__main__":
    print("Días de la semana:")
    for dia in DiasSemana:
        print(f"{dia.name} -> {dia.value}")

    print("\nSelecciona un día de la semana (1-7):")
    try:
        valor = int(input("Ingresa el número del día: "))
        dia_seleccionado = DiasSemana(valor)
        mostrar_dia(dia_seleccionado)
    except ValueError:
        print("Error: El número ingresado no corresponde a un día válido.")
        