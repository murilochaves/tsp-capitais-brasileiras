import os
import json


def touch(file_name, io='input', method='r', bson=False):
    '''
    realiza a abertura de um arquivo e, retorna seu conteúdo
    '''

    # congelando o diretório
    path = os.path.dirname(os.path.abspath(__file__))

    # enquanto for diferente de src, realiza o processamento
    while str(path).split('\\')[-1] != 'src':

        # elevando o nível do diretório
        path = os.path.dirname(path)

    # estrutura de dados
    content = []

    # diretório do caminho do arquivo
    path = os.path.join(path, 'io', io, f'{file_name}')

    # evitando erros
    try:

        # realizando a abertura do arquivo
        with open(path, method, encoding='utf-8') as file:

            # se for leitura
            if method == 'r':

                # lendo os endereços removendo espaçamentos
                content = [line.strip() for line in file]

                # se for no formato bson
                if bson:

                    # lendo os arquivos
                    content = [json.loads(value) for value in content]

            # se for para criar
            elif method == 'w':

                # ignorando o processamento
                pass

    except FileNotFoundError:
        print(f'\np.s.: o arquivo {path} não foi encontrado\n')

    return content


if __name__ == '__main__':
    '''
    centralizando testes das funcionalidades deste código
    '''

    # abertura de arquivo
    capitals = touch(
        file_name='capitals.txt',
        io='input',
        method='r'
    )
    print(capitals)
