import os

class Menu:
    def __init__(self):
        self.homeMenu = '''
<--- SISTEMA ICECAKE ONLINE --->

1 - Dados da Empresa
2 - Inserir/atualizar Produtos no Estoque
3 - Consultar Estoque
4 - Registrar Pedido
5 - Alterar Pedido
6 - Consultar Pedido
7 - Entregar Pedido
8 - Consultar Pedido Entregues
9 - Sair
''' 
        self.menuList = [
            [
                ' \n1 - Consultar Dados \n2 - Cadastrar/Atualizar Dados',
                [ 
                    'Nome do Restaurante: ',
                    'Tipo de Cozinha....: '
                ]

            ], 
            
            [
                ' \n--- Adição de Produtos no Estoque ---',
                [
                    'Nome .....: ',
                    'Quantidade: ',
                    'Preço RS..: '
                ]
            ],
            
            [
                ' \n--- Produtos no Estoque ---',
                '| Sabor | Quantidade | Preço RS |',
            ],
            
            [
                '\n--- Dados para Entrega ---',
                [
                    'Sabor do Bolo ..: ',
                    'Quantidade .....: '
                ]
            ],
            
            [   
                '',
                '\nNúmero do Pedido: '
            ],
            
            [
                '',
                None 
            ],
            
            [
                ' \n--- Entregando Pedido --- \n1 - Pedido Entregue \n2 - Destinatário Ausente \n3 - Endereço Não Existe',
                [
                    'Pedido Entregue',
                    'Destinatário Ausente',
                    'Endereço Não Existe'
                ]
            ],
            
            [
                '',
                None
            ],
            [
                '',
                None
            ]           
]
        
    def __str__(self): return self.homeMenu
        
    def limparTela(self):
        input('\nENTER Para Prosseguir...')
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def inputOption(self, text = ''): 
        print(text)
        return input('Opção: ')
    
    def menu(self, idx):
        if idx >= len(self.menuList): return ValueError
        print(self.menuList[idx][0])
        return self.menuList[idx][1]
    
# menu = Menu()