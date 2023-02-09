from manipuladorDePedidoMixin import ManipuladorPedidoMixin
from Pedido import Pedido
from Pessoa import Pessoa

'''Classe que simula um cliente(usuário)'''

class Cliente(Pessoa, ManipuladorPedidoMixin):

    '''Construtor da classe'''
    def __init__(self, nome, telefone, cpf, conta):
        super().__init__(nome, telefone, cpf, conta)
        self.__pedidos=[]

    '''Método que escreve as informações da classe'''
    def __str__(self):
        return ("Nome: {}\nCPF: {}\nTelefone: {}\n".format(super().nome,super().cpf,super().telefone))