from random import randint
from termcolor import colored

from Pedido import Pedido
from produto import Produto
from termcolor import colored
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
        codigo=randint(0,20)
        produto=input("Digite o produto: ")
        Produto(produto)
        valor=input("Digite o valor: ")
        quantidade=input("Digite a quantidade: ")
        pedido=Pedido(produto, valor, quantidade, codigo)
        self.__pedidos.append(pedido)
        print("O Codigo do seu pedido: ", pedido.get_codigo())
        print(colored("Pedido criado!","green"))
        
    '''Método que paga um pedido'''
    def pagarPedido(self,codigo):
        for i in range(len(self.__pedidos)):
            if  self.get_pedidos()[i].codigo == codigo:
                self.__pedidos[i].status = "pago"
                print(colored("pedido pago","green"))
                break
            else:
                print(colored("não encontrado","red"))


    '''Método que cancela o pedido'''
    def cancelarPedido(self,codigo):
        for i in range(len(self.__pedidos)):
            if  self.get_pedidos()[i].codigo == codigo:
                self.__pedidos[i].status = "cancelado"
                del self.__pedidos[i]
                print(colored("pedido cancelado","green"))
                break
            else:
                print(colored("não encontrado","red"))


    def __str__(self) -> str:
        return f"{self.__pedidos}"