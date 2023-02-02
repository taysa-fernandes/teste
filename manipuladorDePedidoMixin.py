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
    def criarPedido(self,login):
        codigo=12
        produto=input("Digite o produto: ")
        Produto(produto)
        valor=input("Digite o valor: ")
        quantidade=input("Digite a quantidade: ")
        pedido=Pedido(Produto,valor,quantidade,login,codigo)
        self.__pedidos.append(pedido)
        print(self.__pedidos)
        print(pedido.get_codigo())
        return pedido
        
        print("Pedido criado!")
    '''Método que paga um pedido'''
    def cancelarPedido(self,codigo):
        print("entrou")
        print(self.__pedidos)
        for i in range(len(self.__pedidos)):
            if  self.__pedidos[i].codigo == codigo:
                self.__pedidos[i].status = "cancelado"
                print(self.__pedidos)
                del self.__pedidos[i]
                print("pedido cancelado")
                print(self.__pedidos)
                break
            else:
                print("não encontrado")


    '''Método que cancela o pedido'''
   def cancelarPedido(self,codigo):
        print("entrou")
        print(self.__pedidos)
        for i in range(len(self.__pedidos)):
            if  self.__pedidos[i].codigo == codigo:
                self.__pedidos[i].status = "cancelado"
                print(self.__pedidos)
                del self.__pedidos[i]
                print("pedido cancelado")
                print(self.__pedidos)
                break
            else:
                print("não encontrado")
            

            '''pedido = next(x for x in self.__pedidos if x.get_codigo() == codigo )
            pedido.set_status("cancelado")
            print(self.__pedidos)'''
    '''for x in self.__pedidos:
            if x.codigo==codigo:
                self.__pedidos[x].set_status("Cancelado")
                self.__del__()
                print(pedido)'''


    def __str__(self) -> str:
        return f"{self.__pedidos}"