'''
Atividade de Classes - 14.06.21
Base de Dados: https://www.magazineluiza.com.br/caixas-de-som/audio/s/ea/cxsm/
'''

class Product:
    #Atributos:
    nome = 'Caixa de Som Extreme Bass Boom'
    preco = 945.05
    estoque = 10
    valor_estoque = 870.90
    custo_estoque = 0
    estoque_atual = 0
    caixa = 0
    caixa_atual = 0

    def __init__(self):
        print("_-_" * 10)
        print("Menu de Ações:\n1 - Vender produto\n2 - Ampliar Estoque")
        escolha = int(input("Escolha: "))
        if escolha == 1:
            self.quantidade = int(input("Quantos produtos foram vendidos: "))
            self.vender_produto(self.quantidade)

        if escolha == 2:
            self.qtda_produto = int(input("Qauntos produtos deseja comprar: "))
            self.ampliar_estoque(self.qtda_produto)

    #Métodos

    def vender_produto(self, quantidade):
        self.estoque_atual = self.estoque - self.quantidade
        self.caixa_atual = self.quantidade * self.preco
        print("_-_" * 20)
        print("Você vendeu:",self.quantidade,"\nEstoque atual:",self.estoque_atual,"\nCaixa atual: {:.2f}".format(self.caixa_atual))
        self.__init__()

    def ampliar_estoque(self, qtda_produto):
        self.custo_estoque = self.valor_estoque * self.qtda_produto
        print("Seu estoque atual é de:",self.estoque_atual,"\nPara ampliar custará:",self.custo_estoque)
        self.confirmacao = str(input("Deseja confimar? (s = Sim/n = Não): "))
        if self.confirmacao == 's':
            self.estoque_atual += self.qtda_produto
            self.caixa_atual -= self.custo_estoque
            print("Seu atual estoque é de:",self.estoque_atual,"\nO caixa agora tem:",self.caixa_atual)

        if self.confirmacao == 'n':
            self.__init__()

#Programa Principal
App = Product()