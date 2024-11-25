

class Produto():
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


    def getName(self):
        return self.nome
    def getPrice(self):
        return self.preco
    def getAmount(self):
        return self.quantidade

    def modifyName(self, nome):
        self.nome = nome
        return self.nome
    def modifyPrice(self, preco):
        self.preco = preco
        return self.preco
    def modifyAmount(self, preco):
        self.preco = preco
        return self.preco




