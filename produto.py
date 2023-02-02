'''classe que simula um produto'''
class Produto():

    '''Construtor da classe'''
    def __init__(self, nome,codigo=None):
        self.__nome = nome
        self.codigo=codigo

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
        return f"Nome: {self.nome}"