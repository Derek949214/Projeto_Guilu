import requests,json, os
from time import sleep

class Movie:
    
    def busca_filme(self):

        lista = list()
        chave = '7db9f6c4'
        status = 'Pendente'
        
        while True:

            os.system('clear') 
            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|\t          Busca de Filmes e Séries                  |')
            print('|___________________________________________________________|')
            sleep(1)
            
            print(' ___________________________________________________________')
            print('|                                                           |')
            print('| 1-Filmes                                                  |')
            print('| 2-Series                                                  |')
            print('|___________________________________________________________|')
            print('|                                                           |')
            escolha = input('| >>> ').lower()
            print('|___________________________________________________________|')


            if escolha == '1':

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('| Digite o nome do seu filme desejado                       |')
                print('|___________________________________________________________|')
                print('|                                                           |')
                pesquisa = input('| >>> ').lower()
                print('|___________________________________________________________|')

                response1 = requests.get("http://www.omdbapi.com/?apikey={}&s={}&type=movie".format(chave,pesquisa)).json()

                if response1['Response'] == 'False':
                    
                    response = requests.get("http://www.omdbapi.com/?apikey={}&t={}&type=movie".format(chave,pesquisa)).json()

                    if response['Response'] == 'False':
                        
                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('| \t\t   O filme não existe!                      |')
                        print('|___________________________________________________________|')
                        sleep(1)

                    else:
                        
                        os.system('clear')
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
                        print(' Tipo: ', response['Type'].title())
                        print('--' * 110)

                        break


                else:
                
                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|       SUGESTÕES DE FILMES RELACIONADAS COM O NOME!        |')
                    print('|___________________________________________________________|')
                    sleep(1)
                    
                    print('--' * 110)

                    for tamanho in range(0, len(response1['Search'])):

                        print(' Titulo: ', response1['Search'][tamanho]['Title'])
                        print(' Ano: ', response1['Search'][tamanho]['Year'])
                        print(' Tipo: ', response1['Search'][tamanho]['Type'])
                        print('--' * 110)
                        sleep(1)

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('| Escolha um dos filmes acima                               |')
                    print('|___________________________________________________________|')
                    print('|                                                           |')
                    titulo = input('| >>> ')
                    print('|___________________________________________________________|')
                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('| Digite o ano do filme escolhido                           |')
                    print('|___________________________________________________________|')
                    print('|                                                           |')
                    ano = input('| >>> ')

                    try:

                        for tamanho in range(0, len(response1['Search'])):

                            if titulo == response1['Search'][tamanho]['Title'] or ano == response1['Search'][tamanho]['Year']:

                                response = requests.get("http://www.omdbapi.com/?apikey={}&t={}&y={}&type=movie".format(chave,titulo, ano)).json()
                                
                                os.system('clear')
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
                                print(' Tipo: ', response['Type'].title())
                                print('--' * 110)

                                sleep(1.5)
                                    
                                break
                                            
                            else:
                                            
                                tamanho += 1

                            if tamanho == len(response1['Search']):
                                
                                os.system('clear')
                                print(' ___________________________________________________________')
                                print('|                                                           |')
                                print('|      Este filme não está na sugestão listada acima!       |')
                                print('|___________________________________________________________|')
                                sleep(1.7)
                                os.system('clear')
                                
                                
                                
                            else:
                                pass

                        break

                    except KeyError:
                        
                        os.system('clear')
                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('|         Esta sugestão não está listada acima!             |')
                        print('|___________________________________________________________|')
                        sleep(1.7)
                        os.system('clear')
                                

            elif escolha == '2':

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('| Digite o nome da sua série desejada                       |')
                print('|___________________________________________________________|')
                print('|                                                           |')
                pesquisa = input('| >>> ').lower()
                print('|___________________________________________________________|')

                response1 = requests.get("http://www.omdbapi.com/?apikey={}&s={}&type=series".format(chave,pesquisa)).json()
                
                if response1['Response'] == 'False':
                    
                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('| \t\t   Essa série não existe                    |')
                    print('|___________________________________________________________|')
                    sleep(1)

                else:

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|       SUGESTÕES DE SÉRIES RELACIONADAS COM O NOME!        |')
                    print('|___________________________________________________________|')
                    sleep(1)
                    
                    print('--' * 110)

                    for tamanho in range(0, len(response1['Search'])):

                        print(' Titulo: ', response1['Search'][tamanho]['Title'])
                        print(' Ano: ', response1['Search'][tamanho]['Year'])
                        print(' Tipo: ', response1['Search'][tamanho]['Type'])
                        print('--' * 110)
                        sleep(1)

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('| Escolha uma das series acima                              |')
                    print('|___________________________________________________________|')
                    print('|                                                           |')
                    titulo = input('| >>> ')
                    print('|___________________________________________________________|')
                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('| Digite o ano da serie escolhida                           |')
                    print('|___________________________________________________________|')
                    print('|                                                           |')
                    ano = input('| >>> ')

                    try:

                        for tamanho in range(0, len(response1['Search'])):

                            if titulo == response1['Search'][tamanho]['Title'] or ano == response1['Search'][tamanho]['Year']:

                                response = requests.get("http://www.omdbapi.com/?apikey={}&t={}&y={}&type=series".format(chave,titulo, ano)).json()
                                
                                os.system('clear')
                                print(' ___________________________________________________________')
                                print('|                                                           |')
                                print('|\t\t    DETALHES DA SÉRIE                       |')
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
                                print(' Tipo: ', response['Type'].title())
                                print('--' * 110)

                                sleep(1.5)
                                    
                                break
                                            
                            else:
                                            
                                tamanho += 1

                            if tamanho == len(response1['Search']):
                                
                                os.system('clear')
                                print(' ___________________________________________________________')
                                print('|                                                           |')
                                print('|      Este filme não está na sugestão listada acima!       |')
                                print('|___________________________________________________________|')
                                sleep(1.7)
                                os.system('clear')
                                
                                
                                
                            else:
                                pass

                        break

                    except KeyError:
                        
                        os.system('clear')
                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('|         Esta sugestão não está listada acima!             |')
                        print('|___________________________________________________________|')
                        sleep(1.7)
                        os.system('clear')
                                
                        return



            else:

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t\t       OPÇÃO INVÁLIDA                       |')
                print('|___________________________________________________________|')
                sleep(1)
                os.system('clear')


        if response['Response'] == 'False':
            
            print(' ___________________________________________________________')
            print('|                                                           |')
            print('| \t\t   O filme não existe!                      |')
            print('|___________________________________________________________|')
            sleep(1)
            os.system('clear')
            return

            #print(response)
        
        else:
            pass

        dicionario = {
            'Titulo': response['Title'].lower(),
            'Ano': response['Year'],
            'Tempo': response['Runtime'],
            'Genero': response['Genre'],
            'Diretor': response['Director'],
            'Escritor': response['Writer'],
            'Atores': response['Actors'],
            'Pais': response['Country'],
            'Tipo': response['Type'],
            'Status': status
        }

        lista.append(dicionario)
        sleep(1)
        print(' ___________________________________________________________')
        print('|                                                           |')
        print('|\t   Deseja adicionar a lista de desejos?             |')
        print('| 1-Sim                                                     |')
        print('| 2-Não                                                     |')
        print('|___________________________________________________________|')
        print('|                                                           |')
        escolha = input('| >>> ')
        print('|___________________________________________________________|')
        
        

        if escolha == '1':
            
            try:

                flag = True
                
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
                        os.system('clear') 
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
                    os.system('clear')

                
                else:

                    flag = False

            except FileNotFoundError:

                with open('wishlist.json', 'w') as lista_desejos:
                    json.dump(lista, lista_desejos, indent=4)

                    print(' ____________________________________________________________')
                    print('|                                                            |')
                    print('| O filme foi adicionado a sua lista de desejos com sucesso! |')
                    print('|____________________________________________________________|')

                os.system('clear')
                sleep(1)


        if escolha == '2':

            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|\t\t O filme não foi adicionado!                |')
            print('|___________________________________________________________|')
            sleep(1)
            os.system('clear')


    def listar(self):

        try:

            with open('wishlist.json') as arquivo:
                printar = json.load(arquivo)

                os.system('clear')
                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t\t   Sua lista de desejos                     |')
                print('|___________________________________________________________|')
                print('--' * 110)
                sleep(1)

                for item in printar:

                    print(' Título: ', item['Titulo'].title())      
                    print(' Ano: ', item['Ano'])
                    print(' Tempo: ', item['Tempo'])
                    print(' Genero: ', item['Genero'])
                    print(' Diretor: ', item['Diretor'])
                    print(' Escritor: ', item['Escritor'])
                    print(' Atores: ', item['Atores'])
                    print(' País: ', item['Pais'])
                    print(' Status: ', item['Status'])
                    print(' Tipo: ', item['Tipo'].title())
                    print('--' * 110)
                    sleep(1)

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t\t      FIM DA LISTA                          |')
                print('|___________________________________________________________|')
                sleep(1)
                
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

        except FileNotFoundError:

            print(' ______________________________________________________________')
            print('|                                                              |')
            print('|       Não existe nenhum filme na sua lista de desejos!       |')
            print('|______________________________________________________________|')
            sleep(1)
            os.system('clear')
        
    def busca_desejos(self):

        try:

            flag = False

            with open('wishlist.json') as arquivo:
                printar = json.load(arquivo)

            os.system('clear')
            print(' __________________________________________________________________')
            print('|                                                                  |')
            print('| Digite o nome do filme que deseja buscar na sua lista de desejos |')
            print('|__________________________________________________________________|')
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
                print('Título: ', item['Titulo'].title())      
                print('Ano: ', item['Ano'])
                print('Tempo: ', item['Tempo'])
                print('Genero: ', item['Genero'])
                print('Diretor: ', item['Diretor'])
                print('Escritor: ', item['Escritor'])
                print('Atores: ', item['Atores'])
                print('País: ', item['Pais'])
                print('Status: ', item['Status'])
                print(' Tipo: ', item['Tipo'].title())
                print('')
                print('--' * 110)
                sleep(2)

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

            else:

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t\t    FILME NÃO ENCONTRADO!                   |')
                print('|___________________________________________________________|')
                sleep(1)
                os.system('clear')


        except FileNotFoundError:

            print(' ______________________________________________________________')
            print('|                                                              |')
            print('|       Não existe nenhum filme na sua lista de desejos!       |')
            print('|______________________________________________________________|')
            sleep(1)
            os.system('clear')


    def mudar(self):

        try:
            with open('wishlist.json') as arquivo:
                altera = json.load(arquivo)
                
                print('--' * 110)
                for item in altera:

                    print(' Título: ', item['Titulo'].title())      
                    print(' Ano: ', item['Ano'])
                    print(' Tempo: ', item['Tempo'])
                    print(' Genero: ', item['Genero'])
                    print(' Diretor: ', item['Diretor'])
                    print(' Escritor: ', item['Escritor'])
                    print(' Atores: ', item['Atores'])
                    print(' País: ', item['Pais'])
                    print('Status: ', item['Status'])
                    print(' Tipo: ', item['Tipo'].title())
                    print('--' * 110)
                    sleep(1)

            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|   Digite o nome do filme que deseja alterar o status      |')
            print('|___________________________________________________________|')

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
                print('|___________________________________________________________|')
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
                        os.system('clear')
                        
                elif alterar == '2':

                    item['Status'] = 'Assistir mais tarde'

                    with open('wishlist.json', 'w') as arquivo:
                        json.dump(altera, arquivo, indent=4)

                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('|\t     Marcado como "Assistir mais tarde"             |')
                        print('|___________________________________________________________|')
                        sleep(1)
                        os.system('clear')
                        
                elif alterar == '3':

                    item['Status'] = 'Continuar assistindo'

                    with open('wishlist.json', 'w') as arquivo:
                        json.dump(altera, arquivo, indent=4)

                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('|\t      Marcado como "Continuar assistindo"           |')
                        print('|___________________________________________________________|')
                        sleep(1)
                        os.system('clear')
                        

                elif alterar == '4':
                    
                    item['Status'] = 'Nao assistido'

                    with open('wishlist.json', 'w') as arquivo:
                        json.dump(altera, arquivo, indent=4)

                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('|\t\tMarcado como "Não assistido"                |')
                        print('|___________________________________________________________|')
                        sleep(1)
                        os.system('clear') 
                        

                else:
                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|\t\t       OPÇÃO INVÁLIDA                       |')
                    print('|___________________________________________________________|')
                    sleep(1)
                    os.system('clear') 
                    
            else:
                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t  O filme não existe na sua lista de desejos!       |')
                print('|___________________________________________________________|')
                sleep(1)
                os.system('clear') 
               

        except FileNotFoundError:

            print(' ______________________________________________________________')
            print('|                                                              |')
            print('|       Não existe nenhum filme na sua lista de desejos!       |')
            print('|______________________________________________________________|')
            sleep(1)
            os.system('clear')
                    

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
                print(' Tipo: ', item['Tipo'].title())
                print('--' * 110)
                sleep(1)

            print(' ___________________________________________________________')
            print('|                                                           |')
            print('| Digite o filme que deseja excluir da sua lista de desejos |')
            print('|___________________________________________________________|')
            print('|                                                           |')
            excluir = input('| >>> ').lower().strip()
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
                    os.system('clear') 
            
            else:
                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t O filme não existe na sua lista de desejos!        |')
                print('|___________________________________________________________|')
                sleep(1)
                os.system('clear') 
                
        except FileNotFoundError:

            print(' ______________________________________________________________')
            print('|                                                              |')
            print('|       Não existe nenhum filme na sua lista de desejos!       |')
            print('|______________________________________________________________|')
            sleep(1)
            os.system('clear')


    def sugestao_ultimo(self):

        try:

            with open('wishlist.json') as arquivo:
                desejo = json.load(arquivo)

                tamanho = len(desejo)
                tamanho -= 1

                titulo = desejo[tamanho]['Titulo']

                chave = '7db9f6c4'
                response1 = requests.get("http://www.omdbapi.com/?apikey={}&s={}".format(chave,titulo)).json()

                if response1['Response'] == 'False':
                    pass

                else:

                    print('--' * 110)
                    
                    for tamanho in range(1, len(response1['Search'])):
                        
                        print(' Titulo: ', response1['Search'][tamanho]['Title'])
                        print(' Ano: ', response1['Search'][tamanho]['Year'])
                        print(' Tipo: ', response1['Search'][tamanho]['Type'])
                        print('--' * 110)
                        sleep(1)


                # print(' Titulo: ', desejo[tamanho]['Titulo'])
                # print(' Ano: ', desejo[tamanho]['Ano'])
                # print(' Tempo: ', desejo[tamanho]['Tempo'])
                # print(' Genero: ', desejo[tamanho]['Genero'])
                # print(' Diretor: ', desejo[tamanho]['Diretor'])
                # print(' Escritor: ', desejo[tamanho]['Escritor'])
                # print(' Atores: ', desejo[tamanho]['Atores'])
                # print(' País: ', desejo[tamanho]['Pais'])
                # print(' Status: ', desejo[tamanho]['Status'])
                # print(' Tipo: '), desejo[tamaho]['Tipo]
                # print('--' * 110)
                # sleep(1)

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
            

        except FileNotFoundError:

            print(' ______________________________________________________________')
            print('|                                                              |')
            print('|       Não existe nenhum filme na sua lista de desejos!       |')
            print('|______________________________________________________________|')
            sleep(1)
            os.system('clear')



    def sugestao_historico(self):
        
        try:

            with open('wishlist.json') as arquivo:
                desejo = json.load(arquivo)

            for item in desejo:

                titulo = item['Titulo']

                chave = '7db9f6c4'
                response1 = requests.get("http://www.omdbapi.com/?apikey={}&s={}".format(chave,titulo)).json()

                if response1['Response'] == 'False':
                    pass

                else:

                    for tamanho in range(1, len(response1['Search'])):
                        
                        print('--' * 110)
                        print(' Titulo: ', response1['Search'][tamanho]['Title'])
                        print(' Ano: ', response1['Search'][tamanho]['Year'])
                        print(' Tipo: ', response1['Search'][tamanho]['Type'])
                        sleep(1)

            print('--' * 110)
                            

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

        except FileNotFoundError:

            print(' ______________________________________________________________')
            print('|                                                              |')
            print('|       Não existe nenhum filme na sua lista de desejos!       |')
            print('|______________________________________________________________|')
            sleep(1)
            os.system('clear')

    #print(response['Ratings'][2]['Value'])
