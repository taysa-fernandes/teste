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
        nome=input("Informe o nome do produto: ")
        produto=Produto(nome)
        self.estoques.append(produto)
        produto.codigo=19
        print(produto.codigo)
        print("Produto adicionado em estoque!")


    '''Método que remove o produto do estoque'''
    def remover_estoque(self,codigo):
        for j in range(len(self.estoques)):
            if self.estoques[j].codigo==codigo:
                del self.estoques[j]
                print("Produto removido do estoque!")
            else:
                print("não encontrado")
        


    '''Método que atualiza informações de produto em estoque'''
    def atualizar_estoque(self,codigo):
         for j in range(len(self.estoques)):
                 self.add_estoque()
                 self.remover_estoque(codigo)
                 print("Produto atualizado!")  
            
    
    def __str__(self) -> str:
        return f"Estoques: {self.estoques}"

manipular=ManipuladorEstoqueMixin()
manipular.add_estoque()
print(manipular.estoques)
manipular.remover_estoque(19)
print(manipular.estoques)
#manipular.atualizar_estoque(19)