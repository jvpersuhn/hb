from Deeler import Deeler

class Jogador:
    def __init__(self, nome):
        self.__cartas = []
        self.__pontuacao = 0
        self.__situacao = True
        self.__deeler = Deeler()
        self.__nome = nome
        self.__pedirCarta = True

    def pedirCarta(self) -> bool:
        carta = self.__deeler.retiraCartas()
        return self.verificaCarta(carta)

    def verificaCarta(self, carta : str):
        ponto = 0
        self.__cartas.append(carta)
        if carta.isdigit():
            carta = int(carta)
            ponto = carta
            self.__pontuacao += carta
        else:
            if carta == 'A':
                if len(self.__cartas) == 0:
                    ponto = 11
                    self.__pontuacao += 11
                else:
                    ponto = 1
                    self.__pontuacao += 1
            else:
                ponto = 10
                self.__pontuacao += 10
        print(f'A carta retirada foi: {carta} que tem o valor {ponto} \n')
        return self.verificaPontuacao()

    def verificaPontuacao(self):
        if self.__pontuacao > 21:
            self.__situacao = False

    @property
    def pontuacao(self):
        return self.__pontuacao

    @property
    def situacao(self):
        return self.__situacao

    @property
    def nome(self):
        return self.__nome

    @property
    def situacaoCarta(self):
        return self.__pedirCarta

    @situacaoCarta.setter
    def situacaoCarta(self, op):
        self.__pedirCarta = op
