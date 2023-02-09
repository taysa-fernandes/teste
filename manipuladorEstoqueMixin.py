'''Classe que manipula o estoque da farmácia'''
<<<<<<< HEAD
=======
from Produto import Produto
>>>>>>> 041aa4ddedd50fc1e00fbae686bb622e92abca82
from random import randint

from termcolor import colored

from produto import Produto


class ManipuladorEstoqueMixin:
    def __init__(self):
        self.estoques = []

    def add_estoque(self):
        nome = input("Informe o nome do produto: ")
        codigo = randint(1, 100)
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

    def atualizar_estoque(self, codigo):
        for i, estoque in enumerate(self.estoques):
            if estoque.codigo == codigo:
                nome = input("Informe o novo nome do produto: ")
                self.estoques[i].nome == nome
                print(colored(f"Produto com código {codigo} atualizado no estoque.","green"))
                break
        else:
            print(colored(f"Não foi encontrado um produto com código {codigo} no estoque.","red"))
