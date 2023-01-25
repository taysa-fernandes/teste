from operador import Operador
from cliente import Cliente
from Pessoa import Pessoa
from manipuladorDePedidoMixin import ManipuladorPedidoMixin
from random import randint

'''Classe que simula um gerente de uma farmácia'''

class Gerente(Pessoa,ManipuladorPedidoMixin):

    '''Construtor da classe'''
    def __init__(self, nome, telefone, cpf, conta, senha):
        super().__init__(nome, telefone, cpf, conta, senha)
        self.pedidos=[]
        self.clientes=[]
        self.operadores=[]


    '''Método que cria os operadores'''
    def criarOperador(self,operador):
        codigoOperador=randint(0,10000)
        print(codigoOperador)
        self.operadores.append(operador)
        print("Operador criado!")


    '''Sobrescrevendo método que deleta instancia de objetos'''
    def __del__(self):
         print ("Removido")


    '''Método que apaga um operador'''
    def removerOperador(self,operador):
        operador.situacao="inativo"
        self.__del__()
        print("Operador removido!")


    '''Método que cria um cliente(usuário)'''
    def criarCliente(self,cliente):
        codigoCliente=randint(0,10000)
        print(codigoCliente)
        self.clientes.append(cliente)
        print("Cliente criado!")

        
    '''Método que apaga um cliente(usuário)'''
    def removerCliente(self,cliente):
        cliente.situacao="inativo"
        self.__del__()
        print("Cliente removido!")
