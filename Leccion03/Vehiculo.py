class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'El vehiculo que tiene es de color {self.color} y tiene {self.ruedas} ruedas'


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'{super().__str__()}, su vehiculo es un coche que va a una velocidad de {self.velocidad}KmH'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'El vehiculo es una bicicleta de tipo {self.tipo}, {super().__str__()}'