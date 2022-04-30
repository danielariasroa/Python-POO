from Cuadrado import Cuadrado
from Rectangulo import Rectangulo


print('Creacion de objeto CUADRADO'.center(60,'.'))
cuadrado1 = Cuadrado(lado=91, color='negro')
print(cuadrado1.calcular_area())
print(cuadrado1)

print('Creacion de objeto RECTANGULO'.center(60,'.'))
rectangulo1 = Rectangulo(ancho=3, alto=4, color='Morado')
print(rectangulo1.calcularArea())
print(rectangulo1)