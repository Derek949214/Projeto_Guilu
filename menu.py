from request_test import Movie


class Menu:
    def __init__(self):
        pass
    
    def escolhas(self, escolha):
        
        print('--' * 94)

        if escolha == 1:
            menu = Movie()
            menu.busca_filme()

        if escolha == 4:
            return 0
   
            

    def pedidos(self):
        menu = Menu()
        print('--' * 94)
        print('\tMENU')
        print('--' * 94)
        print('1-Buscar Filmes')
        print('2-Alterar Filme')
        print('3-Remover Filme')
        print('4-Sair')

        escolha = int(input('>>> '))
        menu.escolhas(escolha)

        
if __name__ == "__main__":
    menu = Menu()
    menu.pedidos()