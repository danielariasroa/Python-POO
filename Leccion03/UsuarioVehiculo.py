from Vehiculo import *

vehiculo = input('que tipo de vehiculo tiene? (Coche / Bicicleta): ')
if vehiculo == 'Coche':
    color = input('ingrese el color de su coche: ')
    ruedas = int(input('ingrese el numero de ruedas: '))
    velocidad = int(input('ingrese la velocidad en kilometros de su coche: '))

    usuario1 = Coche('Rojo', 4, 12)
    print(usuario1)
elif vehiculo == 'Bicicleta':
    color = input('ingrese el color de su bicicleta: ')
    ruedas = int(input('ingrese el numero de ruedas: '))
    tipo = input('ingrese el tipo de bicicleta que es (urbana / montaña etc...): ')
    usuario2 = Bicicleta('Azul', 2, "urbana")
    print(usuario2)
else: 
    print('El vehiculo que se ingreso no corresponde.')

