class Produto:
    
    def __init__(self, nome, descricao, quantidade, preco_compra, preco_venda):
        self.nome:str = nome
        self.descricao:str = descricao
        self.quantidade:int = quantidade
        self.preco_compra:float = preco_compra
        self.preco_venda:float = preco_venda

class GerenciarProdutos:
    
    def __init__(self):
        self.estoque = []
            
    def cadastrar_produto(self):
        
        print(f'CADASTRO DE PRODUTO')
        nome = input(f'Nome do produto: ')
        descricao = input(f'Descrição do produto: ')
        quantidade = int(input(f'Quantidade: '))
        preco_compra = float(input(f'Preço de compra: R$ '))
        preco_venda = float(input(f'Preço de Venda: R$ '))
        
        produto = Produto(nome, descricao, quantidade, preco_compra, preco_venda)
        
        self.estoque.append(produto)
        
    def visualizar_produtos(self):
        
        if not self.estoque:
            print(f'O estoque está vazio. Sem itens para visualizar.')
        else:
            print(f'TELA PARA VISUALIZAR OS PRODUTOS')
            for produto in self.estoque:
                print(f'nome: {produto.nome}')            
                print(f'descrição: {produto.descricao}')
                print(f'quantidade: {produto.quantidade}')
                print(f'Preço de compra: R$ {produto.preco_compra:.2f}')
                print(f'Preço de Venda: R$ {produto.preco_venda:.2f}')
    
    def lista_produtos(self):
        
        if not self.estoque:
            print(f'O estoque está vazio! Nenhum produto cadastrado.')
        
        else:
            print(f'Quantidade de produtos cadastrados: {len(self.estoque)}')

            # Percorrendo a lista para LISTAGEM
            # Utilizando enumerate para pegar ÍNDICE e PRODUTO
            for indice, produto in enumerate(self.estoque):
                print(f'{indice + 1}: -> {produto.nome}')
                
    def excluir_produto(self):
        
        if not self.estoque:
            print(f'O estoque não tem produtos, nada para excluir')
            
        else:
            opt:int = 0
            
            while True:
                print(f'Menu de Opções de Exclusão: ')
                print(
                     f'1 - Excluir ÚLTIMO PRODUTO CADASTRADO no estoque.\n'
                    +f'2 - Excluir produto ESPECÍFICO do estoque.\n'
                    +f'3 - Apagar TODO O ESTOQUE.\n'
                    +f'0 - Não quero excluir nenhum.\n'
                )
                
                opt = int(input(f'Sua escolha: '))
                
                if opt == 1:
                    print(F'Excluindo ÚLTIMO PRODUTO CADASTRADO.')
                    removido = self.estoque.pop()
                    print(f'Produto Removido: {removido.nome}')
                
                elif opt == 2:
                    self.lista_produtos()
                    item = int(input(f'Qual produto deseja remover do estoque?: '))
                    item -= 1
                    removido = self.estoque.pop(item)
                    print(f'{removido.nome} removido com sucesso!')
                    
                elif opt == 3:
                    
                    while True:
                    
                        resposta = str(input(f'TEM CERTEZA DE QUE DESEJA APAGAR TODO O ESTOQUE?: ')).upper().strip()
                    
                        if resposta == 'S':
                            print(f'Limpando estoque...')
                            self.estoque.clear()
                            print(f'Estoque limpo com sucesso!\nQuantidade de itens: {len(self.estoque)}')

                        elif resposta == 'N':
                            print(f'Retornando para menu de exclusão.')

                        else:
                            print(f'Escolha apenas S ou N.')
                        
                elif opt == 0:
                    print(f'Cancelando exclusão de produtos...')
                    break 
                
    def alterar_produto(self):
             
        if not self.estoque:
            print(f'Estoque vazio, ada para alterar.')

        else:
            print(f'Produtos registrados disponíveis para alteração: ')
            
            for indice, produto in enumerate(self.estoque):
                print(f'{indice + 1}: -> {produto.nome}')
                
            opt = int(input(f'Qual produto deseja alterar os dadots?: '))
            opt -= 1
            produto = self.estoque[opt]
            
            produto.nome = input(f'Nome do produto: ')
            produto.descricao = input(f'Descrição do produto: ')
            produto.quantidade = int(input(f'Quantidade: '))
            produto.preco_compra = float(input(f'Preço de compra: R$ '))
            produto.preco_venda = float(input(f'Preço de Venda: R$ '))
            
            print(f'Produto alterado com sucesso!')
            
            while True:
                
                resposta = str(input(f'Deseja ver uma lista dos produtos para ver a alteração?: [s/n] ')).lower().strip()
                
                if resposta == 's':
                    self.lista_produtos()
                    break
                
                elif resposta == 'n':
                    break
                
                else:
                    print(f'Não tem essa opção, escolha apenas s ou n')