class TiposValidos:
    def __init__(self):
        self.valor_inteiro:int
        self.valor_float:float
        self.texto:str
        
    def ler_inteiro(self, mensagem) -> int:
        while True:
            try:
                return int(input(mensagem))
            
            except ValueError:
                print(ValueError)
                print(f'Valor inválido. Digite um valor inteiro.')
                
    def ler_float(self, mensagem) -> float:
        while True:
            try:
                return float(input(mensagem))
            
            except ValueError:
                print(ValueError)
                print(f'Valor inválido. Digite um valor float.')
                
    def ler_texto(self, mensagem) -> str:
        while True:
            texto = input(mensagem).strip()
            
            if texto:
                return texto
            else:
                print(f'Esse campo não pode ficar vazio.')