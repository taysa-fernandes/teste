
'''Classe que simula o operador de caixa de uma farmácia'''
from Pessoa import Pessoa
from manipuladorDePedidoMixin import ManipuladorPedidoMixin
class Operador(Pessoa,ManipuladorPedidoMixin):
    '''Construtor da classe'''
    def __init__(self, nome, telefone, cpf, conta, senha,matricula,salario):
        super().__init__(nome, telefone, cpf, conta, senha)
        self.__matricula=matricula
        self._salario=salario
    @property
    def matricula(self):
        return self.__matricula
    '''setter de matricula'''
    @matricula.setter
    def set_matricula(self,matricula):
        self.__matricula=matricula
    @property
    def salario(self):
        return self.__salario
    '''setter de salário'''
    @salario.setter
    def set_salario(self,salario):
        self.__salario=salario