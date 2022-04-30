class MyClase:

    variableDeclase = 'esta es una variable de clase'

    def __init__(self, variableInstancia):

        self.variableInstancia = variableInstancia

    @staticmethod
    def metodo_estatico():
        print(MyClase.variableDeclase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variableDeclase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variableInstancia)
        print(MyClase.variableDeclase)

mazorca = MyClase('mazorca')
mazorca.metodo_clase()

mazorca.metodo_instancia()