from request_test import Movie
from time import sleep


class Menu:
    
    def voltar(self):
        print(' ___________________________________________________________')
        print('|                                                           |')
        print('|\t\t  VOLTANDO PARA O MENU...                   |')
        print('|___________________________________________________________|')
        sleep(1.5)
        
    def escolhas(self, escolha):

        if escolha == '0':

            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|\t\t    Até um outro dia!                       |')
            print('|___________________________________________________________|')
            print()

            return 0

        elif escolha == '1':

            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|\t\t   Busca de Filmes                          |')
            print('|___________________________________________________________|')
            sleep(1)
            menu = Movie()
            menu.busca_filme()

            voltando = Menu()
            voltando.voltar()

            filme = Menu()
            filme.pedidos()

        elif escolha == '2':
            menu = Movie()
            menu.listar()

            voltando = Menu()
            voltando.voltar()

            filme = Menu()
            filme.pedidos()

        elif escolha == '3':
            menu = Movie()
            menu.busca_desejos()

            voltando = Menu()
            voltando.voltar()

            filme = Menu()
            filme.pedidos()

        elif escolha == '4':
            menu = Movie()
            menu.mudar()

            voltando = Menu()
            voltando.voltar()

            filme = Menu()
            filme.pedidos()

        elif escolha == '5':
            menu = Movie()
            menu.deletar_filme()

            voltando = Menu()
            voltando.voltar()

            filme = Menu()
            filme.pedidos()

        else:
            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|\t\t     OPÇÃO INVÁLIDA                         |')
            print('|___________________________________________________________|')
            sleep(1)
            voltando = Menu()
            voltando.voltar()
            
            filme = Menu()
            filme.pedidos()
   
            

    def pedidos(self):
        menu = Menu()
        print(' ___________________________________________________________')
        print('|                                                           |')
        print('|\t\t\t  MENU                              |')
        print('|___________________________________________________________|')
        sleep(1)
        print(' ___________________________________________________________')
        print('|                                                           |')
        print('| 1-Buscar Filmes                                           |')
        print('| 2-Ver lista de desejos                                    |')
        print('| 3-Buscar filme na lista de desejos                        |')
        print('| 4-Alterar filme                                           |')
        print('| 5-Remover filme                                           |')
        print('| 0-Sair                                                    |')
        print('|                                                           |')
        escolha = input('| >>> ')
        print('|___________________________________________________________|')
        menu.escolhas(escolha)

        
if __name__ == "__main__":
    menu = Menu()
    menu.pedidos()