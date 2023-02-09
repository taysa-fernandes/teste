<<<<<<< HEAD
from manipuladorDePedidoMixin import ManipuladorPedidoMixin
from Pessoa import Pessoa
=======
from Pessoa import Pessoa
from ManipuladorDePedidoMixin import ManipuladorPedidoMixin
>>>>>>> 041aa4ddedd50fc1e00fbae686bb622e92abca82

'''Classe que simula o operador de caixa de uma farmácia'''

class Operador(Pessoa, ManipuladorPedidoMixin):

    '''Construtor da classe'''
    def __init__(self, nome, telefone, cpf, conta, salario, situacao="Ativo"):
        super().__init__(nome, telefone, cpf, conta)
        self._salario = salario
        self.situacao = situacao

#### Getters e Setters

    @property
    def salario(self):
        return self.__salario
    '''setter de salário'''
    @salario.setter
    def set_salario(self,salario):
        self.__salario=salario
        
    def __str__(self):
        return ("Nome: {}\nCPF: {}\nTelefone: {}\n".format(super().nome,super().cpf,super().telefone))