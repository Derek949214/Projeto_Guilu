import requests, json, os
from time import sleep

class Sugestao:

    def repositorio(self):

        lista = list()

        chave = '7db9f6c4'
        status = 'Pendente'
                
        while True:

            os.system('clear') 
            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|\t         BUSCA DE FILMES E SÉRIES                   |')
            print('|___________________________________________________________|')
            sleep(1)
                    
            print(' ___________________________________________________________')
            print('|                                                           |')
            print('| 1-Filmes                                                  |')
            print('| 2-Series                                                  |')
            print('| 3-Menu                                                    |')
            print('|___________________________________________________________|')
            print('|                                                           |')
            escolha = input('| >>> ').lower().strip()
            print('|___________________________________________________________|')

            escolha == '1'

            if escolha == '1':

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('| Digite o nome do filme que deseja buscar                  |')
                print('|___________________________________________________________|')
                print('|                                                           |')
                pesquisa = input('| >>> ').lower().strip()
                print('|___________________________________________________________|')

                response1 = requests.get("http://www.omdbapi.com/?apikey={}&s={}&type=movie&plot=full".format(chave,pesquisa)).json()

                if response1['Response'] == 'False':
                                        
                    response = requests.get("http://www.omdbapi.com/?apikey={}&t={}&type=movie&plot=full".format(chave,pesquisa)).json()

                    if response['Response'] == 'False':
                                            
                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('| \t\t   O FILME NÃO EXISTE!                      |')
                        print('|___________________________________________________________|')
                        sleep(1)

                    else:
                                            
                        os.system('clear')
                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('|\t\t    DETALHES DO FILME                       |')
                        print('|___________________________________________________________|')
                        sleep(1)
                                            
                        print()

                        print('--' * 110)
                        print()
                        print(' Título: ', response['Title'])      
                        print(' Ano: ', response['Year'])
                        print(' Tempo: ', response['Runtime'])
                        print(' Genero: ', response['Genre'])
                        print(' Diretor: ', response['Director'])
                        print(' Escritor: ', response['Writer'])
                        print(' Atores: ', response['Actors'])
                        print(' País: ', response['Country'])
                        print(' Tipo: ', response['Type'].title())
                        print()
                        print('--' * 110)
                        break

                else:
                                    
                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|       SUGESTÕES DE FILMES RELACIONADAS COM O NOME!        |')
                    print('|___________________________________________________________|')
                    sleep(1)
                                        
                    print()
                    print('--' * 110)

                    for tamanho in range(0, len(response1['Search'])):

                        print()
                        print(' Titulo: ', response1['Search'][tamanho]['Title'])
                        print(' Ano: ', response1['Search'][tamanho]['Year'])
                        print(' Tipo: ', response1['Search'][tamanho]['Type'])
                        print()
                        print('--' * 110)
                        sleep(1)

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('| Escolha um dos filmes acima                               |')
                    print('|___________________________________________________________|')
                    print('|                                                           |')
                    titulo = input('| >>> ').strip()
                    print('|___________________________________________________________|')
                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('| Digite o ano do filme escolhido                           |')
                    print('|___________________________________________________________|')
                    print('|                                                           |')
                    ano = input('| >>> ').strip()

                    try:

                        for tamanho in range(0, len(response1['Search'])):

                            if titulo == response1['Search'][tamanho]['Title'] or ano == response1['Search'][tamanho]['Year']:

                                response = requests.get("http://www.omdbapi.com/?apikey={}&t={}&y={}&type=movie&plot=full".format(chave,titulo, ano)).json()
                                                    
                                os.system('clear')
                                print(' ___________________________________________________________')
                                print('|                                                           |')
                                print('|\t\t    DETALHES DO FILME                       |')
                                print('|___________________________________________________________|')

                                sleep(1)
                                print()
                                                    
                                print('--' * 110)
                                print()
                                print(' Título: ', response['Title'])
                                print(' Ano: ', response['Year'])
                                print(' Tempo: ', response['Runtime'])
                                print(' Genero: ', response['Genre'])
                                print(' Diretor: ', response['Director'])
                                print(' Escritor: ', response['Writer'])
                                print(' Atores: ', response['Actors'])
                                print(' País: ', response['Country'])
                                print(' Tipo: ', response['Type'].title())
                                print()
                                print('--' * 110)

                                break
                            else:
                                                                
                                tamanho += 1
                                

                            if tamanho == len(response1['Search']):
                                                    
                                os.system('clear')
                                print(' ___________________________________________________________')
                                print('|                                                           |')
                                print('|      ESTE FILME NÃO ESTÁ NA SUGESTÃO LISTADA ACIMA!       |')
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
                        print('|         ESTA SUGESTÃO NÃO ESTÁ LISTADA ACIMA!             |')
                        print('|___________________________________________________________|')
                        sleep(1.7)
                        os.system('clear')

            
            elif escolha == '2':

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('| Digite o nome da série que desejada buscar                |')
                print('|___________________________________________________________|')
                print('|                                                           |')
                pesquisa = input('| >>> ').lower().strip()
                print('|___________________________________________________________|')

                response1 = requests.get("http://www.omdbapi.com/?apikey={}&s={}&type=series&plot=full".format(chave,pesquisa)).json()
                        
                if response1['Response'] == 'False':
                            
                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('| \t\t   ESTA SÉRIE NÃO EXISTE                    |')
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

                        print()
                        print(' Titulo: ', response1['Search'][tamanho]['Title'])
                        print(' Ano: ', response1['Search'][tamanho]['Year'])
                        print(' Tipo: ', response1['Search'][tamanho]['Type'])
                        print()
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

                                response = requests.get("http://www.omdbapi.com/?apikey={}&t={}&y={}&type=series&plot=full".format(chave,titulo, ano)).json()
                                        
                                os.system('clear')
                                print(' ___________________________________________________________')
                                print('|                                                           |')
                                print('|\t\t    DETALHES DA SÉRIE                       |')
                                print('|___________________________________________________________|')

                                sleep(1)
                                print('--' * 110)
                                print()
                                print(' Título: ', response['Title'])
                                print(' Ano: ', response['Year'])
                                print(' Tempo: ', response['Runtime'])
                                print(' Genero: ', response['Genre'])
                                print(' Diretor: ', response['Director'])
                                print(' Escritor: ', response['Writer'])
                                print(' Atores: ', response['Actors'])
                                print(' País: ', response['Country'])
                                print(' Tipo: ', response['Type'].title())
                                print()
                                print('--' * 110)
                                
                                break

                            else:
                                                    
                                tamanho += 1

                            if tamanho == len(response1['Search']):
                                        
                                os.system('clear')
                                print(' ___________________________________________________________')
                                print('|                                                           |')
                                print('|      ESTA SÉRIE NÃO ESTÁ NA SUGESTÃO LISTADA ACIMA!       |')
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
                        print('|         ESTA SUGESTÃO NÃO ESTÁ LISTADA ACIMA!             |')
                        print('|___________________________________________________________|')
                        sleep(1.7)
                        os.system('clear')
                                        
                        return

            elif escolha == '3':

                return


            else:

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t\t      OPÇÃO INVÁLIDA                        |')
                print('|___________________________________________________________|')
                sleep(1)
                

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
        escolha = input('| >>> ').strip()
        print('|___________________________________________________________|')
        

        if escolha == '1':
            
            try:

                flag = True
                
                with open('sugestao.json') as arquivo:
                    sugestao = json.load(arquivo)

                for item in sugestao:

                    if dicionario['Titulo'] == item['Titulo'] and dicionario['Tipo'] == item['Tipo'] and dicionario['Ano'] == item['Ano']:

                        if dicionario['Tipo'] == 'movie':

                            print(' ___________________________________________________________')
                            print('|                                                           |')
                            print('|      ESSE FILME JÁ EXISTE NA SUA LISTA DE DESEJOS!        |')
                            print('|___________________________________________________________|')

                            sleep(2)
                            flag = False
                            os.system('clear') 
                            break

                        elif dicionario['Tipo'] == 'series':

                            print(' ___________________________________________________________')
                            print('|                                                           |')
                            print('|      ESSA SÉRIE JÁ EXISTE NA SUA LISTA DE DESEJOS!        |')
                            print('|___________________________________________________________|')

                            sleep(2)
                            flag = False
                            os.system('clear') 
                            break

                        else:
                            pass
                    
                    else:

                        flag = True

                if flag:

                    sugestao.append(dicionario)

                    with open('sugestao.json', 'w') as lista_desejos:
                        json.dump(sugestao, lista_desejos, indent=4)

                        if dicionario['Tipo'] == 'movie':
                            
                            print(' ____________________________________________________________')
                            print('|                                                            |')
                            print('| O FILME FOI ADICIONADO A SUA LISTA DE DESEJOS COM SUCESSO! |')
                            print('|____________________________________________________________|')


                        if dicionario['Tipo'] == 'series':

                            print(' ____________________________________________________________')
                            print('|                                                            |')
                            print('| A SÉRIE FOI ADICIONADA A SUA LISTA DE DESEJOS COM SUCESSO! |')
                            print('|____________________________________________________________|')

                    sleep(2)
                    os.system('clear')

                
                else:

                    flag = False

            except FileNotFoundError:

                with open('sugestao.json', 'w') as lista_desejos:
                    json.dump(lista, lista_desejos, indent=4)

                    if dicionario['Tipo'] == 'movie':
                            
                        print(' ____________________________________________________________')
                        print('|                                                            |')
                        print('| O FILME FOI ADICIONADO A SUA LISTA DE DESEJOS COM SUCESSO! |')
                        print('|____________________________________________________________|')


                    if dicionario['Tipo'] == 'series':

                        print(' ____________________________________________________________')
                        print('|                                                            |')
                        print('| A SÉRIE FOI ADICIONADA A SUA LISTA DE DESEJOS COM SUCESSO! |')
                        print('|____________________________________________________________|')

                os.system('clear')
                sleep(1)


        elif escolha == '2':

            if dicionario['Tipo'] == 'movie':

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|              O FILME NÃO FOI ADICIONADO!                  |')
                print('|___________________________________________________________|')
                sleep(1)
                os.system('clear')

            elif dicionario['Tipo'] == 'series':

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|              A SÉRIE NÃO FOI ADICIONADA!                  |')
                print('|___________________________________________________________|')
                sleep(1)
                os.system('clear')

            else:
                pass

        else:

            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|\t\t      OPÇÃO INVÁLIDA                        |')
            print('|___________________________________________________________|')
            sleep(1)

if __name__ == "__main__":
    
    os.system('clear')
    menu = Sugestao()
    menu.repositorio()