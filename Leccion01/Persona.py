class Persona:

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

persona1 = Persona('daniel', 'roa', 21)
persona1.mostrar_detalle()

print(f'El objeto persona 1 es: {persona1.nombre} {persona1.apellido} y tiene {persona1.edad} años de edad')
persona2 = Persona('sofia', 'Roa', 22)
persona2.mostrar_detalle()