from conta import Conta

'''Classe Conta poupança que implementa o tipo da classe Conta'''

class ContaPoupanca(Conta):

    '''Construtor da classe'''
    def __init__(self, nome, banco, numeroConta, saldo, limite,rendimento):
        super().__init__(nome, banco, numeroConta, saldo, limite)
        self.__rendimento=rendimento

#### Getters e Setters

    '''getter de rendimento'''
    @property
    def rendimento(self):
        return self.__rendimento
    '''setter de rendimento'''
    @rendimento.setter
    def set_redimento(self,rendimento):
        self.__rendimento=rendimento

    def __str__(self) -> str:
        return f"Rendimento Atual: {self.rendimento}"