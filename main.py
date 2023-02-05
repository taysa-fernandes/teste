import uuid

from Cliente import Cliente
from Conta import Conta
from Gerente import Gerente
from ManipuladorDePedidoMixin import ManipuladorPedidoMixin
from ManipuladorEstoqueMixin import ManipuladorEstoqueMixin
from Operador import Operador

'''Gerar Automaticamente uma matricula para o cliente'''
NumbRand = uuid.uuid1()

'''Instanciando objetos das classe Conta, Cliente, Operador e Gerente'''
conta1 = Conta("suzana", "inter", 123859, 1200, 500, "poupanca")
conta2 = Conta("lorena", "santander", 679056, 200, 900, "poupanca")
cliente=Cliente("Hermeson", "(84)99834-9742", "123.853.090-09", conta1, NumbRand, "hermersonLOPES")
operador=Operador("jair", "(12)3485-7583", "467-759-388-90", conta2, NumbRand, 12345, 1230.00)
gerente=Gerente("Lucas", "(56)95783-8964", "123-675-890-90", conta2, "esprin5")


'''gerente.criarOperador(operador)
print(gerente.operadores, "\n")

gerente.removerOperador(operador)
print(operador.situacao, "\n")
print(gerente.operadores, "\n")'''

# gerente.criarCliente(cliente)
# print(gerente.clientes, "\n")
manipularPedido= ManipuladorPedidoMixin()
manipularPedido.criarPedido(cliente.login)
manipularPedido.cancelarPedido(12)#muda o status mas n exlcui o objeto
# manipularPedido.pagarPedido(12)'''
'''manipularEstoque=ManipuladorEstoqueMixin()
manipularEstoque.add_estoque()
print(manipularEstoque.estoques)
manipularEstoque.remover_estoque("lápis")
print(manipularEstoque.estoques)'''
'''manipularEstoque.atualizar_estoque(produto,produto2)
print(manipularEstoque.estoques)'''
