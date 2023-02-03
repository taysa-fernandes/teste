from operador import Operador
from cliente import Cliente
from Pessoa import Pessoa
from manipuladorEstoqueMixin import ManipuladorEstoqueMixin
from random import randint

'''Classe que simula um gerente de uma farmácia'''

class Gerente(Pessoa,ManipuladorEstoqueMixin):

    '''Construtor da classe'''
    def __init__(self, nome, telefone, cpf, conta, senha):
        super().__init__(nome, telefone, cpf, conta, senha)
        self.pedidos=[]
        self.clientes=[]
        self.operadores=[]

    '''Método que cria os operadores'''
    '''def criarOperador(self,operador):
        #gera um código aleatório para o operador
        codigoOperador=randint(0,10000)
        print(codigoOperador) 
        
        self.operadores.append(operador)
        print("Operador criado!")'''


    '''Método que apaga um operador'''
    ''' def removerOperador(self,operador):
        operador.situacao="inativo"
        print("Operador removido!")'''


    '''Método que cria um cliente(usuário)'''
    '''def criarCliente(self,cliente):
        #gera um código aleatório para o cliente
        codigoCliente=randint(0,10000) 
        print(codigoCliente)
        self.clientes.append(cliente)
        print("Cliente criado!")'''
    
    '''Método que escreve as informações da classe'''
    def __str__(self) -> str:
        return f"Dados do Gerente: \nNome: {self.nome} Telefone: {self.telefone} CPF: {self.cpf} Conta: {self.conta}"

