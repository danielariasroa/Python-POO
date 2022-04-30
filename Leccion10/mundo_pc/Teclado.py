from mundo_pc.dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador_teclado = 0
    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclado += 1
        self._id_teclado = Teclado.contador_teclado
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'ID : {self._id_teclado} Marca: {self._marca} Tipo entrada: {self._tipo_entrada}'


if __name__ == '__main__':
    teclado1 = Teclado('Samsung', 'Pene')
    print(teclado1)

    teclado2 = Teclado('Gamer', 'Ano')
    print(teclado2)
