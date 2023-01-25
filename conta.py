'''Classe que representa a conta ao qual irá ser realizado os pagamentos'''

class Conta():

    '''Construtor da classe'''
    def __init__(self,nome,banco,numeroConta,saldo,limite,tipo,status="ativo"):
        self.__nome=nome
        self.__banco=banco
        self.__numeroConta=numeroConta
        self.__saldo=saldo
        self.__limite=limite
        self.tipo=tipo
        self.status=status
        self.transacoes=[]

#### Getters e Setters

    '''Getter de nome'''
    @property
    def nome(self):
        return self.__nome
    '''setter de nome'''
    @nome.setter
    def set_nome(self,nome):
        self.__nome=nome
    '''Getter de banco'''
    @property
    def banco(self):
        return self.__banco
    '''setter de banco'''
    @banco.setter
    def set_banco(self,banco):
        self.__banco=banco
    '''Getter do número  da conta'''
    @property
    def numeroConta(self):
        return self.__numeroConta
    '''setter do número da conta'''
    @numeroConta.setter
    def set_numeroConta(self,numeroConta):
        self.__numeroConta=numeroConta
    '''Getter de saldo'''
    @property
    def saldo(self):
        return self.__saldo
    '''setter de saldo'''
    @saldo.setter
    def set_saldo(self,saldo):
        self.__saldo=saldo
    '''Getter de limite'''
    @property
    def limite(self):
        return self.__limite
    '''setter de limite'''
    @limite.setter
    def set_limite(self,limite):
        self.__limite=limite


    '''Método que mostra o histórico de movimentações que foi realizada na conta e seu saldo final'''
    def emitirExtrato(self):
        if self.status=="ativo":
            self.transacoes.append(f"tirou extrado - saldo de {self.__saldo}")
        print("-"*12,"Histórico","-"*12)
        print(f"numero: {self.__numeroConta}\n saldo: {self.__saldo}")
        for transacao in self.transacoes:
            print(transacao)


    '''Método que realiza um déposito de um valor em uma conta'''
    def deposita(self, valor):
        self.__saldo += valor
        self.transacoes.append("depósito de {}".format(valor))


    '''Método que realiza um saque de um valor em uma conta'''
    def saca(self, valor):
       if (self.saldo < valor):
        return False
       else:
            self.__saldo -= valor
            self.transacoes.append("saque de {}".format(valor))


    '''Método que realiza uma transferência de um valor de uma conta para outra'''
    def transferir(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.transacoes.remove("saque de {}".format(valor))
            self.transacoes.append("transferência de {} para {}".format(valor,destino.nome))
            return True


    '''Método que desativa a conta'''
    def encerrarConta(self):
        self.status="inativo"
        self.transacoes.append("Conta desativada")
        self.transacoes.remove(f"Tirou extrado - saldo de {self.__saldo}")