from Jogador import Jogador

class BlackJack:
    def jogar(self):
        lista = self.__numeroJogadores()



    def __numeroJogadores(self, lista : list) -> list:
        try:
            numero = int(input('Digite a quantidade de jogadores: '))
            while numero < 2 or numero > 7:
                numero = int(input('O numero deve ser no minimo 2 e no maximo 7'))

            for i in range(0,numero):
                j = Jogador(f'Jogador {i}')
                lista.append(j)
        except:
            print('Digite apenas numeros')
