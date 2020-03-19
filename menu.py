from request_test import Movie
from time import sleep
import os

class Menu:
    
    def voltar(self):

        print(' ___________________________________________________________')
        print('|                                                           |')
        print('|\t\t  VOLTANDO PARA O MENU...                   |')
        print('|___________________________________________________________|')
        sleep(1.5)
        os.system('clear')
        
    def escolhas(self, escolha):
        
        if escolha == '0':

            os.system('clear') 

            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|\t\t         SAINDO...                          |')
            print('|___________________________________________________________|')
            sleep(1.5)
            os.system('clear')
            
            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|\t\t    Até um outro dia!                       |')
            print('|___________________________________________________________|')
            print()
            sleep(1)
            os.system('clear')
            

        elif escolha == '1':

            os.system('clear') 
            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|\t\t      Busca de Filmes                       |')
            print('|___________________________________________________________|')
            sleep(1)

            menu = Movie()
            menu.busca_filme()


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


        elif escolha == '4':

            menu = Movie()
            menu.mudar()


        elif escolha == '5':
            
            menu = Movie()
            menu.deletar_filme()


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
        print('|___________________________________________________________|')
        print('|                                                           |')
        escolha = input('| >>> ')
        print('|___________________________________________________________|')
        
        if escolha == '0':

            menu.escolhas(escolha)
            return
            

        elif escolha == '1':

            menu.escolhas(escolha)

            voltando = Menu()
            voltando.voltar()

            filme = Menu()
            filme.pedidos()

        elif escolha == '2':

            menu.escolhas(escolha)

            voltando = Menu()
            voltando.voltar()

            filme = Menu()
            filme.pedidos()

        elif escolha == '3':

            menu.escolhas(escolha)

            voltando = Menu()
            voltando.voltar()

            filme = Menu()
            filme.pedidos()

        elif escolha == '4':

            menu.escolhas(escolha)

            voltando = Menu()
            voltando.voltar()

            filme = Menu()
            filme.pedidos()

        elif escolha == '5':

            menu.escolhas(escolha)

            voltando = Menu()
            voltando.voltar()

            filme = Menu()
            filme.pedidos()

        else:

            menu.escolhas(escolha)

            voltando = Menu()
            voltando.voltar()

            filme = Menu()
            filme.pedidos()

        
if __name__ == "__main__":
    os.system('clear')
    menu = Menu()
    menu.pedidos()