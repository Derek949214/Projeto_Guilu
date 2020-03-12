import requests,json
from time import sleep

class Movie:
    
    def busca_filme(self):

        lista = list()
        chave = '7db9f6c4'
        print(' ____________________________________________________________')
        print('|                                                           |')
        print('| Digite seu filme                                          |')
        print('|                                                           |')
        titulo = input('| >>> ')
        print('|___________________________________________________________|')

        status = 'Pendente'
        
        response = requests.get("http://www.omdbapi.com/?apikey={}&t={}".format(chave,titulo)).json()

        if response['Response'] == 'False':
            
            print(' ___________________________________________________________')
            print('|                                                           |')
            print('| \t\t    O filme não existe!                     |'.format(titulo))
            print('|___________________________________________________________|')
            sleep(1)

            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|\t\t  VOLTANDO PARA O MENU...                   |')
            print('|___________________________________________________________|')
            sleep(1.5)
            #print(response)
            return
        
        else:
            pass

        print('--' * 110)
        print(' Título: ', response['Title'])      
        print(' Ano: ', response['Year'])
        print(' Tempo: ', response['Runtime'])
        print(' Genero: ', response['Genre'])
        print(' Diretor: ', response['Director'])
        print(' Escritor: ', response['Writer'])
        print(' Atores: ', response['Actors'])
        print(' País: ', response['Country'])
        print('--' * 110)

        dicionario = {
            'Titulo': response['Title'].title(),
            'Ano': response['Year'],
            'Tempo': response['Runtime'],
            'Genero': response['Genre'],
            'Diretor': response['Director'],
            'Escritor': response['Writer'],
            'Atores': response['Actors'],
            'Pais': response['Country'],
            'Status': status
        }

        lista.append(dicionario)
        sleep(1)
        print(' ___________________________________________________________')
        print('|                                                           |')
        print('|\t   Deseja adicionar a lista de desejos?             |')
        print('| 1-Sim                                                     |')
        print('| 2-Não                                                     |')

        escolha = int(input('| >>> '))
        print('|___________________________________________________________|')
        
        

        if escolha == 1:
            flag = True
            
            try:
                with open('wishlist.json') as arquivo:
                    desejo = json.load(arquivo)

                for item in desejo:

                    if dicionario['Titulo'] == item['Titulo']:

                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('|\t Esse filme já existe na sua lista de desejo!       |')
                        print('|___________________________________________________________|')

                        sleep(1)
                        flag = False
                        break
                    
                    else:
                        flag = True

                if flag:
                    desejo.append(dicionario)

                    with open('wishlist.json', 'w') as lista_desejos:
                        json.dump(desejo, lista_desejos, indent=4)

                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('| O filme foi adicionado a sua lista de desejos com sucesso!|')
                        print('|___________________________________________________________|')

                    sleep(1)

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|\t\t  VOLTANDO PARA O MENU...                   |')
                    print('|___________________________________________________________|')
                    sleep(1.5)
                
                else:
                    flag = False

            except FileNotFoundError:

                if flag:

                    with open('wishlist.json', 'w') as lista_desejos:
                        json.dump(lista, lista_desejos, indent=4)

                        print(' ____________________________________________________________')
                        print('|                                                            |')
                        print('| O filme foi adicionado a sua lista de desejos com sucesso! |')
                        print('|____________________________________________________________|')

                    sleep(1)

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|\t\t  VOLTANDO PARA O MENU...                   |')
                    print('|___________________________________________________________|')
                    sleep(1.5)

        if escolha == 2:
            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|\t\t  VOLTANDO PARA O MENU...                   |')
            print('|___________________________________________________________|')
            sleep(1.5)


    def listar(self):

        try:
            with open('wishlist.json') as arquivo:
                printar = json.load(arquivo)

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t\t   Sua lista de desejos                     |')
                print('|___________________________________________________________|')
                print('--' * 94)
                sleep(1)

                for item in printar:
                    print('Título: ', item['Titulo'])      
                    print('Ano: ', item['Ano'])
                    print('Tempo: ', item['Tempo'])
                    print('Genero: ', item['Genero'])
                    print('Diretor: ', item['Diretor'])
                    print('Escritor: ', item['Escritor'])
                    print('Atores: ', item['Atores'])
                    print('País: ', item['Pais'])
                    print('--' * 94)
                    sleep(1)

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|\t\t  VOLTANDO PARA O MENU...                   |')
                    print('|___________________________________________________________|')
                    sleep(1)

        except FileNotFoundError:
            print('Esse arquivo não foi criado ainda!')


        
    def busca_desejos(self):

        flag = False

        try:
            with open('wishlist.json') as arquivo:
                printar = json.load(arquivo)

            print(' __________________________________________________________________')
            print('|                                                                  |')
            print('| Digite o nome do filme que deseja buscar na sua lista de desejos |')
            print('|                                                                  |')
            filme = input('| >>> ').title()
            print('|__________________________________________________________________|')

            for item in printar:

                if filme == item['Titulo']:
                    flag = True

            if flag:
                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t\t      FILME ENCONTRADO!                     |')
                print('|___________________________________________________________|')
                sleep(1)
                print('--' * 94)
                print('Título: ', item['Titulo'])      
                print('Ano: ', item['Ano'])
                print('Tempo: ', item['Tempo'])
                print('Genero: ', item['Genero'])
                print('Diretor: ', item['Diretor'])
                print('Escritor: ', item['Escritor'])
                print('Atores: ', item['Atores'])
                print('País: ', item['Pais'])
                print('--' * 94)
                sleep(2)

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t\t  VOLTANDO PARA O MENU...                   |')
                print('|___________________________________________________________|')
                sleep(1.5)

            else:
                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t\t    FILME NÃO ENCONTRADO!                   |'.format(filme))
                print('|___________________________________________________________|')
                sleep(1)

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t\t  VOLTANDO PARA O MENU...                   |')
                print('|___________________________________________________________|')
                sleep(1.5)

        except FileNotFoundError:
            print('Não existe nenhum filme na sua lista de desejos!')



    def mudar(self):

        try:
            with open('wishlist.json') as arquivo:
                altera = json.load(arquivo)

                for item in altera:
                    print()
                    print(' Título: ', item['Titulo'])      
                    print(' Ano: ', item['Ano'])
                    print(' Tempo: ', item['Tempo'])
                    print(' Genero: ', item['Genero'])
                    print(' Diretor: ', item['Diretor'])
                    print(' Escritor: ', item['Escritor'])
                    print(' Atores: ', item['Atores'])
                    print(' País: ', item['Pais'])
                    print('--' * 110)
                    sleep(1)

            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|\tDigite o nome do filme que deseja alterar           |')
            print('|                                                           |')
            mudanca = input('| >>> ').title()
            print('|___________________________________________________________|')

            flag = False

            for item in altera:

                if mudanca == item['Titulo']:

                    flag = True
                    break
                        
            if flag:
                
                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t\t    Deseja marcar como...                   |')
                print('| 1-Assistido                                               |')
                print('| 2-Assistir mais tarde                                     |')
                print('| 3-Continuar assisitindo                                   |')
                print('| 4-Não assistido                                           |')
                print('|                                                           |')
                alterar = input('| >>> ')
                print('|___________________________________________________________|')
                
                if alterar == '1':

                    item['Status'] = 'Assistido'

                    with open('wishlist.json', 'w') as arquivo:
                        json.dump(altera, arquivo, indent=4)

                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('|\t\t  Marcado como "Assistido"                  |')
                        print('|___________________________________________________________|')
                    
                elif alterar == '2':

                    item['Status'] = 'Assistir mais tarde'

                    with open('wishlist.json', 'w') as arquivo:
                        json.dump(altera, arquivo, indent=4)

                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('|\t     Marcado como "Assistir mais tarde"             |')
                        print('|___________________________________________________________|')
                        
                elif alterar == '3':

                    item['Status'] = 'Continuar assistindo'

                    with open('wishlist.json', 'w') as arquivo:
                        json.dump(altera, arquivo, indent=4)

                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('|\t      Marcado como "Continuar assistindo"           |')
                        print('|___________________________________________________________|')

                elif alterar == '4':

                    item['Status'] = 'Nao assistido'

                    with open('wishlist.json', 'w') as arquivo:
                        json.dump(altera, arquivo, indent=4)

                        print('Marcado como "Não assistido"')

                else:
                    print('Opção inválida')

            else:
                print('O filme "{}" não existe na sua lista de desejos!'.format(mudanca))

        except FileNotFoundError:
            print('Não existe nenhum filme na sua lista de desejos!')
                    
                   

    def deletar_filme(self):

        try:
            with open('wishlist.json') as arquivo:
                delete = json.load(arquivo)

            for item in delete:

                print('Título: ', item['Titulo'])      
                print('Ano: ', item['Ano'])
                print('Tempo: ', item['Tempo'])
                print('Genero: ', item['Genero'])
                print('Diretor: ', item['Diretor'])
                print('Escritor: ', item['Escritor'])
                print('Atores: ', item['Atores'])
                print('País: ', item['Pais'])
                print('--' * 94)

            excluir = input('Digite o filme que deseja excluir da sua lista de desejos\n>>> ').title()
                        
            flag = False
            lista = list()
                    
            for item in delete:

                if excluir == item['Titulo']:
                    flag = True

            if flag:

                for item in delete:

                    if excluir != item['Titulo']:
                        lista.append(item)

                with open('wishlist.json', 'w') as arquivo:
                    json.dump(lista, arquivo, indent=4)

                    print('Filme removido da sua lista de desejos')

            else:
                print('O filme "{}" não existe na sua lista de desejos'.format(excluir))

        except FileNotFoundError:
            print('Não existe nenhum filme na sua lista de desejos!')
                        
        

    #print(response['Ratings'][2]['Value'])
