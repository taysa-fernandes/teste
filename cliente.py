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
        pedido= next(x for x in self.pedido if x.get_codigo() == codigo )
        pedido.set_status("Pago")
        print("Reserva paga")
    '''Método que escreve as informações da classe'''
    def __str__(self):
        return ("nome: {}\ncpf: {}\ntelefone: {}\n".format(super().nome,super().cpf,super().telefone))