'''Classe que simula um pedido'''
from cliente import Cliente
class Pedido:
    '''Construtor da classe'''
    def __init__(self,produto,valorProduto,quantidade,cliente,status="Aguardando pagamento",):
       self.__produto=produto
       self.__valorProduto=valorProduto
       self.__quantidade=quantidade
       self.__cliente=cliente
       self.status=status
    '''Getter de Produto'''
    @property
    def produto(self):
        return self.__produto
    '''setter de Produto'''
    @produto.setter
    def set_produto(self,produto):
        self.__produto=produto
    '''Getter de valor do produto'''
    @property
    def valorProduto(self):
        return self.__valorProduto
    '''setter de valor do produto'''
    @valorProduto.setter
    def set_valorProduto(self,valorProduto):
        self.__valorProduto=valorProduto
    '''Getter de quantidade'''
    @property
    def quantidade(self):
        return self.__quantidade
    '''setter de quantidade'''
    @quantidade.setter
    def set_quantidade(self,quantidade):
        self.__quantidade=quantidade
    '''Getter de cliente'''
    @property
    def cliente(self):
        return self.__cliente
    '''setter de cliente'''
    @cliente.setter
    def set_cliente(self,cliente):
        self.__cliente=cliente
    '''método que escreve as informações da classe'''
    def __str__(self):
        return ("Produto: {}\nvalor: {}\nquantidade: {}\n,cliente: {}\nstatus: {}".format(self.__produto,self.__valorProduto,self.__quantidade,self.__cliente,self.status))
    '''Método que sobrescreve o str e o passa para classe que utiliza a classe Pedido'''
    def __repr__(self):
         return ("Produto: {}\nvalor: {}\nquantidade: {}\n,cliente: {}\nstatus: {}".format(self.__produto,self.__valorProduto,self.__quantidade,self.__cliente,self.status))
