# Clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        """Método genérico que será sobrescrito por las subclases."""
        return "Sonido genérico"

    def describir(self):
        """Método para describir al animal."""
        print(f"Soy un/a {self.__class__.__name__} y me llamo {self.nombre}. {self.hacer_sonido()}")

# Subclase Perro
class Perro(Animal):
    def hacer_sonido(self):
        """Sobrescribe el método hacer_sonido."""
        return "Guau guau"
        
# Subclase Gato
class Gato(Animal):
    def hacer_sonido(self):
        """Sobrescribe el método hacer_sonido."""
        return "Miau miau"

# Subclase Vaca
class Vaca(Animal):
    def hacer_sonido(self):
        """Sobrescribe el método hacer_sonido."""
        return "Muuu"

# Demostración de herencia y polimorfismo
if __name__ == "__main__":
    # Crear objetos de las subclases
    perro = Perro("Rex")
    gato = Gato("Michi")
    vaca = Vaca("Lola")

    # Llamar al método describir (polimorfismo en acción)
    perro.describir()
    gato.describir()
    vaca.describir()