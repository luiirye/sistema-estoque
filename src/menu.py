from produto import GerenciarProdutos
from tipos_validos import TiposValidos
from rich.panel import Panel
from rich import print

class Menu:
    def __init__(self):
        self.opt = 0
        self.produto  = GerenciarProdutos() # Objeto para guardar o produto
        self.tipos = TiposValidos() # Objeto para validar se o tipo informado está correspondendo ao que é pedido
        
    def menu_estoque(self):
        
        while True:
            
            titulo = "MENU DE ESTOQUE" 
            
            conteudo_menu  = "Escolha uma das opções abaixo:\n\n"
            conteudo_menu += "1 - Cadastrar Produto(s).\n"
            conteudo_menu += "2 - Alterar Produto(s).\n"
            conteudo_menu += "3 - Excluir Produto(s).\n"
            conteudo_menu += "4 - Listagem de Produto(s).\n"
            conteudo_menu += "0 - Encerrar menu.\n"
            
            painel = Panel(conteudo_menu, title=titulo, width=40)
            
            print(painel)           
            
            self.opt = self.tipos.ler_inteiro(f'Sua escolha: ')
            
            # Opção para cadastrar um produto na lista
            if self.opt == 1:
                self.produto.cadastrar_produto()
                print(f'Produto Cadastrado com sucesso!')
            
            # Opção para realizar alterações em um produto da lista
            elif self.opt == 2:
                self.produto.alterar_produto()
                print(f'Produto alterado com sucesso!')
            
            # Opção para excluir um produto da lista
            elif self.opt == 3:
                self.produto.excluir_produto()
            
            # Opção para listar os produtos da lista
            elif self.opt == 4:
                self.produto.lista_produtos()
                
                resposta = ""
                
                while True:
                    resposta = self.tipos.ler_texto(f'Deseja exibir todos os produtos com seus detalhes? S/N: ').strip().lower()
                    
                    if resposta == 's':
                        self.produto.visualizar_produtos()
                    elif resposta == 'n':
                        break
                    else:
                        print(f'Repostas não correspondente, tente novamente!')
                print(f'Fim da lista de prouto(s)!')
                        
            elif self.opt == 0:
                print(f'Saindo...')
                break
            
            else:
                print(f'Não tem essa opção, escolha outra!')
        
        
teste = Menu()
teste.menu_estoque()