from Pedido import Pedido
from random import randint
'''Classe que contra pedidos'''
class ManipuladorPedidoMixin:
    '''Construtor da classe'''
    def __init__(self):
        self.pedidos=[]
    '''Método que cria pedido'''
    def criarPedido(self,pedido):
        pedido.codigo=randint(0,10000)
        print("Pedido criado!")
    '''Método que cancela o pedido'''
    def cancelarPedido(self,codigo):
        pedido= next(x for x in self.__pedidos if x.get_codigo() == code )
        pedido.set_status("Cancelado")
        print("pedido cancelada")