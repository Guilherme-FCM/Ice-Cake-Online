import os
import time

class Interface:
    def __init__(self, menu = { 'Não foram passadas funcionalidades.': None }, nomeMenu = 'Menu'):
        self.__menu = menu
        self.nomeMenu = nomeMenu

    def start(self):
        try:
            self.__MainFlag = True
            while self.__MainFlag:
                self.execute()  
                self.__limpar()
      
        except KeyboardInterrupt: print('\n\nPrograma interrompido pelo usuário!')

    def execute(self):
        self.show()
        opcao = self.opcao()

        if opcao == 0: self.sair()
        else:
            funcao = self.__funcao(opcao - 1)
            retorno = funcao()
            if retorno: print(f'\n{retorno}')

    def addFuncionalidade(self, funcionalidade = {}):
        for nome, func in funcionalidade.items(): self.__menu[nome] = func

    def removeFuncionalidade(self, nome): del self.__menu[nome]

    def show(self):
        self.exibirLogo()
        for idx, menu in enumerate(self.__menu.keys()): print(f'  [{idx + 1}] {menu}')
        print('  [0] Sair')
    
    def opcao(self): 
        while True:
            try: 
                opcao = int(input('\nOpção: '))

                if opcao > len(self.__menu) or opcao < 0: print('Opção inválida. Tente novamente!')
                else: return opcao
            except ValueError: print('Opção inválida. Tente novamente!')

    def exibirLogo(self): self.nomeMenu != '' and print(f'\n <-- {self.nomeMenu} -->\n')

    def __limpar(self):
        input('\nENTER Para Prosseguir...')
        os.system('cls' if os.name == 'nt' else 'clear')

    def __funcao(self, idx):
        for i, funcao in enumerate(self.__menu.values()): 
            if idx == i: return funcao

    def sair(self): 
        print('Finalizando processos e salvando dados...')
        time.sleep(1.5)
        print('Obrigado por utiliza nosso software!')
        self.__breakMainLoop()
    
    def __breakMainLoop(self): self.__MainFlag = False