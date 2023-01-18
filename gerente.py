'''Classe que simula um gerente de uma farmácia'''
from operador import Operador
from cliente import Cliente
from Pessoa import Pessoa
from manipuladorDePedidoMixin import ManipuladorPedidoMixin
class Gerente(Pessoa,ManipuladorPedidoMixin):
    '''Construtor da classe'''
    def __init__(self, nome, telefone, cpf, conta, senha):
        super().__init__(nome, telefone, cpf, conta, senha)
        self.pedidos=[]
        self.clientes=[]
    '''Método que cria os operadores'''
    def criarOperador(self,matricula,salario):
        Operador(matricula,salario)
        self.operadores.append(Operador)
        print("Operador criado!")
    '''Método que apaga um operador'''
    def removerOperador(self,operador):
        self.operadores.remove(operador)
        print("Operador removido!")
    '''Método que cria um cliente(usuário)'''
    def criarCliente(self,login):
        Cliente(login)
        self.clientes.append(Cliente)
        print("Cliente criado!")
    '''Método que apaga um cliente(usuário)'''
    def removerCliente(self,cliente):
        self.clientes.remove(cliente)
        print("Cliente removido!")
