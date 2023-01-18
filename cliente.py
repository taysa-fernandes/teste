from Pessoa import Pessoa
from manipuladorDePedidoMixin import ManipuladorPedidoMixin
'''Classe que simula um cliente(usuário)'''
class Cliente(Pessoa,ManipuladorPedidoMixin):
    '''Construtor da classe'''
    def __init__(self, nome, telefone, cpf, conta, senha,login):
        super().__init__(nome, telefone, cpf, conta, senha)
        self.__login=login
        self.pedidos=[]
    '''Getter de login'''
    @property
    def login(self):
        return self.__login
    '''setter de login'''
    @login.setter
    def set_login(self,login):
        self.__login=login
    '''Método que paga um pedido'''
    def pagarPedido(self,codigo):
        pass