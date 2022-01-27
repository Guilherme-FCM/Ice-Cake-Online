from IceCakeOnline import IceCakeOnline
from Interface import Interface
from interfaceFunctions import *

interface = Interface({
    'Dados da Empresa': dadosEmpresa,
    'Inserir/atualizar Produtos no Estoque': inserirAtualizarProdutosEstoque,
    'Consultar Estoque': consultarEstoque,
    'Registrar Pedido': registrarPedido,
    'Alterar Pedido': alterarPedido,
    'Consultar Pedidos': consultarPedido,
    'Entregar Pedido': entregarPedido,
    'Consultar Pedidos Entregues': consultarPedidosEntregues
}, 'SISTEMA ICECAKE ONLINE')
interface.start()