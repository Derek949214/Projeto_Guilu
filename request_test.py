import requests,json
from time import sleep

class Movie:
    
    def busca_filme(self):

        lista = list()
        chave = '7db9f6c4'
        titulo = input('Digite seu Filme: ')

        status = 'Pendente'
        
        response = requests.get("http://www.omdbapi.com/?apikey={}&t={}".format(chave,titulo)).json()

        #print('Erro de conexão')

        if response['Response'] == 'False':
            
            print()
            print('O filme "{}" não existe!'.format(titulo))
            #print(response)
            return
        
        else:
            pass

        print('--' * 94)
        print('Título: ', response['Title'])      
        print('Ano: ', response['Year'])
        print('Tempo: ', response['Runtime'])
        print('Genero: ', response['Genre'])
        print('Diretor: ', response['Director'])
        print('Escritor: ', response['Writer'])
        print('Atores: ', response['Actors'])
        print('País: ', response['Country'])
        print('--' * 94)

        dicionario = {
            'Titulo': response['Title'],
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
        escolha = int(input('É esse filme que deseja adicionar a lista de desejos?\n1-Sim\n2-Não\n>>> '))
        
        

        if escolha == 1:
            flag = True
            
            try:
                with open('wishlist.json') as arquivo:
                    desejo = json.load(arquivo)

                for item in desejo:

                    if dicionario['Titulo'] == item['Titulo']:

                        print('Esse filme já existe na sua lista de desejo!')

                        sleep(1)
                        flag = False
                        break
                    
                    else:
                        flag = True

                if flag:
                    desejo.append(dicionario)

                    with open('wishlist.json', 'w') as lista_desejos:
                        json.dump(desejo, lista_desejos, indent=4)

                        print('O filme foi adicionado a sua lista de desejos com sucesso!')

                    sleep(1)
                
                else:
                    flag = False

            except FileNotFoundError:

                if flag:

                    with open('wishlist.json', 'w') as lista_desejos:
                        json.dump(lista, lista_desejos, indent=4)

                        print('O filme foi adicionado a sua lista de desejos com sucesso!')
                    sleep(1)

        if escolha == 2:
            print('Voltando para o menu...')
            print()

    def listar(self):

        try:
            with open('wishlist.json') as arquivo:
                printar = json.load(arquivo)
            
            print(json.dumps(printar, indent=4))

        except FileNotFoundError:
            print('Esse arquivo não foi criado ainda!')




    def mudar(self):

        with open('wishlist.json') as arquivo:
            altera = json.load(arquivo)

            print(json.dumps(altera, indent=4))

        mudanca = input('Digite o nome do filme que deseja alterar: ').title()

        flag = False

        for item in altera:

            if mudanca == item['Titulo']:

                flag = True
                break
                    
        if flag:
            
            alterar = input('1-Assistido\n2-Assistir mais tarde\n3-Continuar assistindo\n4-Não assistido\n>>> ')
            
            if alterar == '1':

                item['Status'] = 'Assistido'

                with open('wishlist.json', 'w') as arquivo:
                    json.dump(altera, arquivo, indent=4)

                    print('Marcado como "Assistido"')
                
            elif alterar == '2':

                item['Status'] = 'Assistir mais tarde'

                with open('wishlist.json', 'w') as arquivo:
                    json.dump(altera, arquivo, indent=4)

                    print('Marcado como "Assistir mais tarde"')
                    
            elif alterar == '3':

                item['Status'] = 'Continuar assistindo'

                with open('wishlist.json', 'w') as arquivo:
                    json.dump(altera, arquivo, indent=4)

                    print('Marcado como "Continuar assistindo"')

            elif alterar == '4':

                item['Status'] = 'Ainda vou assistir'

                with open('wishlist.json', 'w') as arquivo:
                    json.dump(altera, arquivo, indent=4)

                    print('Marcado como "Ainda vou assistir"')

            else:
                print('Opção inválida')

        else:
            print('O filme "{}" não existe na sua lista de desejos!'.format(mudanca))
                
                   

    def deletar_filme(self):

        with open('wishlist.json') as arquivo:
            delete = json.load(arquivo)

            print(json.dumps(delete, indent=4))
            
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
                


        

    #print(response['Ratings'][2]['Value'])
