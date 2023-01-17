from conta import Conta
'''Classe que representa uma pessoa na vida real'''
class Pessoa:
    '''Construtor da classe'''
    def __init__(self,nome,telefone,cpf,conta,senha):
        self.__nome=nome
        self.__telefone=telefone
        self.__cpf=cpf
        self.__conta=conta
        self.__senha=senha
    '''getter de nome'''
    @property
    def nome(self):
        return self.__nome
    '''setter de nome'''
    def set_nome(self,nome):
        self.__nome=nome
    '''getter de telefone'''
    @property
    def telefone(self):
        return self.__telefone
    '''setter de telefone'''
    def set_telefone(self,telefone):
        self.__telefone=telefone
    '''getter de taxa'''
    @property
    def cpf(self):
        return self.__cpf
    '''setter de cpf'''
    def set_cpf(self,cpf):
        self.__cpf=cpf
    '''getter de conta'''
    @property
    def conta(self):
        return self.__conta
    '''setter de conta'''
    def set_conta(self,conta):
        self.__conta=conta
    '''getter de taxa'''
    @property
    def senha(self):
        return self.__senha
    '''setter de senha'''
    def set_senha(self,senha):
        self.__senha=senha