'''
Atividade de Classes - 14.06.21
Base de dados: Encarte do Super Mercado guanabara
'''

#Aplicativo de Gerenciamento Manager de um mercadinho

class Mercadinho:
    # Atributo
    _nome = ''
    _caixa = 1000
    _estoque = 0
    _preco = 0

    # Método

    def __init__(self):
        print('_+_+'*20)
        print("Bem Vindo ao Mercadinho",self._nome,"\nO que deseja fazer?\n1 - Alterar nome do Mercado\n2 - Verificar caixa\n3 - Comprar Produtos\n4 - Verificar Estoque\n5 - Vender Produto")
        escolha = int(input("Escolha (1/2/3/4/5): "))
        if escolha == 1:
            self.set_nome()
        if escolha == 2:
            self.get_caixa()
        if escolha == 3:
            self.comprar_produto()
        if escolha == 4:
            self.get_estoque()
        if escolha == 5:
            self.vender_produto()

    def set_nome(self):
        print('_+_+' * 20)
        self.novo_nome = str(input("Digite o novo nome: "))
        self._nome = self.novo_nome
        print("Você alterou o nome com sucesso.")
        self.__init__()

    def get_caixa(self):
        print('_+_+' * 20)
        print("Você possui: R$",self._caixa)
        self.__init__()

    def comprar_produto(self):
        print('_+_+' * 20)
        print("Produto disponível: Pó de café Pelé, por: R$6,79 uni.")
        qtd = int(input("Quantos deseja comprar: "))
        self._estoque += qtd
        custo = qtd * 6.79
        self._caixa -= custo
        print('_+_+' * 20)
        print("Compra efetuada com sucesso!")
        print('_+_+' * 20)
        self._preco = int(input("Por quanto deseja vender? ").replace(",","."))
        self.__init__()

    def get_estoque(self):
        print('_+_+' * 20)
        print("Você possui:",self._estoque,"produtos em estoque")
        self.__init__()

    def vender_produto(self):
        print('_+_+' * 20)
        qtd = int(input("Quantos você vendeu? "))
        self._estoque -= qtd
        lucro = qtd*self._preco
        self._preco += lucro
        print('_+_+' * 20)
        print("Com a venda de",qtd,"você lucrou",lucro)

# Programa Principal
app = Mercadinho()



