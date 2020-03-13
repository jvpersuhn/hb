import random
class Deeler:
    def __init__(self):
        self.__listaEmbaralhada = ['2','3','4','5','6','7','8','9','10','A','J','Q','K']
        random.shuffle(self.__listaEmbaralhada)

    def retiraCartas(self) -> str:
        return self.__listaEmbaralhada.pop()
