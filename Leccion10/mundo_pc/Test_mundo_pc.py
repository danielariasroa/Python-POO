from mundo_pc.Computadora import Computadora
from mundo_pc.Monitor import Monitor
from mundo_pc.Orden import Orden
from mundo_pc.Teclado import Teclado
from mundo_pc.raton import Raton

monitor1 = Monitor('Lg', 16)
teclado1 = Teclado('Samsung', 'Pene')
raton1 = Raton('Hp', 'USB')
computadora1 = Computadora('Daniel', monitor1, teclado1, raton1)
monitor2 = Monitor('Acer', 27)
teclado2 = Teclado('Gamer', 'Ano')
raton2 = Raton('Acer', 'Bluetho')
computador2 = Computadora('compu2', monitor2, teclado2, raton2)
monitor3 = Monitor('Acer', 27)
teclado3 = Teclado('Gamer', 'Ano')
raton3 = Raton('Acer', 'Bluetho')
computador3 = Computadora('compu3', monitor3, teclado3, raton3)

computadoras1 = [computadora1, computador2]
orden1 = Orden(computadoras1)
print(orden1)

orden1.agregar_computadoras(computador3)
print(orden1)

computadoras2 = [computadora1, computador3]
orden2 = Orden(computadoras2)
print(orden2)