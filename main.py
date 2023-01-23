from conta import Conta
from manipuladorDePedidoMixin import ManipuladorPedidoMixin
from Pedido import Pedido
from cliente import Cliente
from gerente import Gerente
from operador import Operador
from manipuladorEstoqueMixin import ManipuladorEstoqueMixin
from produto import Produto
conta1 = Conta("suzana","inter",123859,1200,500,"poupanca")
conta2 = Conta("lorena","santander",679056,200,900,"poupanca")
cliente=Cliente("Hermeson","(84)99834-9742","123.853.090-09",conta1,"67fbp","hermersonLOPES")
operador=Operador("jair","(12)3485-7583","467-759-388-90",conta2,"bfuif93",12345,1230.00)
produto=Produto(12,"faca")
produto2=Produto(4,"lápis")

'''pedido=Pedido("lápis",12.00,2,cliente)
manipularPedido= ManipuladorPedidoMixin()
manipularPedido.criarPedido(pedido)
print(manipularPedido.pedidos)
manipularPedido.cancelarPedido(pedido)
print(manipularPedido.pedidos)'''
gerente=Gerente("Lucas","(56)95783-8964","123-675-890-90",conta2,"esprin5")
gerente.criarOperador(operador)
print(gerente.operadores)
gerente.removerOperador(operador)
print(operador.situacao)
print(gerente.operadores)
'''gerente.criarCliente(cliente)
print(gerente.clientes)
gerente.removerCliente(cliente)
print(gerente.clientes)'''
'''manipularEstoque=ManipuladorEstoqueMixin()
manipularEstoque.add_estoque(produto)
print(manipularEstoque.estoques)
manipularEstoque.remover_estoque(produto)
print(manipularEstoque.estoques)
manipularEstoque.atualizar_estoque(produto,produto2)
print(manipularEstoque.estoques)'''
