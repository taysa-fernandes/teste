from Pessoa import Pessoa
from ManipuladorDePedidoMixin import ManipuladorPedidoMixin

'''Classe que simula o operador de caixa de uma farmácia'''

class Operador(Pessoa, ManipuladorPedidoMixin):

    '''Construtor da classe'''
    def __init__(self, nome, telefone, cpf, conta, senha, matricula, salario, situacao="Ativo"):
        super().__init__(nome, telefone, cpf, conta, senha)
        self.__matricula=matricula
        self._salario=salario
        self.situacao=situacao

#### Getters e Setters

    '''Getter de matrícula'''
    @property
    def matricula(self):
        return self.__matricula
    '''setter de matricula'''
    @matricula.setter
    def set_matricula(self,matricula):
        self.__matricula=matricula
    '''Getter de salario'''
    @property
    def salario(self):
        return self.__salario
    '''setter de salário'''
    @salario.setter
    def set_salario(self,salario):
        self.__salario=salario
        
    def __str__(self) -> str:
        return f"Matrícula: {self.matricula} Salário: {self.salario} Situação: {self.situacao}"