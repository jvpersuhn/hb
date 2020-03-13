
class Jogador:
    def __init__(self):
        self.__tentativas = 10

    @property
    def tentativa(self):
        return self.__tentativas

    @tentativa.setter
    def tentativa(self, qtd):
        self.__tentativas -= qtd

