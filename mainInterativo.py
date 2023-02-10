from termcolor import colored

from cliente import Cliente
from conta import Conta
from manipuladorDePedidoMixin import ManipuladorPedidoMixin
from manipuladorEstoqueMixin import ManipuladorEstoqueMixin
from operador import Operador
from Pedido import Pedido
from produto import Produto
from Carrinho import Carrinho


def pular_linhas():
    print("\n" * 60)

def category_cliente():
    pular_linhas()
    
    print(colored('''============ DIGITE O NÚMERO DA OPERAÇÃO DESEJADA: ============\n
1) Criar pedido\n2) Cancelar pedido\n3) Pagar pedido\n4) Carrinho\n5) Sair\n
=================================================================''',"magenta"))
    option = int(input())
    manipularPedido= ManipuladorPedidoMixin()
    
    if option == 1:
        pular_linhas()
        manipularPedido.criarPedido()
        print(manipularPedido.get_pedidos)
        
    if option==2:
        pular_linhas()
        codigo=input("Digite o codigo do pedido que deseja cancelar: \n")
        manipularPedido.cancelarPedido(codigo)
        print(manipularPedido.get_pedidos)
       
    if option==3:
        pular_linhas()
        codigo=input("Digite o código do pedido: \n")
        manipularPedido.pagarPedido(codigo)
        print(manipularPedido.get_pedidos)
        
    if option == 4:
        pular_linhas()
        cotegory_carrinho()
        
    if option == 5:
        pular_linhas()
        print(colored("Obrigado por usar o sistema!","green"))
        exit()
        
def cotegory_carrinho():
    pular_linhas()
    print(colored('''============ DIGITE O NÚMERO DA OPERAÇÃO DESEJADA: ============\n
1) Consultar Carrinho\n2) Adicionar Item\n3) Remover Item\n4) Valor Total\n5) Sair\n
=================================================================''',"magenta"))
    option = int(input())
    monipularCarrinho = Carrinho()
    
    if option == 1:
        pular_linhas()
        monipularCarrinho.consultarCarrinho()
        
    if option == 2:
        pular_linhas()
        Item = input("Digite o nome do item: \n")
        monipularCarrinho.adicionarItem(Item)
        
    if option == 3:
        pular_linhas()
        Item = input("Digite o nome do item: \n")
        monipularCarrinho.removerItem(Item)
        
    if option == 4:
        pular_linhas()
        monipularCarrinho.valorTotal()
        
    if option == 5:
        pular_linhas()
        print(colored("Obrigado por usar o sistema!","green"))
        exit()
        
def category_operador():
    pular_linhas()
    print(colored('''============ DIGITE O NÚMERO DA OPERAÇÃO DESEJADA: ============\n
1) Criar pedido\n2) Cancelar pedido\n3) Sair\n
=================================================================''',"magenta"))
    option = int(input())
    manipularPedido= ManipuladorPedidoMixin()

    if option == 1:
        pular_linhas()
        manipularPedido.criarPedido()
        print(manipularPedido.get_pedidos)
        
    if option == 2:
        pular_linhas()
        codigo=input("Digite o codigo do pedido que deseja cancelar: \n")
        manipularPedido.cancelarPedido(codigo)
        print(manipularPedido.get_pedidos)
       
    if option == 3:
        pular_linhas()
        print(colored("Obrigado por usar o sistema!","green"))
        exit()
       
def category_gerente():
    pular_linhas()
    print(colored('''============ DIGITE O NÚMERO DA OPERAÇÃO DESEJADA: ============\n
1) Adicionar no estoque\n2) remover no estoque\n3) atualizar no estoque\n4) Sair\n
=================================================================''',"magenta"))
    option=int(input())
    manipularEstoque=ManipuladorEstoqueMixin()

    if option==1:
        pular_linhas()
        manipularEstoque.add_estoque()
        print(manipularEstoque.estoques)

    if option==2:
        pular_linhas()
        codigo = input('Digite o código do produto que deseja remover: ')
        manipularEstoque.remover_estoque(codigo)
        print(manipularEstoque.estoques)
        
    if option==3:
        pular_linhas()
        codigo = input('Digite o código do produto que deseja atualizar: ')
        manipularEstoque.atualizar_estoque(codigo)
        print(manipularEstoque.estoques)
        
while True:
    print(colored('''============ DIGITE O NÚMERO DA OPERAÇÃO DESEJADA: ============\n
1) Cliente\n2) Operador\n3) Gerente\n4) Sair\n
=================================================================''',"magenta"))
    option = int(input())
    if option == 1:
        category_cliente()
    if option == 2:
        category_operador()
    if option==3:
        category_gerente()
    if option >= 4 or  option < 1:
        print(colored("Obrigado por usar o sistema!","green"))
        break