from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto.mostrar_detalle()))
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado('Juan', 2984828)

imprimir_detalles(empleado)

gerente = Gerente('Daniel', 15000000, 'Sistemas')
imprimir_detalles(gerente)

