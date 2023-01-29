'''Classe que manipula o estoque da farmácia'''
from produto import Produto
from random import randint
class ManipuladorEstoqueMixin():

    '''Construtor da classe'''
    def __init__(self):
        self.estoques=[]

    codigoProduto=0
    '''Método que adiciona produtos no estoque'''
    def add_estoque(self):
        nome=input("Informe o nome do produto")
        produto=Produto(nome)
        self.estoques.append(produto)
        self.codigoProduto=12
        print(self.codigoProduto)
        print("Produto adicionado em estoque!")


    '''Método que remove o produto do estoque'''
    def remover_estoque(self,nome):
        for produto in self.estoques:
            if produto.nome==nome:
                pass
                print("Produto removido do estoque!")
            else:
                print("não encontrado")
        


    '''Método que atualiza informações de produto em estoque'''
    '''def atualizar_estoque(self,produtoAntigo,produtoNovo):
        for i in range(len(self.estoques)):
            if produtoAntigo==self.estoques[i]:
              pass
        print("Produto atualizado!")    '''
    