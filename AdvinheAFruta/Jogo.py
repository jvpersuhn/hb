from Fruta import Frutas
from Jogador import Jogador

class Jogo:
    def __init__(self):
        self.__frutas = Frutas()

    def jogar(self):
        fruta = self.__frutas.sorteiaFruta()
        letras = ['_'] * len(fruta)
        j = Jogador()

        while True:

            if j.tentativa == 0:
                print('Suas tentativas terminaram')
                break
            print(f'Tentativas restantes {j.tentativa}')
            l = input('Digite uma letra: ')
            if len(l) == 1:
                if l in fruta:
                    letras = self.__colocaLetra(fruta, l, letras)
                else:
                    print('letra nao esta na palavra\n')
                    j.tentativa = 1
            else:
                if l == fruta:
                    print('Voce acertou')
                    break
                else:
                    print('Errouuuuu\n')
                    j.tentativa = 1

            if not '_' in letras:
                print('Voce acertou')
                break


    def __colocaLetra(self, palavra : str, letra : str, palavra_final : list):
        for i in range(0,len(palavra)):
            if palavra[i] == letra:
                palavra_final[i] = letra

        print(f"{''.join(palavra_final)}\n")

        return palavra_final



