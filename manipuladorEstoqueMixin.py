'''Classe que manipula o estoque da farmácia'''
from produto import Produto
from random import randint

from termcolor import colored
from Validade import Validade
from produto import Produto


class ManipuladorEstoqueMixin(Validade):
    def __init__(self):
        self.estoques = []

    def add_estoque(self):
        nome = input("Informe o nome do produto: ")
        codigo = randint(1,30)
        produto = Produto(nome, codigo)
        self.estoques.append(produto)
        print(colored(f"Produto adicionado ao estoque: {produto}","green"))

    def remover_estoque(self, codigo):
        for i, estoque in enumerate(self.estoques):
            if estoque.codigo == codigo:
                del self.estoques[i]
                print(colored(f"Produto com código {codigo} removido do estoque.","green"))
                break
        else:
            print(colored(f"Não foi encontrado um produto com código {codigo} no estoque.","red"))

    def verificarValidade():
        pass

    def atualizar_estoque(self, codigo):
        for i, estoque in enumerate(self.estoques):
            if estoque.codigo == codigo:
                nome = input("Informe o novo nome do produto: ")
                self.estoques[i].nome = nome
                print(colored(f"Produto com código {codigo} atualizado no estoque.","green"))
                break
        else:
            print(colored(f"Não foi encontrado um produto com código {codigo} no estoque.","red"))
            
    def __str__(self):
        return f"Estoque: {self.estoques}"
