from cliente import Cliente
from Pedido import Pedido
from manipuladorDePedidoMixin import ManipuladorPedidoMixin
from produto import Produto
from conta import Conta

def pular_linhas():
    print("\n" * 130)

def category_cliente():
    pular_linhas()
    '''login=input("Digite o seu login: \n")
    nome=input("Digite seu nome: \n")
    telefone=input("Digite seu número: \n")
    cpf=input("Digite seu cpf: \n")
    banco=input("Banco que vai utilizar: \n")
    numeroConta=input("Número de sua conta: \n")
    saldo=input("Saldo disponivel na conta \n")
    limite=input("Limite de conta: \n")
    tipo=input("Tipo da conta: corrente ou  poupança: \n")
    co=Conta(nome,banco,numeroConta,saldo,limite,tipo)
    senha=input("Escolha uma senha \n")'''
    c=Cliente("luas","2389","4905","47805-859","ruio","dhep")
    print("============ DIGITE O NÚMERO DA OPERAÇÃO DESEJADA: ============\n1.Criar pedido\n2.cancelar pedido\n3.pagar pedido\n4.sair\n=================================================================")
    option = int(input())
    manipularPedido= ManipuladorPedidoMixin()
    if option == 1:
        pular_linhas()
        nome=input("Digite o nome do produto: \n")
        produto=Produto(nome)
        valorProduto = input("Digite o valor do produto: \n")
        quantidade = input("Dgite a quantidade do produto: \n")
        pedido=Pedido(produto,valorProduto,quantidade,"luas")
        manipularPedido.criarPedido(pedido)
        print(manipularPedido.pedidos)
        

    if option == 2:
        pular_linhas()
        pedido=input("Digite o pedido que deseja cancelar: \n")
        manipularPedido.cancelarPedido(pedido)
        print(manipularPedido.pedidos)

    if option==3:
        pular_linhas()
        codigo=input("Digite o código do pedido: \n")
        c.pagarPedido(codigo)
        print(manipularPedido.pedidos)

while True:
    print("============ DIGITE O NÚMERO DA CATEGORIA DESEJADA: ============\n1.Cliente\n2.Operador\n3.Gerente\n4.Sair\n=================================================================")
    option = int(input())
    if option == 1:
        category_cliente()
    if option == 2:
        pass
    if option >= 4 or  option < 1:
        break