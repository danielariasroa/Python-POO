class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return self.nombre + other.nombre

    def __sub__(self, other):
        return self.edad - other.edad

persona1 = Persona('maiz', 14)
persona2 = Persona('Con salsa', 2)
print(persona1+persona2)
print(persona1-persona2)

