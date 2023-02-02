'''classe que simula um produto'''
class Produto():

    '''Construtor da classe'''
    def __init__(self, nome, quantidade):
        self.__nome = nome
        self.__quantidade = quantidade

    '''Getter de nome'''
    @property
    def nome(self):
        return self.__nome
    '''setter de nome'''
    @nome.setter
    def set_nome(self,nome):
        self.__nome=nome
    @property
    def quantidade(self):
        return self.__quantidade
    '''setter de quantidade'''
    @quantidade.setter
    def set_nome(self, quantidade):
        self.__quantidade=quantidade
        
    def __str__(self) -> str:
        return f"Nome: {self.nome} Quantidade: {self.quantidade}"