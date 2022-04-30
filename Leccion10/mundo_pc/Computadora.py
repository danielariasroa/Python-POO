from mundo_pc.Monitor import Monitor
from mundo_pc.Teclado import Teclado
from mundo_pc.raton import Raton


class Computadora:
    contador_computadoras = 0
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora= Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        {self._nombre}: {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        '''
if __name__ == '__main__':
    monitor1 = Monitor('Lg', 16)
    teclado1 = Teclado('Samsung', 'Pene')
    raton1 = Raton('Hp', 'USB')
    computadora1 = Computadora('Daniel', monitor1, teclado1, raton1)
    print(computadora1)

    monitor2 = Monitor('Acer', 27)
    teclado2 = Teclado('Gamer', 'Ano')
    raton2 = Raton('Acer', 'Bluetho')
    computador2 = Computadora('compu2', monitor2, teclado2, raton2)
    print(computador2)