import requests
import json

def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?apikey=7db9f6c4&t=' + titulo)
        dicionario = json.loads(req.text)
        return dicionario

    except:
        print('EROOOO na conexão')
        return None


def printar_detalhes(filme):
    print(json.dumps(filme, indent = 5))


sair = False

while sair == False:
    opcao = input('Escreva o nome de um filme ou SAIR para fechar: ').upper()

    if opcao == 'SAIR':
        sair = True
        print('Saindo...')

    else:
        filme = requisicao(opcao)

        if filme['Response'] == 'False':
            print(filme)

        else:
            printar_detalhes(filme)