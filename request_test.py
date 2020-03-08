import requests,json
from time import sleep

class Movie:
    
    def busca_filme(self):
        chave = '7db9f6c4'
        titulo = input('Digite seu Filme: ')

        response = requests.get("http://www.omdbapi.com/?apikey={}&t={}".format(chave,titulo)).json() 
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
            'Status': 'Pendente'
        }
        lista = [dicionario]
        sleep(1)
        escolha = int(input('É esse filme que deseja adicionar a lista de desejos?\n1-Sim\n2-Não\n>>> '))
        
        

        if escolha == 1:
            flag = True
            
            try:
                with open('wishlist.json') as arquivo:
                    desejo = json.load(arquivo)
                
                if lista[0]['Titulo'] == desejo[0]['Titulo']:
                    print('Esse filme já existe na sua lista de desejo')


                else:
                    print()
                    with open('wishlist.json', 'a') as lista_desejos:
                        json.dump(lista, lista_desejos, indent=4)

                        print('O filme foi adicionado a sua lista de desejos com sucesso!')
            
            except FileNotFoundError:
                if flag:
                    with open('wishlist.json', 'w') as lista_desejos:
                        json.dump(lista, lista_desejos, indent=4)

                        print('O filme foi adicionado a sua lista de desejos com sucesso!')

        if escolha == 2:
            print('Voltando para o menu...')
            

    #def deletar_filme(self):



    #print(response['Ratings'][2]['Value'])
