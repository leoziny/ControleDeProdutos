from Produtos import Produto


def criarProduto(produtos):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$"))
    try:
        quantidade = int(input("Digite quantos desse produto tem: "))
        novo_produto = Produto(nome, preco, quantidade)
        produtos.append(novo_produto)  # Adiciona o produto à lista
        print(f"Produto '{nome}' adicionado com sucesso!")
    except ValueError:
        print("Erro! Digite uma quantidade válida em números inteiros.")
