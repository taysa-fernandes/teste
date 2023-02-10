'''classe que simula um produto'''
class Produto():

    '''Construtor da classe'''
    def __init__(self, nome: str, codigo: int ):
        self.__nome = nome
        self.codigo = codigo

    '''Getter de nome'''
    @property
    def nome(self):
        return self.__nome
    '''setter de nome'''
    @nome.setter
    def set_nome(self,nome):
        self.__nome=nome
        
    def __str__(self):
        return f"Nome: {self.nome} | Código: {self.codigo}"