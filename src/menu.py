from produto import GerenciarProdutos

class Menu:
    def __init__(self):
        self.opt = 0
        self.produto  = GerenciarProdutos() # Objeto para guardar o produto
        
    def menu_estoque(self):
        while True:
            print(f'=' * 30)
            print(f'======== MENU ESTOQUE ========')
            print(f'Escolha uma das opções abaixo: ')
            print(f'1 - Cadastrar Produto(s).\n'
                + f'2 - Alterar Produto(s).\n'
                + f'3 - Excluir Produto(s).\n'
                + f'4 - Lista de Produto(s).\n'
                + f'5 - Relatório de todos .\n'
                + f'6 - Produtos que mais saíram.\n'    
                + f'0 - Sair do sistema.\n'
            )
            
            self.opt = int(input(f'Sua escolha: '))
            
            # Concluído
            if self.opt == 1:
                self.produto.cadastrar_produto()
                print(f'Produto Cadastrado com sucesso!')
            
            elif self.opt == 2:
                print(f'Vamos alterar um produto!')
            
            elif self.opt == 3:
                print(f'Vamos excluir um produto!')
            
            elif self.opt == 4:
                self.produto.lista_produtos()
                
                resposta = ""
                
                while True:
                    resposta = input(f'Deseja exibir todos os produtos com seus detalhes? S/N: ').strip().lower()[0]
                    
                    if resposta == 's':
                        self.produto.visualizar_produtos()
                    elif resposta == 'n':
                        break
                    else:
                        print(f'Repostas não correspondente, tente novamente!')
                print(f'Fim da lista de prouto(s)!')
            
            elif self.opt == 5:
                print(f'Vamos exibir um relatório listando os produtos!')
            
            elif self.opt == 6:
                print(f'Quais produtos mais saíram?')
            
            elif self.opt == 0:
                print(f'Saindo...')
                break
            
            else:
                print(f'Não tem essa opção, escolha outra!')
        