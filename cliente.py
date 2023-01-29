from Pessoa import Pessoa
from manipuladorDePedidoMixin import ManipuladorPedidoMixin
from pedido import Pedido


'''Classe que simula um cliente(usuário)'''

class Cliente(Pessoa, ManipuladorPedidoMixin):

    '''Construtor da classe'''
    def __init__(self, nome, telefone, cpf, conta, senha,login):
        super().__init__(nome, telefone, cpf, conta, senha)
        manipular=ManipuladorPedidoMixin()
        self.__login=login


    '''Getter de login'''
    @property
    def login(self):
        return self.__login
    '''setter de login'''
    @login.setter
    def set_login(self,login):
        self.__login=login


    '''Método que paga um pedido'''
    '''def pagarPedido(self,codigo):
        for pedido in self.__pedidos:
            print("entrou")
            if  pedido.get_codigo()==codigo:
                pedido.status="pago"
                print(self.__pedidos)
                print(pedido.get_codigo())
                print("pedido pago")
            else:
                print("não encontrado")'''
    '''pedido= next(x for x in self.pedidos if x.get_codigo() == pedido.codigo )'''
    '''for x in self.manipular.get_pedidos:
            if x.codigo==codigo:
                self.manipular.set_pedidos()
                print("Pedido pago")'''


    '''Método que escreve as informações da classe'''
    def __str__(self):
        return ("Nome: {}\nCPF: {}\nTelefone: {}\n".format(super().nome,super().cpf,super().telefone))