from random import randint

'''Classe que contra pedidos'''
class ManipuladorPedidoMixin():

    '''Construtor da classe'''
    def __init__(self):
        self.pedidos=[]


    '''Método que cria pedido'''
    def criarPedido(self,pedido):
        pedido.codigo=randint(0,10000)
        print(pedido.codigo)
        self.pedidos.append(pedido)
        print("Pedido criado!")


    '''Sobrescrevendo método que deleta instancia de objetos'''
    def __del__(self):
         print ("cancelado")


    '''Método que cancela o pedido'''
    def cancelarPedido(self,pedido):
        pedido.status="Cancelado"
        self.__del__()
