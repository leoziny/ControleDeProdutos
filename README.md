# Sistema de Gerenciamento de Produtos

Este projeto é um sistema simples para gerenciar produtos, desenvolvido em Python. Ele permite que o usuário crie, liste e edite produtos de forma interativa no terminal.

## Funcionalidades

- **Criar Produto**: Permite adicionar produtos à lista, com nome, preço e quantidade.
- **Listar Produtos**: Exibe todos os produtos cadastrados, mostrando suas informações.
- **Editar Produto**: Permite modificar o nome, preço ou quantidade de um produto específico.
- **Validações**: Verifica entradas inválidas para evitar erros durante a execução.

---

## Estrutura do Projeto

```plaintext
├── main.py              # Arquivo principal que executa o programa
├── Produtos.py          # Classe Produto com métodos para manipulação de dados
├── uteis/
│   ├── CriarProduto.py  # Função para criar produtos
│   ├── EditarProduto.py # Função para editar produtos
│   ├── ListarProduto.py # Função para listar produtos
│   ├── VerificarLista.py # Função para verificar se a lista de produtos está vazia
└── README.md            # Documentação do projeto
```
# Como usar?

## Clone o repositório
git clone https://github.com/seu-usuario/sistema-gerenciamento-produtos.git
cd sistema-gerenciamento-produtos
### Execute
python main.py
## Interaja com o menu
O programa oferece um menu interativo com as seguintes opções:

[1] Criar Produto: Adicione produtos à lista.

[2] Listar Produtos: Veja todos os produtos cadastrados.

[3] Editar Produto: Altere informações de um produto específico.

[4] Sair do Programa: Encerre o sistema.
