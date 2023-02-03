from termcolor import colored
class Estoque:
    def __init__(self, produtos=[]):
        self.__produtos = produtos

    #Getters and Setters
    def getProdutos(self):
        return self.__produtos
    def setProdutos(self, value):
        self.__produtos = value

    def add_Produto(self, produto):
        self.__produtos.append(produto)

    def gerarRelatorioDeEstoque(self):
        print(colored("----------------Relátorio de Estoque Atual ----------------------","blue"))
        for i in range(len(self.getProdutos())):
            print(colored("Produto:", self.getProdutos()[i].get("nome"), "\nQuantidade Em Estoque:", self.getProdutos()[i].get("quantidade"),"blue"))
            print(colored("-"*65,"blue"))

    def __str__(self) -> str:
        return f"Produtos: {self.getProdutos()}"


# produto = {
#     "nome": "produto1",
#     "quantidade": 100,
# }
# produto2 = {
#     "nome": "produto2",
#     "quantidade": 130,
# }

# e = Estoque()
# e.appendProduto(produto)
# e.appendProduto(produto2)

# for i in range(len(e.getProdutos())):
#     print(e.getProdutos()[i])

# e.gerarRelatorioDeEstoque()


