# Clase Coche
class Coche:
    def __init__(self, marca, modelo, año):
        """Constructor para inicializar los atributos del coche."""
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False

    def encender(self):
        """Método para encender el coche."""
        if not self.encendido:
            self.encendido = True
            print(f"El coche {self.marca} {self.modelo} está encendido.")
        else:
            print(f"El coche {self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        """Método para apagar el coche."""
        if self.encendido:
            self.encendido = False
            print(f"El coche {self.marca} {self.modelo} está apagado.")
        else:
            print(f"El coche {self.marca} {self.modelo} ya está apagado.")

    def mostrar_informacion(self):
        """Método para mostrar la información del coche."""
        estado = "encendido" if self.encendido else "apagado"
        print(f"Coche: {self.marca} {self.modelo}, Año: {self.año}, Estado: {estado}")


# Crear objetos de la clase Coche
if __name__ == "__main__":
    coche1 = Coche("Toyota", "Corolla", 2020)
    coche2 = Coche("Ford", "Mustang", 2022)

    # Usar los métodos de los objetos
    coche1.mostrar_informacion()
    coche1.encender()
    coche1.mostrar_informacion()
    coche1.apagar()

    print()  # Separador

    coche2.mostrar_informacion()
    coche2.encender()
    coche2.apagar()