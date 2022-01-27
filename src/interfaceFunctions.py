from classes.IceCakeOnline import IceCakeOnline
from src.Interface import Interface

cake = None

def dadosEmpresa(): 
    def cadastrarAtualizarDados():
        global cake
        name = input('Nome do Restaurante: ')
        typ = input('Tipo de Cozinha....: ')
        cake = IceCakeOnline(name, typ)
        print('Sua empresa foi cadastrada com sucesso!')
    
    def consultarDados():
        try: cake.describe_restaurant()
        except AttributeError: print('Empresa Não Cadastrada')

    Interface({
        'Cadastrar/Atualizar Dados': cadastrarAtualizarDados,
        'Consultar Dados': consultarDados
    }).execute()

def inserirAtualizarProdutosEstoque(): 
        print('\n--- Adição de Produtos no Estoque ---')
        try:
            name = input('Sabor ....: ').capitalize()
            quantity = int(input('Quantidade: '))
            price = float(input('Preço RS..: '))

            cake.addFlavor(name, { 'estoque': quantity, 'preco': price })
        except ValueError: print('Algum valor inválido. Tente novamente.')
        except AttributeError: print('Empresa Não Cadastrada')

def consultarEstoque(): 
    try: 
        print(' \n--- Produtos no Estoque ---')
        print('| Sabor | Quantidade | Preço RS |')
        cake.show_flavors()
    except AttributeError: print('Empresa Não Cadastrada')  

def registrarPedido(): 
    try:
        print('\n--- Dados para Entrega ---')
        while True:
            cep = input('CEP: ')
            endereco = cake.verificarCep(cep)
            if endereco:
                complemento = input('Complemento ....: ')
                break
            else: print('CEP Inválido. Tente novamente')

        listaPedido = []

        print('\n--- Registrar Pedido ---')
        while True:
            flavor = input('Sabor do Bolo ..: ')
            quantity = input('Quantidade .....: ')

            if cake.verificarPedido(flavor, quantity):
                listaPedido.append(cake.contruirPedido(flavor, quantity))
                continuar = input('Outro Sabor? [S / N]: ')
                
                if continuar.lower() != 's':
                    endereco = cake.addComplementoEndereco(complemento, endereco)
                    numeroPedido = cake.fazerPedido(listaPedido, endereco)
                    print('Numero do seu pedido:', numeroPedido)
                    break
            else: 
                print('Sabor inválido ou estoque insuficiente.')
                if input('Tentar Novamente? [S / N]: ').lower() == 'n': break

    except AttributeError: print('Empresa Não Cadastrada')

def alterarPedido(): 
    try: 
        numeroPedido = input('\nNúmero do Pedido: ')
        print(f'Pedido {numeroPedido} alterado!')
    except AttributeError: print('Empresa Não Cadastrada')

def consultarPedido(): 
    try: cake.showPedido()
    except AttributeError: print('Empresa Não Cadastrada')

def entregarPedido(): 
    try:
        if len(cake.pedidos) > 0:
            resp = input('Pedido foi entregue? [S/N]: ')
            entregue = True if resp.lower() == 's' else False
            status = input('Status: ')
            cake.atenderPedido(entregue, status)
        else: print('\nNão há pedidos para serem entregues...')
    except AttributeError: print('Empresa Não Cadastrada')

def consultarPedidosEntregues():
    try: cake.pedidosEntregues()
    except AttributeError: print('Empresa Não Cadastrada')