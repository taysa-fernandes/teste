from produto import Produto
'''Classe que simula um pedido'''

class Pedido():

    '''Construtor da classe'''
    def __init__(self, produto, valorProduto, quantidade, codigo=None, status="Aguardando pagamento"):
       self.__produto = produto
       self.__valorProduto = valorProduto
       self.__quantidade = quantidade
       self.status = status
       self.__codigo = codigo

#### Getters e Setters

    '''Getter de Produto'''
    @property
    def produto(self):
        return self.__produto
    '''setter de Produto'''
    @produto.setter
    def set_produto(self,produto):
        self.__produto=produto
        
    '''Getter de codigo'''
    def get_codigo(self):
        return self.__codigo
    '''setter de codigo'''
    def set_codigo(self,codigo):
        self.__codigo=codigo
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

     
    '''método que escreve as informações da classe'''
    def __str__(self):
        return ("Produto: {}\nValor: {}\nQuantidade: {}\nStatus: {}".format(self.__produto, self.__valorProduto,self.__quantidade,self.status))

    '''Método que sobrescreve o str e o passa para classe que utiliza a classe Pedido'''
    def __repr__(self):
         return ("Produto: {}\nValor: {}\nQuantidade: {}\nStatus: {}".format(self.__produto, self.__valorProduto,self.__quantidade,self.status))
