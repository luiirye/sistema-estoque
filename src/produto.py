class Produto:
    
    def __init__(self):
        self.nome: str = ""
        self.categoria: str = ""
        self.tipo: str = ""
        self.fornecedor: str = ""
        self.quantidade: int = 0
        self.preco_compra: float = 0.0
        self.preco_venda: float = 0.0
        
        self.estoque_minimo: int = 0
        self.codigo: int = 0
          
class GerenciarProdutos:
    
    # Função que inicializa o atribut estoque, que armazena o produto cadastrado.
    def __init__(self):
        self.estoque: list = []
    
    # Função que cadastra um produto    
    def cadastrar_produto(self):
        
        produto = Produto() # Objeto para utilizar os atributos da classe Produto
        
        print(f'<=========== CADASTRO DE PRODUTO ===========>')
        print(f'Vamos cadastrar um produto!')
        print(f'Insira as informações solicitadas abaixo: ')
        
        produto.nome = (input(f'Nome: ')).strip().title()
        produto.categoria = input(f'Grupo(bebida, comida, etc): ').strip().lower()
        produto.tipo = input(f'Tipo(energético, salgado, etc): ').strip().lower()
        produto.decricao = input(f'Descriçõ para o Produto: ').strip().lower()
        produto.quantidade = int(input(f'Quantidade: '))
        produto.fornecedor = input(f'Fornecedor: ').strip().lower()
        produto.preco_compra = float(input(F'Preço de compra (Unidade) - R$: '))
        produto.preco_venda = float(input(f'Preço para vender {produto.nome} - R$: '))
        
        self.estoque.append(produto)