'''Classe que simula um gerente de uma farmácia'''
from operador import Operador
from cliente import Cliente
from Pessoa import Pessoa
from manipuladorDePedidoMixin import ManipuladorPedidoMixin
from random import randint
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
    '''Método que apaga um operador'''
    def removerOperador(self,operador):
        self.operadores.pop(operador)
        print("Operador removido!")
    '''Método que cria um cliente(usuário)'''
    def criarCliente(self,cliente):
        codigoCliente=randint(0,10000)
        print(codigoCliente)
        self.clientes.append(cliente)
        print("Cliente criado!")
    '''Método que apaga um cliente(usuário)'''
    def removerCliente(self,codigo):
        self.clientes.pop(codigo)
        print("Cliente removido!")
