class Menu:
    def __init__(self):
        self.opt = 0
        
    def menu_estoque(self):
        while True:
            print(f'=' * 30)
            print(f'======== MENU ESTOQUE ========')
            print(f'Escolha uma das opções abaixo: ')
            print(f'1 - Cadastrar Produto.\n'
                + f'2 - Alterar Produto.\n'
                + f'3 - Excluir Produto.\n'
                + f'4 - Buscar Produto.\n'
                + f'5 - Relatório de todos os Produtos.\n'
                + f'6 - Produtos que mais saíram.\n'    
                + f'0 - Sair do sistema.\n'
            )
            
            self.opt = int(input(f'Sua escolha: '))
            
            if self.opt == 1:
                print(f'Vamos cadastrar um produto!')
            elif self.opt == 2:
                print(f'Vamos alterar um produto!')
            elif self.opt == 3:
                print(f'Vamos excluir um produto!')
            elif self.opt == 4:
                print(f'Vamos Buscar um produto!')
            elif self.opt == 5:
                print(f'Vamos exibir um relatório listando os produtos!')
            elif self.opt == 6:
                print(f'Quais produtos mais saíram?')
            elif self.opt == 0:
                print(f'Saindo...')
                break
            else:
                print(f'Não tem essa opção, escolha outra!')
        