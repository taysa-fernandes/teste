from conta import Conta

conta1 = Conta("suzana","inter",123859,1200,500,"poupanca")
conta2 = Conta("lorena","santander",679056,200,900,"poupanca")
conta1.deposita(100.0)
conta1.saca(50.0)
conta1.transferir(conta2, 200.0)
conta1.extrato()
conta2.extrato()
conta1.encerrarConta()
conta1.extrato()
print(conta1.status)
