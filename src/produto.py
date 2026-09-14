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
        
        print(f'TELA PARA VISUALIZAR OS PRODUTOS')
        for produto in self.estoque:
            print(f'nome: {produto.nome}')            
            print(f'descrição: {produto.descricao}')
            print(f'quantidade: {produto.quantidade}')
            print(f'Preço de compra: R$ {produto.preco_compra:.2f}')
            print(f'Preço de Venda: R$ {produto.preco_venda:.2f}')