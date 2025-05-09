import random

def generar_numeros_aleatorios():
    print("Generación de números aleatorios:")
    # Número aleatorio entre 1 y 100
    numero = random.randint(1, 100)
    print(f"Número aleatorio entre 1 y 100: {numero}")

    # Número aleatorio flotante entre 0 y 1
    numero_flotante = random.random()
    print(f"Número aleatorio flotante entre 0 y 1: {numero_flotante}")

    # Selección aleatoria de una lista
    opciones = ["rojo", "verde", "azul", "amarillo"]
    eleccion = random.choice(opciones)
    print(f"Selección aleatoria de una lista: {eleccion}")

    # Mezclar una lista aleatoriamente
    random.shuffle(opciones)
    print(f"Lista mezclada aleatoriamente: {opciones}")

def simular_experimento():
    print("\nSimulación de un experimento:")
    # Simular el lanzamiento de un dado
    dado = random.randint(1, 6)
    print(f"Lanzamiento de un dado: {dado}")

    # Simular el lanzamiento de una moneda
    moneda = random.choice(["Cara", "Cruz"])
    print(f"Lanzamiento de una moneda: {moneda}")

def tomar_decisiones():
    print("\nTomar decisiones con números aleatorios:")
    # Decisión basada en un número aleatorio
    decision = random.random()
    if decision < 0.5:
        print("Decisión: Tomar el camino A.")
    else:
        print("Decisión: Tomar el camino B.")

if __name__ == "__main__":
    generar_numeros_aleatorios()
    simular_experimento()
    tomar_decisiones()