'''Aula 23'''

class Acesso:
    #Atibutos
    saldoPublic = 0     # PUBLIC - acesso fora da classe
    _saldoProtected = 10     # PROTECTED - acesso fora da classe
    __saldoPrivate = 20     # Private - SEM acesso fora da classe

# GETTERS(GET - mostra atributo) and SETTERS(SET - altera o atributo)
    def get_private(self):
        return self.__saldoPrivate

    def set_private(self, valor):
        self.__saldoPrivate = valor

    def depositar(self):
        valor = float(input("Valor: "))
        self.__saldoPrivate += valor

# Programa Principal
ac = Acesso()
print(ac.get_private())
print(ac.get_private())