'''Classe que simula uma farmácia'''

class Farmacia():

    '''Construtor da classe'''
    def __init__(self,nome,localizacao,cnpj,conta):
        self.__nome=nome
        self.__localizacao=localizacao
        self.__cnpj=cnpj
        self.__conta=conta
        self.pedidos=[]

#### Getters e Setters

    '''Getter de nome'''
    @property
    def nome(self):
        return self.__nome
    '''setter de nome'''
    @nome.setter
    def set_nome(self,nome):
        self.__nome=nome
    '''Getter de localizacao'''
    @property
    def localizacao(self):
        return self.__localizacao
    '''setter de localizacao'''
    @localizacao.setter
    def set_localizacao(self,localizacao):
        self.__localizacao=localizacao
    '''Getter de cnpj'''
    @property
    def cnpj(self):
        return self.__cnpj
    '''setter de cliente'''
    @cnpj.setter
    def set_cnpj(self,cnpj):
        self.__cnpj=cnpj
    '''Getter de conta'''
    @property
    def conta(self):
        return self.__conta
    '''setter de conta'''
    @conta.setter
    def set_conta(self,conta):
        self.__conta=conta
        
    def __str__(self) -> str:
        return f"Nome: {self.nome} Localização: {self.localizacao} CNPJ: {self.cnpj} Conta: {self.conta}"