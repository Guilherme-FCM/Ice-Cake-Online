from iceCakeOnline import IceCakeOnline
from menu import Menu

def retornarInputs():
    lista = []
    for inpt in resposta:
        lista.append(input(inpt))
    return lista

def verificarRestaurante():
    try: 
        if cake: return True
    except NameError: return False
        
Menu = Menu()

while True:
    try:
        option = int(Menu.inputOption(Menu))
        resposta = Menu.menu(option - 1)
    except ValueError:
        print('Opção Inválida...')
        Menu.limparTela()
        continue
    if option == 1:
        opt = Menu.inputOption()
        if opt == '1':
            if verificarRestaurante(): cake.describe_restaurant()
            else: print('Empresa Não Cadastrada')
            
        elif opt == '2':
            
            lista = retornarInputs()
            cake = IceCakeOnline(*lista)
            print('Sua empresa foi cadastrada!')
            
        else: print('Opção inválida...')
        
    elif option == 2:
        if verificarRestaurante():
            try:
                lista = retornarInputs()
                attrs = {
                    'estoque': int(lista[1]),
                    'preco': float(lista[2])
                }
                cake.addFlavor(lista[0].capitalize(), attrs)
            except: print('Algum valor inválido. Tente novamente.')
        else: print('Empresa Não Cadastrada')
           
    elif option == 3:
        if verificarRestaurante():
            print(resposta)
            cake.show_flavors()
            
        else: print('Empresa Não Cadastrada')
        
    elif option == 4:
        if verificarRestaurante():
            while True:
                cep = input('CEP Para Entrega: ')
                endereco = cake.verificarCep(cep)
                if endereco:
                    complemento = input('Complemento ....: ')
                    break
                else: print('CEP Inválido. Tente novamente')
            listaPedido = []
            while True:
                print('\n--- Registrar Pedido ---')
                try:
                    lista = retornarInputs()
                    if cake.verificarPedido(*lista):
                        listaPedido.append(cake.contruirPedido(*lista))
                        continuar = input('Outro Sabor? [S / N]: ')
                        if continuar.lower() != 's':
                            endereco = cake.addComplementoEndereco(complemento, endereco)
                            numeroPedido = cake.fazerPedido(listaPedido, endereco)
                            print('Numero do seu pedido:', numeroPedido)
                            break
                    else: 
                        print('Sabor inválido ou estoque insuficiente.')
                        if input('Tentar Novamente? [S / N]: ').lower() == 'n': break         
                except: print('Algum valor inválido. Tente novamente.')
        else: print('Empresa Não Cadastrada')

    elif option == 5:
        if verificarRestaurante(): 
            numeroPedido = input(resposta)
            print(f'Pedido {numeroPedido} alterado!')
        else: print('Empresa Não Cadastrada')
        
    elif option == 6:
        if verificarRestaurante(): 
            cake.showPedido()
        else: print('Empresa Não Cadastrada')

    elif option == 7:
        if verificarRestaurante():
            if len(cake.pedidos) > 0:
                try:
                    status = int(Menu.inputOption())
                    pedidoEntregue = status == 1 and True or False
                    cake.atenderPedidos(resposta[status - 1], pedidoEntregue)
                except ValueError: 
                    print('Opção Inválida...')
                    Menu.limparTela()
            else: print('\nNão há pedidos para serem entregues...')
        else: print('Empresa Não Cadastrada')

    elif option == 8:
        if verificarRestaurante(): cake.pedidosEntregues()
        else: print('Empresa Não Cadastrada')

    elif option == 9:
        print('Fechando Programa e Salvando Dados...')
        Menu.limparTela()
        break
    
    else: 
        print('Opção Inválida... Tente novamente!')
        continue
    
    Menu.limparTela()