from Pessoa import Pessoa
from manipuladorDePedidoMixin import ManipuladorPedidoMixin
from Pedido import Pedido


'''Classe que simula um cliente(usuário)'''

class Cliente(Pessoa, ManipuladorPedidoMixin):

    '''Construtor da classe'''
    def __init__(self, nome, telefone, cpf, conta, senha):
        super().__init__(nome, telefone, cpf, conta, senha)


    '''Getter de login'''
    @property
    def login(self):
        return self.__login
    '''setter de login'''
    @login.setter
    def set_login(self,login):
        self.__login=login



    '''Método que escreve as informações da classe'''
    def __str__(self):
        return ("Nome: {}\nCPF: {}\nTelefone: {}\n".format(super().nome,super().cpf,super().telefone))