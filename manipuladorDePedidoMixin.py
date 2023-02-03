from random import randint
from Pedido import Pedido
from produto import Produto
'''Classe que controla pedidos'''
class ManipuladorPedidoMixin():

    '''Construtor da classe'''
    def __init__(self):
        self.__pedidos=[]

    '''Getter de pedidos'''
    @property
    def get_pedidos(self):
        return self.__pedidos
    '''setter de pedidos'''
    def set_pedidos(self,pedidos):
        self.__pedidos=pedidos

    '''Método que cria pedido'''
    def criarPedido(self):
        codigo=randint(0,10000)
        produto=input("Digite o produto: ")
        Produto(produto)
        valor=input("Digite o valor: ")
        quantidade=input("Digite a quantidade: ")
        pedido=Pedido(Produto,valor,quantidade,codigo)
        self.__pedidos.append(pedido)
        print(pedido.get_codigo())
        print("Pedido criado!")
        
        
    '''Método que paga um pedido'''
    def pagarPedido(self,codigo):
        for i in range(len(self.__pedidos)):
            if  self.get_pedidos()[i].codigo == codigo:
                self.__pedidos[i].status = "pago"
                print("pedido pago")
                break
            else:
                print("não encontrado")


    '''Método que cancela o pedido'''
    def cancelarPedido(self,codigo):
        for i in range(len(self.__pedidos)):
            if  self.get_pedidos()[i].codigo == codigo:
                self.__pedidos[i].status = "cancelado"
                del self.__pedidos[i]
                print("pedido cancelado")
                break
            else:
                print("não encontrado")


    def __str__(self) -> str:
        return f"{self.__pedidos}"