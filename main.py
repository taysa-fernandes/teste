from conta import Conta
from manipuladorDePedidoMixin import ManipuladorPedidoMixin
from cliente import Cliente
from gerente import Gerente
from operador import Operador
from manipuladorEstoqueMixin import ManipuladorEstoqueMixin
conta1 = Conta("suzana","inter",123859,1200,500,"poupanca")
conta2 = Conta("lorena","santander",679056,200,900,"poupanca")
cliente=Cliente("Hermeson","(84)99834-9742","123.853.090-09",conta1,"67fbp","hermersonLOPES")
operador=Operador("jair","(12)3485-7583","467-759-388-90",conta2,"bfuif93",12345,1230.00)

manipularPedido= ManipuladorPedidoMixin()
manipularPedido.criarPedido(cliente.login)
manipularPedido.cancelarPedido(12)#muda o status mas n exlcui o objeto
#manipularPedido.pagarPedido(12)'''
'''gerente=Gerente("Lucas","(56)95783-8964","123-675-890-90",conta2,"esprin5")
gerente.criarOperador(operador)
print(gerente.operadores)
gerente.removerOperador(operador)
print(operador.situacao)
print(gerente.operadores)'''
'''gerente.criarCliente(cliente)
print(gerente.clientes)
gerente.removerCliente(cliente)
print(gerente.clientes)'''
'''manipularEstoque=ManipuladorEstoqueMixin()
manipularEstoque.add_estoque()
print(manipularEstoque.estoques)
manipularEstoque.remover_estoque("lápis")
print(manipularEstoque.estoques)'''
'''manipularEstoque.atualizar_estoque(produto,produto2)
print(manipularEstoque.estoques)'''
