import time

from uteis.CriarProduto import criarProduto
from uteis.VerificarLista import verificarListaVazia
from uteis.listarProduto import listarProdutos
from uteis.EditarProduto import editarProduto
def main():
    produtos = []
    while True:
        print("-" * 30)
        print("[1] Criar Produto")
        print("[2] Listar Produtos")
        print("[3] Editar Produto")
        print("[4] Sair do Programa")
        print("-" * 30)
        escolhaUsuario = int(input("Digite qual deseja: "))

        if escolhaUsuario == 1:
          criarProduto(produtos)
        elif escolhaUsuario == 2:
            if(verificarListaVazia(produtos)):
                print("Crie algo, pois não possui itens para serem listados.")
            else:
                listarProdutos(produtos)
        elif escolhaUsuario == 3:
            if (verificarListaVazia(produtos)):
                print("Crie algo, pois não possui itens para serem listados.")
            else:
                editarProduto(produtos)
        elif escolhaUsuario == 4:
            print("Saindo do programa", end="")
            for i in range(3):
                print(".", end="")
                time.sleep(.4)
            break


main()