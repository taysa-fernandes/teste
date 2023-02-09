'''Classe que configura o pagamento do pedido'''
class Pagamento():

    '''Construtor da classe'''
    def __init__(self, valor, formaPagamento):
        self.__valor = valor
        self.__formaPagamento = formaPagamento

#### Getters e Setters
        
    '''getter de valor'''
    @property
    def valor(self):
        return self.__valor
    '''setter de valor'''
    @valor.setter
    def set_valor(self,valor):
        self.__valor=valor
    '''getter de forma de pagamento'''
    @property
    def formaPagamento(self):
        return self.__formaPagamento
    '''setter de forma de pagamento'''
    @formaPagamento.setter
    def set_formaPagamento(self,formaPagamento):
        self.__formaPagamento=formaPagamento
        
    def __str__(self) -> str:
        return f"Valor: {self.valor}, Forma de Pagamento: {self.formaPagamento}"