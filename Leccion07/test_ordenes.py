from Orden import Orden
from Producto import Producto


producto1 = Producto('Camisa', 20000)
producto2 = Producto('Pantalon', 39999)
producto3 = Producto('Calzones', 3191)
producto4 = Producto('Lenceria', 12399)

productos = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Orden(productos)
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
print(orden1)
print(f'Total de la orden: {orden1.sumar_productos()}')

orden2 = Orden(productos2)
print(orden2)
print(f'Total de la orden: {orden2.sumar_productos()}')