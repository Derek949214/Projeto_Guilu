from request_test import Movie


class Menu:
    
    def escolhas(self, escolha):
        
        print('--' * 94)

        if escolha == 1:
            menu = Movie()
            menu.busca_filme()

            filme = Menu()
            filme.pedidos()

        if escolha == 2:
            menu = Movie()
            menu.mudar()

            filme = Menu()
            filme.pedidos()

        if escolha == 3:
            menu = Movie()
            menu.deletar_filme()

            filme = Menu()
            filme.pedidos()

        if escolha == 4:
            menu = Movie()
            menu.listar()

            filme = Menu()
            filme.pedidos()
   
            

    def pedidos(self):
        menu = Menu()
        print('--' * 94)
        print('\tMENU')
        print('--' * 94)
        print('1-Buscar Filmes')
        print('2-Alterar Filme')
        print('3-Remover Filme')
        print('4-Para ver a lista de desejos')

        escolha = int(input('>>> '))
        menu.escolhas(escolha)

        
if __name__ == "__main__":
    menu = Menu()
    menu.pedidos()