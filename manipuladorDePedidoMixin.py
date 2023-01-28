from random import randint

'''Classe que controla pedidos'''
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
    def cancelarPedido(self,codigo):
        #pedido = next(x for x in self.pedidos if x.get_codigo() == codigo )
        for x in self.pedidos:
            if x.codigo==codigo:
                self.pedidos[x].status="Cancelado"
                self.__del__()
