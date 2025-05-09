import threading
import time

def tarea_concurrente(nombre, duracion):
    print(f"Tarea {nombre} iniciada.")
    time.sleep(duracion)
    print(f"Tarea {nombre} completada después de {duracion} segundos.")

def ejemplo_threading():
    print("Ejemplo de programación concurrente con threading:")
    # Crear hilos
    hilo1 = threading.Thread(target=tarea_concurrente, args=("A", 2))
    hilo2 = threading.Thread(target=tarea_concurrente, args=("B", 3))

    # Iniciar hilos
    hilo1.start()
    hilo2.start()

    # Esperar a que los hilos terminen
    hilo1.join()
    hilo2.join()
    print("Todas las tareas concurrentes han finalizado.\n")

if __name__ == "__main__":
    ejemplo_threading()

import multiprocessing
import time

def tarea_paralela(nombre, duracion):
    print(f"Tarea {nombre} iniciada en el proceso {multiprocessing.current_process().name}.")
    time.sleep(duracion)
    print(f"Tarea {nombre} completada después de {duracion} segundos.")

def ejemplo_multiprocessing():
    print("Ejemplo de programación paralela con multiprocessing:")
    # Crear procesos
    proceso1 = multiprocessing.Process(target=tarea_paralela, args=("A", 2), name="Proceso-1")
    proceso2 = multiprocessing.Process(target=tarea_paralela, args=("B", 3), name="Proceso-2")

    # Iniciar procesos
    proceso1.start()
    proceso2.start()

    # Esperar a que los procesos terminen
    proceso1.join()
    proceso2.join()
    print("Todas las tareas paralelas han finalizado.\n")

if __name__ == "__main__":
    ejemplo_threading()
    ejemplo_multiprocessing()