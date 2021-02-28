from classes import IceCreamStand
from pycep_correios import get_address_from_cep as consultar_cep
from pycep_correios.exceptions import BaseException
from datetime import datetime

class IceCakeOnline(IceCreamStand):
    def __init__(self, restaurant_name, cuisine_type, flavors = {}, number_served = 0):
        super().__init__(restaurant_name, cuisine_type, flavors, number_served)
        # self.pedidos = {'endereco': {}, 'pedidos': [], 'total': 0}
        self.pedidos = []
        self.statusPedido = ''
        
    def verificarCep(self, cep):
        try:
            endereco = consultar_cep(cep)
            return endereco
        except: return False
    
    def addComplementoEndereco(self, complemento, endereco):
        endereco["complemento"] = complemento
        return endereco
    
    def contruirPedido(self, sabor, quantidade):
        return {
            'sabor': sabor.capitalize(), 
            'quantidade': int(quantidade), 
            'valor': self.flavors[sabor.capitalize()]["preco"] * int(quantidade)
        }
    
    def fazerPedido(self, listaPedidos, endereco): 
        accTotal = 0
        for pedido in listaPedidos: accTotal += pedido["valor"]
        self.pedidos.append({'endereco': endereco, 'pedidos': listaPedidos, 'total': accTotal, 'numero': len(self.pedidos)}) 
        return len(self.pedidos)
        
    def addFlavor(self, flavor, attrs): self.flavors[flavor] = attrs
    
    def verificarPedido(self, sabor, quantidade):
        try:
            if self.flavors[sabor.capitalize()]["estoque"] >= int(quantidade) : return True
            else: return False
        except KeyError: return False
    
    def showPedido(self):
        try:
            endereco = self.pedidos[0]["endereco"]
            print(f'Pedido número {self.pedidos[0]["numero"]}')
            print(f'\nEntregar em: {endereco["logradouro"]}, {endereco["bairro"]}, {endereco["cidade"]}-{endereco["uf"]}')
            print(f'\nComplemento: {endereco["complemento"]}')
            print('\n--- Descrição ---\n')
            for pedido in self.pedidos[0]["pedidos"]:
                print(f'{pedido["sabor"]}: {pedido["quantidade"]} unidade(s)')
            print(f'Total: R$ {pedido["valor"]}')
        except IndexError: print('Não há pedidos na fila!')
        
    def decrementarEstoque(self, sabor, num = 1):
        self.flavors[sabor.capitalize()]["estoque"] -= num
        
    def atenderPedidos(self, statusPedido, pedidoEntregue):    
        if pedidoEntregue:
            arquivo = open('pedidos.txt','a')
            data = datetime.now()
            endereco = self.pedidos[0]["endereco"]
            
            arquivo.write('------- PEDIDO ------------------------------\n')
            arquivo.write(f'\nData: {data.day}/{data.month}/{data.year}\n')
            arquivo.write(f'\nHora: {data.hour}:{data.minute}\n')
            arquivo.write(f'\nEntregar em: {endereco["logradouro"]}, {endereco["bairro"]}, {endereco["complemento"]}\n')
            arquivo.write(f'\nCidade: {endereco["cidade"]}-{endereco["uf"]}\n')
            arquivo.write('\n------ DESCRICAO -------------------------------\n')
            arquivo.write('\nSabor do Bolo  |   Quantidade:\n')
            
            for pedido in self.pedidos[0]["pedidos"]: 
                arquivo.write(f'\n{pedido["sabor"]}   |     {pedido["quantidade"]}\n')
                self.decrementarEstoque(pedido["sabor"], pedido["quantidade"])
            arquivo.write(f'\nTotal: R$ {self.pedidos[0]["total"]}\n\n')
            arquivo.close()
            self.increment_number_served()
            
        self.pedidos.pop(0)
        self.statusPedido = statusPedido
        
    def pedidosEntregues(self):
        arquivo = open('pedidos.txt', 'r')
        print(arquivo.read())