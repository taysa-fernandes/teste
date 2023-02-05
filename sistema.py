class Sistema():
    # Construtor
    def __init__(self):
        self.__clientes = []
        self.__operadores = []
        self.__gerentes = []
    
    # Registros
    def registrarCliente(self, pessoa):
        self.__clientes.append(pessoa)

    def registrarOperador(self, pessoa):
        self.__operadores.append(pessoa)

    def registrarGerente(self, pessoa):
        self.__gerentes.append(pessoa)

    # Remoções
    def removerCliente(self, cliente):
        for i in range(len(self.__clientes)):
            if (self.__clientes[i] == cliente):
                self.__clientes.pop(i)
                break
    
    def removerOperador(self, operador):
        for i in range(len(self.__operadores)):
            if (self.__operadores[i] == operador):
                self.__operadores.pop(i)
                break

    def removerGerente(self, gerente):
        for i in range(len(self.__gerentes)):
            if (self.__gerentes[i] == gerente):
                self.__gerentes.pop(i)
                break
        
    # Getters e Setters
    def get_clientes(self):
        return self.__clientes
    def set_clientes(self, value):
        self.__clientes = value
    
    def get_operadores(self):
        return self.__operadores
    def set_operadores(self, value):
        self.__operadores = value
    
    def get_gerentes(self):
        return self.__gerentes
    def set_gerentes(self, value):
        self.__gerentes = value

t = Sistema()

t.registrarCliente("teste")
print(map(t.get_clientes()))

t.removerCliente("teste")