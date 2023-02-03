'''Classe que manipula o estoque da farmácia'''
from produto import Produto
from random import randint

class ManipuladorEstoqueMixin:
    def __init__(self):
        self.estoques = []

    def add_estoque(self):
        nome = input("Informe o nome do produto: ")
        codigo = randint(1, 100)
        produto = Produto(nome, codigo)
        self.estoques.append(produto)
        print(f"Produto adicionado ao estoque: {produto}")

    def remover_estoque(self, codigo):
        for i, estoque in enumerate(self.estoques):
            if estoque.codigo == codigo:
                del self.estoques[i]
                print(f"Produto com código {codigo} removido do estoque.")
                break
        else:
            print(f"Não foi encontrado um produto com código {codigo} no estoque.")

    def atualizar_estoque(self, codigo):
        for i, estoque in enumerate(self.estoques):
            if estoque.codigo == codigo:
                nome = input("Informe o novo nome do produto: ")
                self.estoques[i].nome == nome
                print(f"Produto com código {codigo} atualizado no estoque.")
                break
        else:
            print(f"Não foi encontrado um produto com código {codigo} no estoque.")


manipular = ManipuladorEstoqueMixin()
manipular.add_estoque()
print(manipular.estoques)

codigo_produto = int(input("Informe o código do produto que deseja remover: "))
manipular.remover_estoque(codigo_produto)
print(*manipular.estoques)

codigo_produto = int(input("Informe o código do produto que deseja atualizar: "))
manipular.atualizar_estoque(codigo_produto)
print(*manipular.estoques)
