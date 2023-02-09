<<<<<<< HEAD
=======
from Operador import Operador
from Cliente import Cliente
from Pessoa import Pessoa
from ManipuladorEstoqueMixin import ManipuladorEstoqueMixin
>>>>>>> 041aa4ddedd50fc1e00fbae686bb622e92abca82
from random import randint

from cliente import Cliente
from manipuladorEstoqueMixin import ManipuladorEstoqueMixin
from operador import Operador
from Pessoa import Pessoa

'''Classe que simula um gerente de uma farmácia'''

class Gerente(Pessoa,ManipuladorEstoqueMixin):

    '''Construtor da classe'''
    def __init__(self, nome, telefone, cpf, conta):
        super().__init__(nome, telefone, cpf, conta)
        self.pedidos=[]
        self.clientes=[]
        self.operadores=[]

    '''Método que cria os operadores'''
    def criarOperador(self,operador):
        #gera um código aleatório para o operador
        codigoOperador=randint(0,10000)
        print(codigoOperador) 
        self.operadores.append(operador)
        print("Operador criado!")


    '''Método que apaga um operador'''
    def removerOperador(self,operador):
        operador.situacao="inativo"
        print("Operador removido!")


    '''Método que cria um cliente(usuário)'''
    def criarCliente(self,cliente):
        #gera um código aleatório para o cliente
        codigoCliente=randint(0,10000) 
        print(codigoCliente)
        self.clientes.append(cliente)
        print("Cliente criado!")
    
    '''Método que escreve as informações da classe'''
    def __str__(self) -> str:
        return f"Dados do Gerente: \nNome: {self.nome} Telefone: {self.telefone} CPF: {self.cpf} Conta: {self.conta}"


gerente = Gerente("João","(11) 99999-9999","123.456.789-10","1234")

gerente.criarCliente(Cliente("João","(11) 99999-9999","123.456.789-10","1234"))
gerente.criarOperador(Operador("João","(11) 99999-9999","123.456.789-10","1234",1000))
gerente.removerOperador(Operador("João","(11) 99999-9999","123.456.789-10","1234",1000))

