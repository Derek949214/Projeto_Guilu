import requests,json
from time import sleep

class Movie:
    
    def busca_filme(self):

        lista = list()
        chave = '7db9f6c4'
        print(' ___________________________________________________________')
        print('|                                                           |')
        print('| Digite seu filme                                          |')
        print('|                                                           |')
        pesquisa = input('| >>> ')
        print('|___________________________________________________________|')

        status = 'Pendente'
        response = requests.get("http://www.omdbapi.com/?apikey={}&s={}".format(chave,pesquisa)).json()

        if response['Response'] == 'False':
            
           response = requests.get("http://www.omdbapi.com/?apikey={}&t={}".format(chave,pesquisa)).json()

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

           if response['Response'] == 'False':
                
                print(' ___________________________________________________________')
                print('|                                                           |')
                print('| \t\t   O filme não existe!                      |')
                print('|___________________________________________________________|')
                sleep(1)

                #print(response)
                return

        else:
            
            print('--' * 110)
            print(json.dumps(response, indent=4))
            print('--' * 110)

        sleep(1.5)

        print(' ___________________________________________________________')
        print('|                                                           |')
        print('| Escolha o filme que deseja                                |')
        print('|                                                           |')
        titulo = input('| >>> ')
        print('|___________________________________________________________|')

        response = requests.get("http://www.omdbapi.com/?apikey={}&t={}".format(chave,titulo)).json()

        if response['Response'] == 'False':
            
            print(' ___________________________________________________________')
            print('|                                                           |')
            print('| \t\t   O filme não existe!                      |')
            print('|___________________________________________________________|')
            sleep(1)

            #print(response)
            return
        
        else:
            pass

        print(' ___________________________________________________________')
        print('|                                                           |')
        print('|\t\t    DETALHES DO FILME                       |')
        print('|___________________________________________________________|')
        sleep(1)
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
            'Titulo': response['Title'].lower(),
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

        escolha = input('| >>> ')
        print('|___________________________________________________________|')
        
        

        if escolha == '1':
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

                        print(' ____________________________________________________________')
                        print('|                                                            |')
                        print('| O filme foi adicionado a sua lista de desejos com sucesso! |')
                        print('|____________________________________________________________|')

                    sleep(1)

                
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


        if escolha == '2':

            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|\t\t O filme não foi adicionado!                |')
            print('|___________________________________________________________|')
            sleep(1)


    def listar(self):

        try:

            with open('wishlist.json') as arquivo:
                printar = json.load(arquivo)

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t\t   Sua lista de desejos                     |')
                print('|___________________________________________________________|')
                print('--' * 110)
                sleep(1)

                for item in printar:

                    print(' Título: ', item['Titulo'])      
                    print(' Ano: ', item['Ano'])
                    print(' Tempo: ', item['Tempo'])
                    print(' Genero: ', item['Genero'])
                    print(' Diretor: ', item['Diretor'])
                    print(' Escritor: ', item['Escritor'])
                    print(' Atores: ', item['Atores'])
                    print(' País: ', item['Pais'])
                    print(' Status: ', item['Status'])
                    print('--' * 110)
                    sleep(1)

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t\t      FIM DA LISTA                          |')
                print('|___________________________________________________________|')
                sleep(1)

        except FileNotFoundError:

            print(' ______________________________________________________________')
            print('|                                                              |')
            print('| Não existe nenhum filme na sua lista de desejos!             |')
            print('|______________________________________________________________|')
            sleep(1)
        
    def busca_desejos(self):

        flag = False

        try:

            with open('wishlist.json') as arquivo:
                printar = json.load(arquivo)

            print(' __________________________________________________________________')
            print('|                                                                  |')
            print('| Digite o nome do filme que deseja buscar na sua lista de desejos |')
            print('|                                                                  |')
            filme = input('| >>> ').lower().strip()
            print('|__________________________________________________________________|')

            for item in printar:

                if filme == item['Titulo']:
                    flag = True
                    break

            if flag:

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t\t      FILME ENCONTRADO!                     |')
                print('|___________________________________________________________|')
                sleep(1)
                print('--' * 110)
                print('Título: ', item['Titulo'])      
                print('Ano: ', item['Ano'])
                print('Tempo: ', item['Tempo'])
                print('Genero: ', item['Genero'])
                print('Diretor: ', item['Diretor'])
                print('Escritor: ', item['Escritor'])
                print('Atores: ', item['Atores'])
                print('País: ', item['Pais'])
                print('Status: ', item['Status'])
                print('')
                print('--' * 110)
                sleep(2)

            else:

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t\t    FILME NÃO ENCONTRADO!                   |')
                print('|___________________________________________________________|')
                sleep(1)


        except FileNotFoundError:

            print(' ______________________________________________________________')
            print('|                                                              |')
            print('| Não existe nenhum filme na sua lista de desejos!             |')
            print('|______________________________________________________________|')
            sleep(1)


    def mudar(self):

        try:
            with open('wishlist.json') as arquivo:
                altera = json.load(arquivo)
                
                print('--' * 110)
                for item in altera:

                    print(' Título: ', item['Titulo'])      
                    print(' Ano: ', item['Ano'])
                    print(' Tempo: ', item['Tempo'])
                    print(' Genero: ', item['Genero'])
                    print(' Diretor: ', item['Diretor'])
                    print(' Escritor: ', item['Escritor'])
                    print(' Atores: ', item['Atores'])
                    print(' País: ', item['Pais'])
                    print('Status: ', item['Status'])
                    print('--' * 150)
                    sleep(1)

            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|   Digite o nome do filme que deseja alterar o status      |')
            print('|                                                           |')
            mudanca = input('| >>> ').lower().strip()
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
                        sleep(1)
                        
                elif alterar == '2':

                    item['Status'] = 'Assistir mais tarde'

                    with open('wishlist.json', 'w') as arquivo:
                        json.dump(altera, arquivo, indent=4)

                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('|\t     Marcado como "Assistir mais tarde"             |')
                        print('|___________________________________________________________|')
                        sleep(1)
                        
                elif alterar == '3':

                    item['Status'] = 'Continuar assistindo'

                    with open('wishlist.json', 'w') as arquivo:
                        json.dump(altera, arquivo, indent=4)

                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('|\t      Marcado como "Continuar assistindo"           |')
                        print('|___________________________________________________________|')
                        sleep(1)
                        

                elif alterar == '4':
                    
                    item['Status'] = 'Nao assistido'

                    with open('wishlist.json', 'w') as arquivo:
                        json.dump(altera, arquivo, indent=4)

                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('|\t\tMarcado como "Não assistido"                |')
                        print('|___________________________________________________________|')
                        sleep(1)
                        

                else:
                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|\t\t       OPÇÃO INVÁLIDA                       |')
                    print('|___________________________________________________________|')
                    sleep(1)
                    
            else:
                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t  O filme não existe na sua lista de desejos!       |')
                print('|___________________________________________________________|')
                sleep(1)
               

        except FileNotFoundError:

            print(' ______________________________________________________________')
            print('|                                                              |')
            print('| Não existe nenhum filme na sua lista de desejos!             |')
            print('|______________________________________________________________|')
            sleep(1)
                    

    def deletar_filme(self):

        try:
            with open('wishlist.json') as arquivo:
                delete = json.load(arquivo)

            print('--' * 110)
            for item in delete:
                
                print(' Título: ', item['Titulo'].title())      
                print(' Ano: ', item['Ano'])
                print(' Tempo: ', item['Tempo'])
                print(' Genero: ', item['Genero'])
                print(' Diretor: ', item['Diretor'])
                print(' Escritor: ', item['Escritor'])
                print(' Atores: ', item['Atores'])
                print(' País: ', item['Pais'])
                print(' Status: ', item['Status'])
                print('--' * 110)
                sleep(1)

            print(' ___________________________________________________________')
            print('|                                                           |')
            print('| Digite o filme que deseja excluir da sua lista de desejos |')
            print('|                                                           |')
            excluir = input('| >>> ').title().strip()
            print('|___________________________________________________________|')
                        
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

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|\t  Filme removido da sua lista de desejos            |')
                    print('|___________________________________________________________|')
                    sleep(1)
            
            else:
                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t O filme não existe na sua lista de desejos!        |')
                print('|___________________________________________________________|')
                sleep(1)
                
        except FileNotFoundError:

            print(' ______________________________________________________________')
            print('|                                                              |')
            print('| Não existe nenhum filme na sua lista de desejos!             |')
            print('|______________________________________________________________|')
            sleep(1)
        

    #print(response['Ratings'][2]['Value'])
