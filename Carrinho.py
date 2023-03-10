from Pedido import Pedido
from produto import Produto

class Carrinho:
    def __init__(self, pedidos=[], formaPagamento="Cartão"):
        self.__pedidos = pedidos
        self.__formaPagamento = formaPagamento
    
    def consultarCarrinho(self):
        print(40*"=", "Carrinho", 40*"=")
        print("Itens Adicionados:\n")
        if (len(self.__pedidos) > 0):
            for i in range(len(self.__pedidos)):
                print(int(
                    self.__pedidos[i].produto.nome,
                    "--- UND R$", self.__pedidos[i].valorProduto,
                    "--- QTD", self.__pedidos[i].quantidade,
                    "--- TOTAL: R$", self.__pedidos[i].valorProduto * self.__pedidos[i].quantidade))
            print("\n")
        else:
            print("O carrinho está vazio!")
        print("\n")

    def adicionarItem(self, pedido):
        self.__pedidos.append(pedido)

    def removerItem(self, pedido):
        for i in range(len(self.__pedidos)):
            if (self.__pedidos[i] == pedido):
                self.__pedidos.pop(i)
                break

    def valorTotal(self):
        aux = 0
        for i in range(len(self.__pedidos)):
            aux += self.__pedidos.valorProduto
        return f'O valor total é: R$ {aux}'
    
    

