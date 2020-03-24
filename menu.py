from wishlist import Movie
from time import sleep
import os

class Menu:
    
    def chamando(self):

        while True:

            print(' ___________________________________________________________')
            print('|                                                           |')
            print('| 1-Menu                                                    |')
            print('|___________________________________________________________|')
            print('|                                                           |')
            sair = input('| >>> ')
            print('|___________________________________________________________|')

            if sair == '1':

                os.system('clear')
                break

            else:

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t\t       OPÇÃO INVÁLIDA                       |')
                print('|___________________________________________________________|')
                sleep(1)


    def voltar(self):

        os.system('clear')
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

            return
            

        elif escolha == '1':

            menu = Movie()
            menu.busca_filme()


        elif escolha == '2':

            menu = Movie()
            menu.listar()

        elif escolha == '3':

            menu = Movie()
            menu.busca_desejos()


        elif escolha == '4':

            menu = Movie()
            menu.mudar()


        elif escolha == '5':
            
            menu = Movie()
            menu.deletar_filme()

        elif escolha == '6':

            menu = Movie()
            menu.sugestao_ultimo()

        elif escolha == '7':

            menu = Movie()
            menu.sugestao_historico()


        else:

            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|\t\t      OPÇÃO INVÁLIDA                        |')
            print('|___________________________________________________________|')

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
        print('| 1-Buscar Filmes e Séries                                  |')
        print('| 2-Ver sua lista de desejos                                |')
        print('| 3-Buscar filmes e séries na lista de desejos              |')
        print('| 4-Alterar status de filmes ou séries                      |')
        print('| 5-Remover filmes ou séries                                |')
        print('| 6-Sugestões pelo último filme/série adicionado(a)         |')
        print('| 7-Sugestões pelo histórico                                |')
        print('| 0-Sair                                                    |')
        print('|___________________________________________________________|')
        print('|                                                           |')
        escolha = input('| >>> ')
        print('|___________________________________________________________|')
        
        if escolha == '0':

            menu.escolhas(escolha)
            

        elif escolha == '1':

            menu.escolhas(escolha)

            voltando = Menu()
            voltando.voltar()

            filme = Menu()
            filme.pedidos()

        elif escolha == '2':

            menu.escolhas(escolha)

            chamar = Menu()
            chamar.chamando()

            voltando = Menu()
            voltando.voltar()

            filme = Menu()
            filme.pedidos()

        elif escolha == '3':

            menu.escolhas(escolha)

            chamar = Menu()
            chamar.chamando()

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

        elif escolha == '6':

            menu.escolhas(escolha)

            chamar = Menu()
            chamar.chamando()

            voltando = Menu()
            voltando.voltar()

            filme = Menu()
            filme.pedidos()

        elif escolha == '7':

            menu.escolhas(escolha)

            chamar = Menu()
            chamar.chamando()

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