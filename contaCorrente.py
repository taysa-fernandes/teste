from conta import Conta
'''Classe Conta corrente que implementa o tipo da classe Conta'''
class ContaCorrente(Conta):
    '''Construtor da classe'''
    def __init__(self, nome, banco, numeroConta, saldo, limite,taxa):
        super().__init__(nome, banco, numeroConta, saldo, limite)
        self.__taxa=taxa
    '''getter de taxa'''
    @property
    def taxa(self):
        return self.__taxa
    '''setter de taxa'''
    @taxa.setter
    def set_taxa(self,taxa):
        self.__taxa=taxa