'''Classe que manipula o estoque da farmácia'''
class ManipuladorEstoqueMixin:
    '''Construtor da classe'''
    def __init__(self):
        self.estoques=[]
    '''Método que adiciona produtos no estoque'''
    def add_estoque(self,produto):
        self.estoques.append(produto)
        print("Produto adicionado em estoque!")
    '''Método que remove o produto do estoque'''
    def remover_estoque(self,produto):
        self.estoques.remove(produto)
        print("Produto removido do estoque!")
    '''método que atualiza informações de produto em estoque'''
    def atualizar_estoque(self,produtoAntigo,produtoNovo):
        for i in range(len(self.estoques)):
            if produtoAntigo==self.estoques[i]:
                self.estoques.remove(produtoAntigo)
                self.estoques.append(produtoNovo)
        print("Produto atualizado!")    
    