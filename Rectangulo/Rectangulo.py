class Cubo:
    def __init__(self, base, altura, profundidad):
        self.base = base
        self.altura = altura
        self.profundidad = profundidad

    def areaDeCubo(self):

        return self.base * self.altura * self.profundidad

base = int(input('Introduzca la base del cubo: '))
altura = int(input('introduzca la altura del cubo: '))
profundidad = int(input('Introduca la profundidad del cubo: '))

resultado = Cubo(base, altura, profundidad)
print(f'el volumen del cubo es: {resultado.areaDeCubo()}')
