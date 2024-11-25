import time

from Produtos import Produto

def editarProduto(produtos):
        indexProduto = 1
        continuar = True
        print("Qual desses deseja pegar para editar: ")
        for prod in produtos:
            print(f"Produto {prod.getName()} está na posição {indexProduto} ")
            indexProduto +=1
            time.sleep(.6)
        while True:
            escolhaProduto = int(input("Digite a posição que deseja: ")) - 1
            if escolhaProduto >= 0 and escolhaProduto < indexProduto:
                break
            else:
                print(f"Escolha um indice entre 1 e {indexProduto}." )

        while continuar:
            produto = produtos[escolhaProduto]
            print("O que deseja modificar desse item?")
            print("[1] Nome")
            print("[2] Preços")
            print("[3] Quantidade")
            print("[0] Sair da edição")
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                print("Você escolheu modificar o Nome.")
                nome = str(input("Digite um nome: "))
                produto.modifyName(nome)
                print(f"Nome modificado para {nome}!!")
            elif opcao == 2:
                print("Você escolheu modificar os Preços.")
                preco = float(input("Digite o preço novo do produto"))
                produto.modifyPrice(preco)
                print(f"Preço modificado para {preco:.2f}")
            elif opcao == 3:
                print("Você escolheu modificar a Quantidade.")
                quantidade = int(input("Digite quantos desses produtods temos: "))
                produto.modifyAmount(quantidade)
                print(f"Quantidade alterada com sucesso para {quantidade}")
            elif opcao == 0:
                print("Saindo da edição", end="")
                for i in range(3):
                    print(".", end="")
                    time.sleep(.4)
                break
                print("")
            else:
                print("Opção inválida. Tente novamente.")