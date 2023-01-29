from cliente import Cliente
from pedido import Pedido
from manipuladorDePedidoMixin import ManipuladorPedidoMixin
from produto import Produto
from conta import Conta
from operador import Operador
from manipuladorEstoqueMixin import ManipuladorEstoqueMixin
list_pedidos=[]

def pular_linhas():
    print("\n" * 130)

def category_cliente():
    pular_linhas()
    
    print("============ DIGITE O NÚMERO DA OPERAÇÃO DESEJADA: ============\n1.criar pedido\n2.cancelar pedido\n3.pagar pedido\n4.sair=================================================================")
    option = int(input())
    manipularPedido= ManipuladorPedidoMixin()
    if option == 1:
        pular_linhas()
        login=input("Digite o seu login: \n")
        manipularPedido.criarPedido(login)
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
def category_operador():
    pular_linhas()
    print("============ DIGITE O NÚMERO DA OPERAÇÃO DESEJADA: ============\n1.criar pedido\n2cancelar pedido\n3.sair=================================================================")
    option = int(input())
    manipularPedido= ManipuladorPedidoMixin()

    if option == 1:
        pular_linhas()
        matricula=input("Digite a sua matricula: \n")
        manipularPedido.criarPedido(matricula)
        print(manipularPedido.get_pedidos)
    if option == 2:
        pular_linhas()
        codigo=input("Digite o codigo do pedido que deseja cancelar: \n")
        manipularPedido.cancelarPedido(codigo)
        print(manipularPedido.get_pedidos)
       
def category_gerente():
    pular_linhas()
    print("============ DIGITE O NÚMERO DA OPERAÇÃO DESEJADA: ============\n1.Adicionar no estoque\n2.remover no estoque\n3.atualizar no estoque\n4.sair=================================================================")
    option=input()
    manipularEstoque=ManipuladorEstoqueMixin()

    if option==1:
        pular_linhas()
        manipularEstoque.add_estoque()
        print(manipularEstoque.estoques)

    if option==2:
        pular_linhas()
        manipularEstoque.remover_estoque()
        print(manipularEstoque.estoques)
while True:
    print("============ DIGITE O NÚMERO DA CATEGORIA DESEJADA: ============\n1.Cliente\n2.Operador\n3.Gerente\n4.Sair\n=================================================================")
    option = int(input())
    if option == 1:
        category_cliente()
    if option == 2:
        category_operador()
    if option==3:
        category_gerente()
    if option >= 4 or  option < 1:
        break