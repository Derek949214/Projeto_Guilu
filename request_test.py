import requests,json

class Movie:

    
    def busca_filme(self,chave, titulo):
        
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
        escolha = int(input('É esse filme que deseja adicionar a lista de desejos?\n1-Sim\n2-Não\n'))
        
        

        if escolha == 1:
            flag = True

            try:
                with open('wishlist.json') as arquivo:
                    json.load(arquivo)
                
                if lista[0]['Titulo'] == arquivo[0]['Titulo']:
                    print('Esse título já existe na sua lista de desejo')
                    flag = False

                else:
                    with open('wishlist.json', 'a') as lista_desejos:
                        json.dump(lista, lista_desejos, indent=4)

                        print('Filme adicionado a sua lista de desejos com sucesso!')
            
            except FileNotFoundError:
                if flag:
                    with open('wishlist.json', 'w') as lista_desejos:
                        json.dump(lista, lista_desejos, indent=4)

                        print('Filme adicionado a sua lista de desejos com sucesso!')

        if escolha == 2:
            print('Voltando para o menu')
        
        #print(json.dumps(lista, indent=4))

    #def deletar_filme(self):


if __name__ == "__main__":   #controle de escopo de execução: serve para que um código não execute se estiver sendo apenas importado.
    movie = Movie()
    key = '7db9f6c4'
    title = input('Digite seu Filme: ')
    movie.busca_filme(key,title)
    #print(response['Ratings'][2]['Value'])
