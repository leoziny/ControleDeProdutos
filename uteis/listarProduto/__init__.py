import time


def listarProdutos(listaProdutos):
    for produto in listaProdutos:
        print(f"Nome = {produto.nome}, Preço = {produto.preco}, Quantidades = {produto.quantidade}")
        time.sleep(.6)