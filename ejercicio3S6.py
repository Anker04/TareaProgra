class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def sonido(self):
        pass  

class Perro(Animal):
    def sonido(self):
        return f"{self.nombre} dice: Woof Woof"

class Gato(Animal):
    def sonido(self):
        return f"{self.nombre} dice: Miau Miau"

class Pajaro(Animal):
    def sonido(self):
        return f"{self.nombre} hace: Pío Pío"

# Ejemplo de uso:
perro1 = Perro("perro", 3)
gato1 = Gato("gato", 2)
pajaro1 = Pajaro("pajaro", 1)

print("Sonido del Perro:")
print(perro1.sonido())

print("\nSonido del Gato:")
print(gato1.sonido())

print("\nSonido del Pájaro:")
print(pajaro1.sonido())
