from random import randint
class Frutas:
    def __init__(self):
        self.__frutas = ['banana','jabuticaba','pitanga','mirtilo','morango','abacaxi','cereja']

    def sorteiaFruta(self)-> str:
        return self.__frutas[randint(0,6)]
